-- Frontier Atlas: accounts, discussion, votes, progress and problem submissions.
-- Run once in the Supabase SQL editor (or `supabase db push`).
-- Everything readable by visitors goes through row-level security; writes always act as auth.uid().

create extension if not exists pgcrypto;

-- ---------- profiles ----------
create table public.profiles (
  id           uuid primary key references auth.users (id) on delete cascade,
  display_name text not null check (char_length(btrim(display_name)) between 2 and 40),
  avatar_url   text check (avatar_url is null or avatar_url ~ '^https://'),
  terms_accepted_at timestamptz,           -- set when the user confirms age 14+ and the terms
  created_at   timestamptz not null default now()
);

-- A new sign-in gets a profile. Only a GitHub handle (already public) is copied over;
-- other providers start with a neutral name so nobody's real name is shown by default.
create function public.handle_new_user() returns trigger
language plpgsql security definer set search_path = '' as $$
declare
  provider text := coalesce(new.raw_app_meta_data ->> 'provider', '');
  handle   text := nullif(btrim(coalesce(new.raw_user_meta_data ->> 'user_name', '')), '');
  avatar   text := new.raw_user_meta_data ->> 'avatar_url';
begin
  insert into public.profiles (id, display_name, avatar_url)
  values (
    new.id,
    case when provider = 'github' and char_length(coalesce(handle, '')) between 2 and 40 then handle
         else 'member-' || substr(replace(new.id::text, '-', ''), 1, 6) end,
    case when provider = 'github' and avatar ~ '^https://' then avatar else null end
  );
  return new;
end $$;

create trigger on_auth_user_created after insert on auth.users
  for each row execute function public.handle_new_user();

-- ---------- admins (managed from the SQL editor only) ----------
create table public.admins (
  user_id uuid primary key references public.profiles (id) on delete cascade
);

create function public.is_admin() returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.admins where user_id = auth.uid());
$$;

-- ---------- posts: discussion, research questions, problem submissions ----------
create table public.posts (
  id          uuid primary key default gen_random_uuid(),
  author      uuid not null default auth.uid() references public.profiles (id) on delete cascade,
  kind        text not null default 'post' check (kind in ('post', 'proposal', 'problem')),
  target      text not null check (target ~ '^(general|concept:[a-z0-9-]{1,64}|problem:[A-Za-z0-9._-]{1,80})$'),
  parent      uuid references public.posts (id) on delete cascade,
  body        text not null check (char_length(btrim(body)) between 1 and 6000),
  spoiler     boolean not null default false,
  source_note text check (char_length(source_note) <= 1000),
  solution    text check (char_length(solution) <= 6000),
  created_at  timestamptz not null default now()
);
create index posts_target_idx on public.posts (target, created_at);
create index posts_parent_idx on public.posts (parent);
create index posts_kind_idx on public.posts (kind, created_at) where parent is null;
create index posts_author_idx on public.posts (author, created_at);

-- Server-side rules a client cannot get around: timestamps, reply shape, rate limit.
create function public.posts_before_insert() returns trigger
language plpgsql security definer set search_path = '' as $$
declare p public.posts;
begin
  new.created_at := now();
  if new.parent is not null then
    select * into p from public.posts where id = new.parent;
    if not found or p.parent is not null or p.target <> new.target or p.kind = 'problem' then
      raise exception 'invalid reply' using errcode = '22023';
    end if;
    new.kind := 'post';
  end if;
  if new.kind <> 'problem' then new.source_note := null; new.solution := null; end if;
  if new.kind = 'problem' and new.target !~ '^concept:' then
    raise exception 'problems are submitted to a concept' using errcode = '22023';
  end if;
  if (select count(*) from public.posts where author = new.author and created_at > now() - interval '1 hour') >= 40 then
    raise exception 'rate limit: 40 posts per hour' using errcode = '54000';
  end if;
  return new;
end $$;
create trigger posts_before_insert before insert on public.posts
  for each row execute function public.posts_before_insert();

-- ---------- reviews of problem submissions ----------
create table public.reviews (
  post_id     uuid primary key references public.posts (id) on delete cascade,
  status      text not null check (status in ('accepted', 'declined')),
  reviewed_by uuid default auth.uid() references public.profiles (id) on delete set null,
  reviewed_at timestamptz not null default now()
);
create function public.reviews_stamp() returns trigger
language plpgsql set search_path = '' as $$
begin
  new.reviewed_by := auth.uid();
  new.reviewed_at := now();
  return new;
end $$;
create trigger reviews_stamp before insert or update on public.reviews
  for each row execute function public.reviews_stamp();

-- ---------- votes ----------
create table public.votes (
  post_id    uuid not null references public.posts (id) on delete cascade,
  user_id    uuid not null default auth.uid() references public.profiles (id) on delete cascade,
  created_at timestamptz not null default now(),
  primary key (post_id, user_id)
);
create index votes_user_idx on public.votes (user_id);

