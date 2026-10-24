-- Reddit-style threads: replies may answer replies, up to 8 levels deep, always within the same target.
create or replace function public.posts_before_insert() returns trigger
language plpgsql security definer set search_path = '' as $$
declare p public.posts; depth int := 0; cur uuid;
begin
  new.created_at := now();
  if new.parent is not null then
    select * into p from public.posts where id = new.parent;
    if not found or p.target <> new.target or p.kind = 'problem' then
      raise exception 'invalid reply' using errcode = '22023';
    end if;
    cur := p.parent;
    while cur is not null loop
      depth := depth + 1;
      if depth >= 8 then raise exception 'thread too deep' using errcode = '22023'; end if;
      select parent into cur from public.posts where id = cur;
    end loop;
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
