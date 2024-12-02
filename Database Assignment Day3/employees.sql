SELECT * FROM Assignment.employees;
USE Assignment;
SET SQL_SAFE_UPDATES = 0; 

CREATE table employees(
	id int auto_increment primary key,
    name varchar(100),
    position varchar(100),
    salary decimal(10,2)
    );

INSERT INTO employees (name, position, salary) VALUES
('혜린', 'PM', 90000),
('은우', 'Frontend',80000),
('가을', 'Backend', 92000),
('지수', 'Frontend', 78000),
('민혁', 'Frontend', 96000),
('하온', 'Backend', 130000);

SELECT name,salary from employees;

SELECT name, salary from employees where position = 'frontend' and salary <= 90000;

update employees set salary = salary * 1.10 where position = 'PM';
select * from employees where position = 'PM';

update employees set salary = salary * 1.05 where position = 'Backend';
select * from employees where position = 'Backend';

delete from employees where name = '민혁';

select position, avg(salary) as average_salary from employees group by position;

drop table employees;