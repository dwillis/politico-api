drop table if exists stories;
create table stories (
  id integer primary key autoincrement,
  title text not null,
  date datetime not null,
  ad_unit_section text null,
  uuid text not null,
  story_type text not null,
  current_headline text not null,
  original_headline text not null,
  source text not null,
  content_id integer,
  authors text not null,
  section text not null,
  text text not null
);

drop table if exists authors;
create table authors (
  id integer primary key autoincrement,
  name text not null,
  slug text not null,
  story_count integer
);

drop table if exists tags;
create table tags (
  id integer primary key autoincrement,
  name text not null,
  slug text not null
);

drop table if exists story_tags;
create table story_tags (
  id integer primary key autoincrement,
  story_id integer not null,
  tag_id integer not null
);
