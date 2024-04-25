import mysql.connector as s1
con1=s1.connect(host="localhost", user="root",passwd="test3008")
if con1.is_connected():
    print("done")
c1=con1.cursor()
s="create database project"
c1.execute(s)

as1="use project"
c1.execute(as1)

st1='create table Intern_data(int_id int PRIMARY KEY,int_name varchar(25)NOT NULL,date_of_joining date NOT NULL,department varchar(50),position varchar(50),DOI int, project_assigned varchar(50)NOT NULL, progress int NOT NULL,tci int)'
c1.execute(st1)

st2="insert into Intern_data values(101,'Anya','2022-06-18','Business strategy','Business Analyst',6,'Re-assess customer/client needs',50,8)"
c1.execute(st2)

st3="insert into Intern_data values(102,'Sophie','2022-04-20','Engineering & Technology','Software Engineer',6,'Debug application',100,6)"
c1.execute(st3)

st4="insert into Intern_data values(103,'Danny','2022-03-21','Finance','Financial Advisor',8,'Respond to client inquiries',100,7)"
c1.execute(st4)

st5="insert into Intern_data values(104,'Jansie','2022-04-23','Design','Design manager',5,'Product Design',100,6)"
c1.execute(st5)

st6="insert into Intern_data values(106,'Malcolm','2022-08-07','Engineering & Technology','Software Engineer',5,'Software development',100,7)"
c1.execute(st6)

st7="insert into Intern_data values(105,'Ravi','2022-06-16','Business strategy','Business analyst',7,'Evaluate enhancement',100,7)"
c1.execute(st7)

con1.commit()

