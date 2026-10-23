-- Profile: a short public "about" text.
alter table public.profiles add column if not exists bio text not null default ''
  check (char_length(bio) <= 500);
grant update (bio) on public.profiles to authenticated;