-- ---------- progress (problems a user marked solved) ----------
create table public.progress (
  user_id    uuid not null default auth.uid() references public.profiles (id) on delete cascade,
  problem_id text not null check (problem_id ~ '^[A-Za-z0-9._-]{1,120}$'),
  created_at timestamptz not null default now(),
  primary key (user_id, problem_id)
);

-- ---------- row-level security ----------
alter table public.profiles enable row level security;
alter table public.admins   enable row level security;
alter table public.posts    enable row level security;
alter table public.reviews  enable row level security;
alter table public.votes    enable row level security;
alter table public.progress enable row level security;

create policy "profiles are public"      on public.profiles for select using (true);
create policy "edit own profile"         on public.profiles for update to authenticated using (id = auth.uid()) with check (id = auth.uid());

create policy "see own admin row"        on public.admins for select to authenticated using (user_id = auth.uid());

-- Pending problem submissions (which may carry a solution) are visible only to their author and admins.
create policy "read posts" on public.posts for select using (
  kind <> 'problem'
  or author = auth.uid()
  or public.is_admin()
  or exists (select 1 from public.reviews r where r.post_id = posts.id and r.status = 'accepted')
);
create policy "write own posts"          on public.posts for insert to authenticated with check (author = auth.uid());
create policy "delete own posts or admin" on public.posts for delete to authenticated using (author = auth.uid() or public.is_admin());

create policy "reviews are public"       on public.reviews for select using (true);
create policy "admins review"            on public.reviews for all to authenticated using (public.is_admin()) with check (public.is_admin());

create policy "see own votes"            on public.votes for select to authenticated using (user_id = auth.uid());
create policy "cast own votes"           on public.votes for insert to authenticated with check (user_id = auth.uid());
create policy "remove own votes"         on public.votes for delete to authenticated using (user_id = auth.uid());

create policy "see own progress"         on public.progress for select to authenticated using (user_id = auth.uid());
create policy "mark own progress"        on public.progress for insert to authenticated with check (user_id = auth.uid());
create policy "unmark own progress"      on public.progress for delete to authenticated using (user_id = auth.uid());

-- ---------- read views ----------
-- Vote totals are public; who voted is not. This view runs as its owner so it can count every vote.
create view public.vote_counts as
  select post_id, count(*)::int as votes from public.votes group by post_id;

-- What the site reads for a thread: posts (filtered by the posts policy above), author name, vote total.
create view public.post_feed with (security_invoker = on) as
  select p.id, p.author, p.kind, p.target, p.parent, p.body, p.spoiler, p.source_note, p.solution, p.created_at,
         pr.display_name as author_name, pr.avatar_url as author_avatar,
         coalesce(v.votes, 0) as votes
  from public.posts p
  join public.profiles pr on pr.id = p.author
  left join public.vote_counts v on v.post_id = p.id;

-- Discussion size per target, for the "Solutions & discussion (n)" links.
create view public.thread_counts with (security_invoker = on) as
  select target, count(*)::int as n from public.posts where kind <> 'problem' group by target;

-- ---------- account deletion ----------
-- Deletes the caller's auth user; profile, posts, votes and progress go with it (on delete cascade).
create function public.delete_me() returns void
language plpgsql security definer set search_path = '' as $$
begin
  if auth.uid() is null then raise exception 'not signed in'; end if;
  delete from auth.users where id = auth.uid();
end $$;

-- ---------- privileges for the API roles ----------
revoke all on public.profiles, public.admins, public.posts, public.reviews, public.votes, public.progress,
              public.vote_counts, public.post_feed, public.thread_counts from anon, authenticated;
grant select on public.profiles, public.posts, public.reviews, public.vote_counts, public.post_feed, public.thread_counts to anon, authenticated;
grant update (display_name, avatar_url, terms_accepted_at) on public.profiles to authenticated;
grant select on public.admins to authenticated;
grant insert (kind, target, parent, body, spoiler, source_note, solution), delete on public.posts to authenticated;
grant insert (post_id, status), update (post_id, status), delete on public.reviews to authenticated;
grant select, insert (post_id), delete on public.votes to authenticated;
grant select, insert (problem_id), delete on public.progress to authenticated;

revoke execute on function public.delete_me() from public, anon;
grant execute on function public.delete_me() to authenticated;
revoke execute on function public.handle_new_user() from public, anon, authenticated;
revoke execute on function public.posts_before_insert() from public, anon, authenticated;
grant execute on function public.is_admin() to anon, authenticated;

-- ---------- realtime: new and deleted posts reach open pages ----------
do $$ begin
  if exists (select 1 from pg_publication where pubname = 'supabase_realtime') then
    alter publication supabase_realtime add table public.posts;
  end if;
end $$;
