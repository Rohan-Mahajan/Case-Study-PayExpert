create database payexpert;

use payexpert;

create table employee (
    employeeId int primary key,
    firstName varchar(50) not null,
    lastName varchar(50) not null,
    dateOfBirth date not null,
    gender varchar(10) not null constraint check_gender check(gender in ('male', 'female', 'other')),
    email varchar(100) not null unique,
    phoneNumber varchar(15),
    address varchar(255),
    position varchar(50) not null,
    joiningDate date not null constraint check_joiningDate check(joiningdate < cast(getdate() as date) ),
    terminationDate date
);
drop table payroll
create table payroll(
     payrollId int primary key,
	 employeeId int,
	 payPeriodStartDate date not null,
	 payPeriodEndDate date not null,
	 constraint check_payDates check(payPeriodStartDate<=payPeriodEndDate),
	 basicSalary decimal(14,2) not null,
	 overTimePay decimal(12,2),
	 deductions decimal(12,2),
	 netSalary as (basicSalary + isnull(overTimePay, 0) - isnull(deductions, 0)) persisted,
	 constraint fk_employee_payroll foreign key(employeeId)
	 references employee(employeeId)
	 on delete cascade
	 on update cascade
);

create table tax(
     taxId int primary key,
	 employeeId int,
	 taxYear int not null,
	 taxableIncome decimal(14,2) not null,
	 taxAmount decimal(14,2) not null,
	 constraint fk_tax_employee foreign key(employeeId)
	 references employee(employeeId)
);

create table financialRecord(
     recordId int primary key,
	 employeeId int,
	 reccordDate date not null,
	 description varchar(100) not null,
	 amount decimal (14,2) not null,
	 recordType varchar(20)not null,
	 constraint fk_finRecord_employee foreign key (employeeId)
	 references employee(employeeId)
);

select * from employee;

select * from payroll;

select * from tax;

select * from financialRecord;

insert into employee (employeeid, firstname, lastname, dateofbirth, gender, email, phonenumber, address, position, joiningdate)
values 
(1, 'rohan', 'mahajan', '1990-07-07', 'male', 'rohan.mahajan@example.com', '9171835808', 'mg road, khandwa', 'sde', '2024-05-06'),
(2, 'sneha', 'sharma', '1985-03-15', 'female', 'sneha.sharma@example.com', '9182736450', 'baker street, mumbai', 'hr manager', '2023-01-10'),
(3, 'amit', 'verma', '1988-11-22', 'male', 'amit.verma@example.com', '9198765432', 'connaught place, delhi', 'analyst', '2022-09-15'),
(4, 'priya', 'patel', '1995-02-28', 'female', 'priya.patel@example.com', '9176543210', 'juhu beach, mumbai', 'designer', '2021-06-01'),
(5, 'rahul', 'kumar', '1993-05-12', 'male', 'rahul.kumar@example.com', '9187654321', 'mg road, indore', 'developer', '2020-11-20'),
(6, 'anjali', 'singh', '1992-08-30', 'female', 'anjali.singh@example.com', '9165432109', 'nehru place, delhi', 'tester', '2023-03-15'),
(7, 'vikram', 'reddy', '1987-12-25', 'male', 'vikram.reddy@example.com', '9112345678', 'bangalore road, hyderabad', 'devops engineer', '2022-04-10'),
(8,  'neha','gupta','1994-09-18','female','neha.gupta@example.com','9190123456','andheri east, mumbai','marketing executive','2023-07-20'),
(9,  'karan','chopra','1991-06-14','male','karan.chopra@example.com','9178901234','sector 17, chandigarh','sales manager','2024-01-05'),
(10,'pooja','bansal','1989-10-30','female','pooja.bansal@example.com','9187654321','navi mumbai','finance analyst','2023-02-18');

insert into payroll (payrollid, employeeid, payperiodstartdate, payperiodenddate, basicsalary, overtimepay, deductions)
values 
(1, 1, '2024-05-01', '2024-05-31', 50000.00, 5000.00, 2000.00),
(2, 2, '2024-01-01', '2024-01-31', 60000.00, 3000.00, 1500.00),
(3, 3, '2024-09-01', '2024-09-30', 55000.00, 4000.00, 2500.00),
(4, 4, '2024-06-01', '2024-06-30', 45000.00, 2000.00, 1000.00),
(5, 5, '2024-11-01', '2024-11-30', 70000.00, 6000.00, 3000.00),
(6, 6, '2023-03-01', '2023-03-31', 48000.00, 1500.00, 1200.00),
(7, 7, '2022-04-01', '2022-04-30', 75000.00, 3500.00, 4000.00),
(8, 8, '2023-07-01', '2023-07-31', 53000.00, 2500.00, 1800.00),
(9, 9,'2024-02-01','2024-02-29',60000.00 ,3000.00 ,1500.00),
(10,'10','2023-12-01','2023-12-31',55000.00 ,2000.00 ,1000.00);


insert into tax (taxid, employeeid, taxyear, taxableincome, taxamount)
values 
(1, 1,'2023 ',500000.00 ,75000.00),
(2, 2,'2023 ',600000.00 ,90000.00),
(3, 3,'2024 ',550000.00 ,82500.00),
(4, 4,'2023 ',450000.00 ,67500.00),
(5, 5,'2022 ',700000.00 ,105000.00),
(6, 6,'2023 ',480000.00 ,72000.00),
(7, 7,'2022 ',750000.00 ,112500.00),
(8, 8,'2023 ',530000.00 ,79500.00),
(9,9 , '2023',900000.00 ,900000.00),
(10,10 ,'2023 ',750000.00 ,750000.00);

insert into financialrecord (recordid, employeeid,reccorddate,
description,
amount,
recordtype)
values 
(1,'1 ','2024 -05 -15 ','salary payment ',50050.50 ,'income'),
(2,'2 ','2024 -01 -20 ','bonus payment ',10050.50 ,'income'),
(3,'3 ','2024 -09 -10 ','expense reimbursement ',5000.50 ,'expense'),
(4,'4 ','2024 -06 -25 ','travel allowance ',2500.50 ,'income'),
(5,'5 ','2024 -11 -30 ','medical expense ',2000.50 ,'expense'),
(6,'6 ','2023 -03 -15 ','salary payment ',48050.50 ,'income'),
(7,'7 ','2022 -04 -27 ','equipment purchase ',150000.50 ,'expense'),
(8,'8 ','2023 -07 -18 ','salary payment ',53050.50 ,'income'),
(9,'9 ','2019 -02 -12 ','tax payment ',150000.50 ,'tax'),
(10,'10 ','2018 -12 -31 ','investment income ',200000.50 ,'income');