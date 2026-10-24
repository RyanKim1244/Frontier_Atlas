\set ON_ERROR_STOP 0
\set QUIET 1
-- users: a (github), b (google), admin (kakao)
insert into auth.users (id, raw_app_meta_data, raw_user_meta_data) values
 ('00000000-0000-0000-0000-00000000000a', '{"provider":"github"}', '{"user_name":"alice-gh","avatar_url":"https://avatars.githubusercontent.com/u/1"}'),
 ('00000000-0000-0000-0000-00000000000b', '{"provider":"google"}', '{"full_name":"Bob Real Name","avatar_url":"https://lh3.googleusercontent.com/x"}'),
 ('00000000-0000-0000-0000-0000000000ad', '{"provider":"kakao"}',  '{"name":"관리자"}');
insert into public.admins values ('00000000-0000-0000-0000-0000000000ad');
select id, display_name, avatar_url from profiles order by id;

-- as A
set role authenticated; set request.jwt.claim.sub = '00000000-0000-0000-0000-00000000000a';
insert into posts (target, body) values ('concept:divisibility', 'hello $x$') ;
insert into posts (target, body, spoiler, kind) values ('problem:IMO-2026-P1', 'my solution', true, 'post');
insert into posts (kind, target, body, source_note, solution) values ('problem', 'concept:divisibility', 'Show 6 | n^3-n', 'own', 'factor');
\echo expect ERROR author spoof (no privilege on column author)
insert into posts (author, target, body) values ('00000000-0000-0000-0000-00000000000b', 'concept:divisibility', 'spoof');
\echo expect ERROR bad target
insert into posts (target, body) values ('javascript:alert(1)', 'x');
\echo expect ERROR problem to non-concept
insert into posts (kind, target, body) values ('problem', 'problem:IMO-2026-P1', 'x');
\echo expect ERROR empty body
insert into posts (target, body) values ('general', '   ');
insert into progress (problem_id) values ('IMO-2026-P1'), ('PUTNAM-1962-A4');
\echo expect ERROR progress for someone else
insert into progress (user_id, problem_id) values ('00000000-0000-0000-0000-00000000000b', 'X');
\echo expect ERROR review as non-admin
insert into reviews (post_id, status) select id, 'accepted' from posts where kind='problem';
\echo expect ERROR change author name to 1 char
update profiles set display_name = 'x' where id = auth.uid();
update profiles set display_name = 'Alice' where id = auth.uid();
\echo expect 0 rows updated (other profile)
update profiles set display_name = 'Hacked' where id = '00000000-0000-0000-0000-00000000000b';

-- as B
set request.jwt.claim.sub = '00000000-0000-0000-0000-00000000000b';
\echo B sees (expect 2 posts, no pending problem):
select kind, target, body, author_name, votes from post_feed order by created_at;
insert into votes (post_id) select id from posts where target = 'concept:divisibility' and kind = 'post';
\echo expect ERROR double vote
insert into votes (post_id) select id from posts where target = 'concept:divisibility' and kind = 'post';
insert into posts (target, parent, body) select target, id, 'reply' from posts where target = 'concept:divisibility' and kind='post';
\echo expect ERROR reply across targets
insert into posts (target, parent, body) select 'general', id, 'reply' from posts where target = 'concept:divisibility' and kind='post';
\echo reply to reply now allowed (nested threads)
insert into posts (target, parent, body) select target, id, 'r2' from posts where body = 'reply';
\echo expect 0 deleted (A post)
delete from posts where body = 'hello $x$';
\echo B progress (expect 0):
select count(*) from progress;
\echo B admin rows (expect 0):
select count(*) from admins;
select public.is_admin() as b_is_admin;

-- as admin
set request.jwt.claim.sub = '00000000-0000-0000-0000-0000000000ad';
select public.is_admin() as admin_is_admin;
\echo admin sees pending problem:
select kind, body, solution from post_feed where kind = 'problem';
insert into reviews (post_id, status) select id, 'accepted' from posts where kind='problem';
insert into reviews (post_id, status) select id, 'declined' from posts where kind='problem' on conflict (post_id) do update set post_id = excluded.post_id, status = excluded.status;
insert into reviews (post_id, status) select id, 'accepted' from posts where kind='problem' on conflict (post_id) do update set post_id = excluded.post_id, status = excluded.status;
select status, reviewed_by from reviews;

-- anon
reset role; set role anon; set request.jwt.claim.sub = '';
\echo anon sees (expect 3 posts incl accepted problem + reply):
select kind, target, body, votes from post_feed order by created_at;
select * from thread_counts order by target;
\echo expect ERROR anon insert
insert into posts (target, body) values ('general', 'x');
\echo anon votes table (expect ERROR or 0):
select count(*) from votes;
select * from vote_counts;

-- rate limit
reset role; set role authenticated; set request.jwt.claim.sub = '00000000-0000-0000-0000-00000000000b';
do $$ begin for i in 1..45 loop begin insert into posts (target, body) values ('general', 'spam ' || i); exception when others then raise notice 'stopped at %: %', i, sqlerrm; exit; end; end loop; end $$;

-- delete account (A)
set request.jwt.claim.sub = '00000000-0000-0000-0000-00000000000a';
select public.delete_me();
reset role;
\echo after deleting A: users, profiles, A posts, A progress, votes on A posts
select (select count(*) from auth.users), (select count(*) from profiles), (select count(*) from posts where author='00000000-0000-0000-0000-00000000000a'), (select count(*) from progress), (select count(*) from votes);
\echo anon delete_me (expect ERROR permission)
set role anon; select public.delete_me();
