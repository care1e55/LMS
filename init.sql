create table auth(
	user_id UUID primary key DEFAULT uuid_generate_v1(),
	email varchar,
	password varchar
);


create table students(
	student_id uuid primary key,
	first_name varchar,
	middle_name varchar,
	last_name varchar,
	group_id varchar,
	enter_year date,
	major varchar,
	education_form varchar,
	education_base varchar,
	user_id UUID,
	CONSTRAINT user_id FOREIGN KEY(user_id) REFERENCES auth(user_id)
--	CONSTRAINT group_id FOREIGN KEY(group_id) REFERENCES groups(group_id)
);


create table profile(
	user_id UUID,
	email varchar,
	phone_number varchar,
	city varchar,
	about varchar,
	vk_link varchar,
	facebook_link varchar,
	linkedin_link varchar,
	instagram_link varchar,
	education varchar,
	CONSTRAINT user_id FOREIGN KEY(user_id) REFERENCES auth(user_id)
);


create table teachers(
	user_id UUID,
	teacher_id uuid primary key,
	first_name varchar,
	middle_name varchar,
	last_name varchar,
	CONSTRAINT user_id FOREIGN KEY(user_id) REFERENCES auth(user_id)
);


create table courses(
	course_id uuid primary key,
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


create table homeworks(
	homework_id uuid primary key,
	homeworks_name varchar,
	homework_start_date varchar,
	homework_end_date varchar,
	description varchar,
	course_id varchar);


create table groups(
	group_id uuid primary key,
	group_name varchar,
	description varchar,
	-- teacher_id varchar,
	-- major_id varchar,
	-- materials varchar,
	-- homeworks varchar);








