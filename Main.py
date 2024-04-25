#main program
import mysql.connector as s1 #to establish connection with mysql
con1=s1.connect(host='localhost', user='root',passwd='test3008',database='company')
if con1.is_connected():
    print("                               WELCOME BACK                        ")
    print("                         Database INTERN accessed                        ")
c1=con1.cursor()
print("Please select from the below tasks:")
print(" 1: Show details to Retrieve Resumé\n"," 2: Hire Intern\n"," 3: Add intern\n"," 4: Update the progress\n"," 5: Show details of all interns")
query=''
ask='Yes'
while ask=='Yes':
    ch=int(input("Enter task number:")) #asks the task to be              done
    if ch==1: #To show details to Retrieve Resumé
        Int_Id=int(input("Enter Intern's Id:"))
        query=(query+'select* from intern_data where   Int_Id={}').format(Int_Id)
        c1.execute(query)
        d1=c1.fetchall()
        for i in d1:
            print("Displaying details required for the resumé of the intern required...")
            print("Intern's Id:", i[0])
            print("Intern's name is", i[1])
            print("Joined on", i[2])
            print("Worked as", i[4])
            print("Worked on the project",i[6])
            print("Completed it in",i[8],"months") 

   
    elif ch==2: #To hire intern
        query=query+'select* from intern_data'
        c1.execute(query)
        d2=c1.fetchall()
        for j in d2:
            if j[7]==100 and j[8]<j[5]:
                print("Displaying details of the eligible interns...")
                print(j)
            elif j[7]==100 and j[8]==j[5]:
                print("Interns which may be eligible:")
                print(j)
            else:
                print("These interns may not be fully eligible yet, to be hired.")
                print(j)
     
           
    elif ch==3: #To add the details of a new intern
        new_id=int(input("Enter new intern's id:"))
        name=input("Enter new intern's name:")
        doj=input("Enter date of joining:")
        dept=input("Enter department:")
        pos=input("Enter the position of the new intern:")
        doi=int(input("Enter duration of internship (in months):"))
        pr_as=input("Enter project assigned:")
        pro=int(input("Enter progress (in %):"))
        tci=int(input("Enter time the project has been/will be completed in (in months:"))
        query=(query+'insert into intern_data values({},"{}","{}","{}","{}",{},"{}",{},{})'.format(new_id,name,doj,dept,pos,doi,pr_as,pro,tci))
        c1.execute(query)
        print("Successfully added")
        con1.commit()





        
    elif ch==4: #To update the progress of the project
        Int_Id=int(input("Enter Intern's Id:"))
        pro=int(input("Enter current progress (in %):"))
        query=(query+'update intern_data set Progress={} where Int_Id={}').format(pro,Int_Id)
        c1.execute(query)
        print("Successfully updated")
        con1.commit()

    elif ch==5: #To show all the details of all the current interns
        query=query+'select* from intern_data'
        c1.execute(query)
        d3=c1.fetchall()
        for k in d3:
            print(k)
            
    ask=input("Do you still want to continue (Yes/No):")
    if ask=='Yes':
        continue
    else:
        break

con1.close()
