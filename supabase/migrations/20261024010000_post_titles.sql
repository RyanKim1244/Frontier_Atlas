-- Titles for posts (required for research questions by the site; optional elsewhere).
alter table public.posts add column if not exists title text check (title is null or char_length(btrim(title)) between 1 and 150);
grant insert (title) on public.posts to authenticated;

create or replace view public.post_feed with (security_invoker = on) as
  select p.id, p.author, p.kind, p.target, p.parent, p.body, p.spoiler, p.source_note, p.solution, p.created_at,
         pr.display_name as author_name, pr.avatar_url as author_avatar,
         coalesce(v.votes, 0) as votes, p.title
  from public.posts p
  join public.profiles pr on pr.id = p.author
  left join public.vote_counts v on v.post_id = p.id;
grant select on public.post_feed to anon, authenticated;
