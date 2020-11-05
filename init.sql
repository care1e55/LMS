create table auth(
	user_id varchar,
	email varchar,
	password varchar
)

create table users(
	id varchar,
	first_name varchar,
	middle_name varchar,
	last_name varchar,
	user_role varchar,
	email varchar,
	phone_number varchar,
	city varchar,
	about varchar,
	vk_link varchar,
	facebook_link varchar,
	linkedin_link varchar,
	instagram_link varchar
);

create table courses(
	course_id varchar,
	course_name varchar,
	description varchar);

create table running_courses(
	course_id varchar,
	course_name varchar,
	description varchar,
	teacher_id varchar,
	major_id varchar,
	materials varchar,
	homeworks varchar);

create table running_homeworks(
	homework_id varchar,
	homeworks_name varchar,
	homework_start_date varchar,
	homework_end_date varchar,
	description varchar,
	course_id varchar);


create table groups (
	course_id varchar,
	course_name varchar,
	description varchar,
	teacher_id varchar,
	major_id varchar,
	materials varchar,
	homeworks varchar);