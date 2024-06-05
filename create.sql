use datalab;
create table award(
	id char(10),
    award varchar(10),
    award_time date,
    award_name varchar(50),
    primary key(id,award,award_time,award_name)
);
create table stu(
	id char(10) primary key,
    name varchar(5),
    major varchar(20),
    doc varchar(20),
    award_times int default 0
);
create table course(
	id char(10),
    course_num varchar(15),
    course_name varchar(15),
    cred int default 0,
    have_grade varchar(10) default 'false',
    primary key(id,course_num)
);
create table course_grade(
	id char(10),
    course_num varchar(15),
    course_name varchar(15),
    cred int default 0,
    grade int default 0,
    primary key(id,course_num)
);

delimiter //
create procedure commit_grade(id char(10),course_num varchar(15),course_name varchar(15),grade int)
begin
	declare s int default 0;
    declare a int default 0;
    declare cre int default 0;
    declare continue handler for sqlexception set s=1;
	start transaction;
    select course.cred into cre
    from course
    where course.id=id and course.course_num=course_num;
    if cre=0 then
		set s=1;
	end if;
    update course
    set have_grade='true'
    where course.id=id and course.course_num=course_num;
	insert into course_grade
    Values(id,course_num,course_name,cre,grade);
    if s=1 then
		rollback;
	else 
		commit;
	end if;
end //
delimiter ;

delimiter //
create function gpa(id char(10))
returns float
reads sql data
begin
	declare state int default 0;
    declare grade,cred,total_g,total_c float default 0;
    declare ct cursor for(
		select course_grade.grade,course_grade.cred from course_grade where course_grade.id=id);
	declare continue handler for not found set state=1;
    open ct;
    repeat
		fetch ct into grade,cred;
        if state=0 then
			set total_g=total_g+grade*cred;
            set total_c=total_c+cred;
		end if;
		until state=1
	end repeat;
    close ct;
    if total_c=0 then
		return 0;
	else
		return total_g/total_c;
	end if;
end//
delimiter ;

delimiter //
create trigger A
after insert on award for each row 
begin
	update stu
    set award_times=award_times+1
    where stu.id=new.id;
end//
create trigger B
after delete on award for each row
begin
	update stu	
    set award_times=award_times-1
    where stu.id=old.id;
end//
delimiter ;
