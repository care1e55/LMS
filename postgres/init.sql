--########CREATE SCHEMA OBJECTS########


CREATE EXTENSION IF NOT EXISTS "uuid-ossp";


create table if not exists auth(
	user_id UUID primary key DEFAULT uuid_generate_v1(),
	email varchar UNIQUE,
	password varchar UNIQUE,
	"role" varchar,
	registration_code varchar,
	is_active bool
);

create table if not exists students(
	student_id uuid primary key DEFAULT uuid_generate_v1(),
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

create table if not exists user_profile(
	profile_id UUID primary key DEFAULT uuid_generate_v1(),
	user_id UUID,
	email varchar,
	phone_number varchar,
	city varchar,
	about varchar,
	vk_link varchar,
	facebook_link varchar,
	linkedin_link varchar,
	instagram_link varchar,
	CONSTRAINT user_id FOREIGN KEY(user_id) REFERENCES auth(user_id)
);

create table if not exists teachers(
	user_id UUID,
	teacher_id uuid primary key,
	first_name varchar,
	middle_name varchar,
	last_name varchar,
	CONSTRAINT user_id FOREIGN KEY(user_id) REFERENCES auth(user_id)
);

create table if not exists groups(
	group_id varchar primary key,
	group_name varchar,
	description varchar);

create table if not exists courses(
	course_id uuid primary key DEFAULT uuid_generate_v1(),
	course_name varchar,
	description varchar,
	group_id varchar,
	teacher_id varchar,
	major_id varchar
);

create table if not exists materials(
	material_id uuid primary key DEFAULT uuid_generate_v1(),
	material_name varchar,
	material_content varchar,
--	add_date date,
	add_date varchar,
	course_id uuid
);

create table if not exists homeworks(
	homework_id uuid primary key DEFAULT uuid_generate_v1(),
	homeworks_name varchar,
	homework_start_date varchar,
	homework_end_date varchar,
	description varchar,
	course_id varchar);

create table if not exists solutions(
	solution_id uuid primary key DEFAULT uuid_generate_v1(),
	homework_id varchar,
	student_id varchar,
	course_id varchar,
	description varchar);


--########FILL TEST DATA########

INSERT INTO public.groups(group_id, group_name, description ) VALUES(
	'1', 
	'GR1', 
	'group of students'
);

INSERT INTO public.groups(group_id, group_name, description ) VALUES(
	'2', 
	'GR2', 
	'group of students'
);

INSERT INTO public.auth(user_id, email, "password", "role", registration_code, is_active) VALUES(
	'00000000-0000-0000-0000-000000000001', 
	'student1@example.com', 
	'student1',
	'student',
	'code1',
	false
);

INSERT INTO public.auth(user_id, email, "password", "role", registration_code, is_active) VALUES(
	'00000000-0000-0000-0000-000000000002', 
	'student2@example.com', 
	'student2',
	'student',
	'code2',
	false
);

INSERT INTO public.auth(user_id, email, "password", "role", registration_code, is_active) VALUES(
	'00000000-0000-0000-0000-000000000003', 
	'student3@example.com', 
	'student3',
	'student',
	'code3',
	false
);

INSERT INTO public.auth(user_id, email, "password", "role", registration_code, is_active) VALUES(
	'00000000-0000-0000-0000-000000000004', 
	'teacher1@example.com', 
	'teacher1',
	'teacher',
	'code4',
	false
);

INSERT INTO public.students(
	student_id, 
	first_name, 
	middle_name, 
	last_name, 
	group_id, 
	enter_year, 
	major, 
	education_form, 
	education_base, 
	user_id)
VALUES(
	'00000000-0000-0000-0001-000000000001', 
	'student1_first_name', 
	'student1_middle_name', 
	'student1_last_name', 
	'1', 
	'01.09.2020', 
	'', 
	'day', 
	'free', 
	'00000000-0000-0000-0000-000000000001'
);

INSERT INTO public.students(
	student_id, 
	first_name, 
	middle_name, 
	last_name, 
	group_id, 
	enter_year, 
	major, 
	education_form, 
	education_base, 
	user_id)
VALUES(
	'00000000-0000-0000-0001-000000000002', 
	'student2_first_name', 
	'student2_middle_name', 
	'student2_last_name', 
	'1', 
	'01.09.2020', 
	'', 
	'day', 
	'free', 
	'00000000-0000-0000-0000-000000000002'
);

INSERT INTO public.students(
	student_id, 
	first_name, 
	middle_name, 
	last_name, 
	group_id, 
	enter_year, 
	major, 
	education_form, 
	education_base, 
	user_id)
VALUES(
	'00000000-0000-0000-0001-000000000003', 
	'student3_first_name', 
	'student3_middle_name', 
	'student3_last_name', 
	'2', 
	'01.09.2020', 
	'', 
	'day', 
	'free', 
	'00000000-0000-0000-0000-000000000003'
);

INSERT INTO public.user_profile(
	profile_id,
	user_id,
	email,
	phone_number,
	city,
	about,
	vk_link,
	facebook_link,
	linkedin_link,
	instagram_link)
VALUES(
	'00000000-0000-0000-0002-000000000001',
	'00000000-0000-0000-0000-000000000001',
	'student1@example.com',
	'+7-900-111-22-33',
	'Moscow',
	'',
	'vk.com/exmaple',
	'facebook.com/exmaple',
	'linkedin.com/exmaple',
	'instagram.com/exmaple'
);

INSERT INTO public.user_profile(
	profile_id,
	user_id,
	email,
	phone_number,
	city,
	about,
	vk_link,
	facebook_link,
	linkedin_link,
	instagram_link)
VALUES(
	'00000000-0000-0000-0002-000000000002',
	'00000000-0000-0000-0000-000000000002',
	'student2@example.com',
	'+7-902-111-22-33',
	'Moscow',
	'',
	'vk.com/exmaple',
	'facebook.com/exmaple',
	'linkedin.com/exmaple',
	'instagram.com/exmaple'
);

INSERT INTO public.user_profile(
	profile_id,
	user_id,
	email,
	phone_number,
	city,
	about,
	vk_link,
	facebook_link,
	linkedin_link,
	instagram_link)
VALUES(
	'00000000-0000-0000-0002-000000000003',
	'00000000-0000-0000-0000-000000000003',
	'student2@example.com',
	'+7-903-111-22-33',
	'Moscow',
	'',
	'vk.com/exmaple',
	'facebook.com/exmaple',
	'linkedin.com/exmaple',
	'instagram.com/exmaple'
);

INSERT INTO public.teachers(
	user_id,
	teacher_id,
	first_name,
	middle_name,
	last_name
)
VALUES(
	'00000000-0000-0000-0000-000000000004',
	'00000000-0000-0000-0003-000000000004',
	'teacher1_first_name',
	'teacher1_middle_name',
	'teacher1_last_name'
);

INSERT INTO public.courses(
	course_id,
	course_name,
	description,
	group_id,
	teacher_id,
	major_id
)
VALUES(
	'00000000-0000-0000-0004-000000000001',
	'course_name_1',
	'description',
	'1',
	'00000000-0000-0000-0003-000000000004',
	''
);

INSERT INTO public.materials
(
	material_id,
	material_name,
	material_content,
	add_date,
	course_id
)
VALUES(
	'00000000-0000-0000-0005-000000000001',
	'material1_name',
	'material1_content',
	'19.30.2020',
	'00000000-0000-0000-0004-000000000001'
);

INSERT INTO public.homeworks(
	homework_id,
	homeworks_name,
	homework_start_date,
	homework_end_date,
	description,
	course_id
) 
VALUES(
'00000000-0000-0000-0005-000000000001',
'homeworks_name',
'19.12.2020',
'26.12.2020',
'description',
'00000000-0000-0000-0004-000000000001'
);

INSERT INTO public.solutions(
	solution_id,
	homework_id,
	student_id,
	course_id,
	description
)
VALUES(
	'00000000-0000-0000-0006-000000000001',
	'00000000-0000-0000-0005-000000000001',
	'00000000-0000-0000-0001-000000000001',
	'00000000-0000-0000-0004-000000000001',
	'description'
);
