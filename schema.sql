 CREATE TABLE mst_party_type(id serial primary key, name varchar(20));
 create table mst_party_representation_type(id serial primary key, name varchar(30));
 create table attorney(id serial primary key, name varchar(30));
 create table mst_case_type_category(id serial primary key, name varchar(20));
 create table mst_case_type_group(id serial primary key, mst_case_type_category_id int serial
 references mst_case_type_category(id), name varchar(30));
create table mst_case_type(id serial primary key, mst_case_type_group_id serial
references mst_case_type_group(id), name varchar(30));
create table courtcase(id serial primary key, case_key varchar(25), case_name varchar(30), case_number varchar(20), filing_date
create table mst_courthouse(id serial primary key, mst_jurisdiction serial references mst_jurisdiction(id), name varchar(30));
create table mst_jurisdiction(id serial primary key, name varchar(30));
create table mst_case_status(id serial primary key, name varchar(30));
create table mst_case_status_category(id serial primary key, name varchar(30));
create table court_case(id serial primary key, case_key varchar(25), case_name varchar(20), case_number varchar(20),
filing_date date, mst_case_type_id serial references mst_case_type(id), mst_case_status_category_id serial
references mst_case_status_category(id),  mst_case_status_id serial references mst_case_status(id),
mst_courthouse_id serial references mst_courthouse(id),
judge_name varchar(20), created_date timestamp, last_update_date timestamp);