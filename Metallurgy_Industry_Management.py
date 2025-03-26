import mysql.connector
mydb = mysql.connector.connect (host="localhost",
                                user="root",
                                passwd="R@ghav_2005")
print(mydb)
mc=mydb.cursor()
mc.execute("CREATE DATABASE METALLURGY_INDUSTRY_MANAGEMENT")
mc.execute("USE METALLURGY_INDUSTRY_MANAGEMENT")
mc.execute("CREATE TABLE IF NOT EXISTS ORE ( SRNO INT PRIMARY KEY,\
ORENAME VARCHAR(20),ORECHEMICALFORMULA VARCHAR(20),METAL VARCHAR(20),PRICE_perqntl INT )")
mc.execute("CREATE TABLE IF NOT EXISTS WORKERS( W_ID INT PRIMARY KEY,W_NAME VARCHAR(20),CONTACTNO INT,DEPARTMENT VARCHAR(20))")
mc.execute("CREATE TABLE IF NOT EXISTS FINANCIAL_INFO( SRNO INT PRIMARY KEY, SALARY INT,W_ID INT REFERENCES WORKER (W_ID))")
mc.execute("INSERT INTO ORE VALUES(1,'TINSTONE','SNO2','TIN',15000)") 
mc.execute("INSERT INTO ORE VALUES(2,'ZINCITE','ZnO','ZINC',12000)")
mc.execute("INSERT INTO ORE VALUES(3,'NITRATE ORE','NANO3','SODIUM',20000)")
mc.execute("INSERT INTO WORKERS VALUES('101','RAMU',985003695,'REFINING'),('102','SHAMJI',800555555,'SMELTING')")
mc.execute("INSERT INTO WORKERS VALUES('103','RAMJI',800555455,'SMELTING'),('104','RAMAVTAR',958552100,'GRINDING')")
mc.execute("INSERT INTO WORKERS VALUES('105','NARENDRA',800544555,'LEACHING')")
mc.execute("INSERT INTO FINANCIAL_INFO VALUES(1,20000,103),(2,25000,102)")
mc.execute("INSERT INTO FINANCIAL_INFO VALUES(3,24000,101),(4,26000,104)")
mc.execute("INSERT INTO FINANCIAL_INFO VALUES(5,28000,105)")
mydb.commit()
for i in mc:
    print(i)
def add_ore():
    while True:
        mc=mydb.cursor()
        print('ENTER THE FOLLOWING DETAILS')
        SRNO=int(input('Enter serial no : '))
        ORENAME=input('Enter ore name: ')
        ORECHEMICALFORMULA=input('Enter chemical formula : ')
        METAL= input('Enter Metal Name :')
        PRICE= int(input('Enter price(per quintal) : '))
        query="INSERT INTO ORE VALUES({},'{}','{}','{}',{})".format(SRNO,ORENAME,ORECHEMICALFORMULA,METAL,PRICE)
        mc.execute(query)
        mydb.commit()
        if mc.rowcount>0:
            print('RECORDS ADDED SUCCESSFULLY!!!')
        x= input('Do you want to add more (y/n): ')
        if (x== "y" or x=="Y"):
            continue
        else:
            break
        a=int(input('Enter 1 to continue OR 2 to Exit : '))
        if a==1:
            continue
        elif a==2:
            break
        else:
            print("Wrong input")

def delete_ore():
    while True:
        mc=mydb.cursor()
        a = int(input('Enter serialno = '))
        query='delete from ore where srno ={}'.format(a )
        mc.execute(query)
        mydb.commit()
        if mc.rowcount>0:
            print('RECORD DELETED SUCCESSFULLY!!')
        else:
            print('RECORDS DONT EXIST___: ')
        x = input('Do you want to delete more (y/n): ')
        if (x== "y" or x=="Y"):
            continue
        else:
            break
        

def update_ore():
    while True:
        mc=mydb.cursor()
        y=int(input('Enter the ORE serial no. whose records you wish to update: '))
        print('Which colomn do you wish to edit:\n>1-SRNO\n>2-ORENAME\n>3-ORECHEMICALFORMULA\n>4-METAL\n>5-PRICE_perqntl')
        x=int(input('ENTER CHOICE:'))
        if x==1:
            srno=int(input('Enter new serialno: '))
            query= 'update ORE set SRNO ={} where SRNO ={}'.format(srno,y)
            mc.execute(query)
            mydb.commit()
            print('RECORD UPDATED SUCCESSFULLY!!')
        elif x==2:
            name=input('ENTER NEW ORE NAME : ')
            query='update ore set orename="{}" where srno ={}'.format(name,y)
            mc.execute(query)
            mydb.commit()
            print('RECORD UPDATED SUCCESSFULLY!!!')
        elif x==3:
            orechem= input('ENTER NEW ore chemical formula = ')
            query='update ore set ORECHEMICALFORMULA= "{}" where srno={}'.format(orechem,y)
            mc.execute(query)
            mydb.commit()
            print('RECORD UPDATED SUCCESSFULLY!!')
        elif x==4:
            m= input('ENTER NEW METAL= ')
            query='update ore set metal="{}" where srno={}'.format(m,y)
            mc.execute(query)
            mydb.commit()
            print('RECORD UPDATED SUCCESSFULLY!!')
        elif x==5:
            p= int(input('ENTER NEW PRICE= '))
            query='update ore set price_perqntl= {} where srno={}'.format(p,y)
            mc.execute(query)
            mydb.commit()
            print('RECORD UPDATED SUCCESSFULLY!!')
        else:
            print('WRONG INPUT TRY AGAIN!')
        a=int(input('PRESS 0 TO EXIT OR ANY OTHER NUMBER TO KEEP UPDATING:'))
        if a==0:
            break
        else:
            continue
def display_ore():
    while True:
        mc=mydb.cursor()
        print('Choose what records you wish to view\n1-ORENAME\n2-ORECHEMICALFORMULA\n3-METAL\n4-EVERY RECORD EXISTING')
        y=int(input('Enter choice= '))
        if y==1:
            mc=mydb.cursor()
            x=int(input('Enter ore serial no whose records you wish to view= '))
            query='select SRNO,ORENAME from ore where SRNO="{}"'.format(x)
            mc.execute(query)
            for i in mc:
                print(i)
            if mc.rowcount==0:
                print('WRONG INPUT TRY AGAIN')
                continue
        elif y==2:
            mc=mydb.cursor()
            x=int(input('Enter ore serial no whose records you wish to view= '))
            query='select SRNO,ORECHEMICALFORMULA from ore where SRNO={}'.format(x)
            mc.execute(query)
            for i in mc:
                print(i)
            if mc.rowcount==0:
                print('WRONG INPUT TRY AGAIN')
                continue
        elif y==3:
            mc=mydb.cursor()
            x=int(input('Enter ore serial no whose records you wish to view= '))
            query='select SRNO,METAL from ore where SRNO={}'.format(x)
            mc.execute(query)
            for i in mc:
                print(i)
        elif y==4:
            mc=mydb.cursor()
            query='select * from ore'
            mc.execute(query)
            for i in mc:
                print(i)
        y=int(input('Enter 1 to continue OR 2 to Exit : '))
        if y==1:
            continue
        elif y==2:
            break
        else:
            print("Wrong input")


def add_worker():
    while True:
        mc=mydb.cursor()
        print('ENTER THE FOLLOWING DETAILS')
        W_ID=int(input('Enter worker id : '))
        W_NAME=input('Enter Worker name : ')
        CONTACTNO =int(input('Enter contact no : '))
        DEPARTMENT=input('Enter department: ')
        query="INSERT INTO WORKERS VALUES({},'{}','{}','{}')".format(W_ID,W_NAME,CONTACTNO,DEPARTMENT)
        mc.execute(query)
        mydb.commit()
        print('RECORDS ADDED SUCCESSFULLY!!!')
        x=int(input('Enter 1 to view the added records, 0 to exit or any other number to continue adding records=  '))
        if x==1:
            new='select * from workers where W_ID={}'.format(W_ID)
            mc.execute(new)
            for i in mc:
                print(i)
        x=int(input('Enter 0 to exit or any other number to continue adding records=  '))
        if x==0:
            break

def delete_worker():
    while True:
        mc=mydb.cursor()
        print('Enter the Worker ID whose records you wish to delete')
        x=int(input('Worker ID = '))
        query='delete from workers where W_ID={}'.format(x)
        mc.execute(query)
        if mc.rowcount>0:
            print('RECORDS DELETED SUCCESSFULLY!!')
        else:
            print('RECORD NOT FOUND TRY AGAIN!!')
        y=int(input('Enter 1 to continue OR 2 to Exit : '))
        if y==1:
            continue
        elif y==2:
            break
        else:
            print("Wrong input")

def update_worker():
    while True:
        mc=mydb.cursor()
        y=input('Enter the Worker ID whose records you wish to update: ')
        print('Which colomn do you wish to edit:\n1-W_ID\n2-W_NAME\n3-CONTACTNO\n>4-DEPARTMENT')
        x=int(input('ENTER CHOICE:'))
        if x==1:
            ID_NEW= int(input('Ennter new W_ID : '))
            query='update workers set W_ID="{}" where W_ID={}'.format(ID_NEW,y)
            mc.execute(query)
            mydb.commit()
            print('RECORD UPDATED SUCCESSFULLY!!')
        elif x==2:
            NAME_NEW=input('Enter new Worker name : ')
            query='update workers set W_NAME="{}" where W_ID={}'.format(NAME_NEW,y)
            mc.execute(query)
            mydb.commit()
            print('RECORD UPDATED SUCCESSFULLY!!')
        elif x==3:
            Con_NEW=int(input('Enter new contact number = '))
            query='update workers set CONTACTNO={} where W_ID={}'.format(Con_NEW,y)
            mc.execute(query)
            mydb.commit()
            print('RECORD UPDATED SUCCESSFULLY!!')
        elif x==4:
            Dept_NEW=input('Enter new department = ')
            query='update WORKERS set DEPARTMENT="{}" where W_ID={}'.format(Dept_NEW,y)
            mc.execute(query)
            mydb.commit()
            print('RECORD UPDATED SUCCESSFULLY!!')
        else:
            print('WRONG INPUT TRY AGAIN!')
        y=int(input('Enter 1 to continue OR 2 to Exit : '))
        if y==1:
            continue
        elif y==2:
            break
        else:
            print("Wrong input")

def display_workers():
    while True:
        mc=mydb.cursor()
        print('Choose what records you wish to view\n1-Worker Name\n2-Contact no\n3-Department\n4-All\n5-EVERY RECORD EXISTING')
        y=int(input('Enter choice= '))
        if y==1:
            mc=mydb.cursor()
            x=int(input('Enter worker ID whose records you wish to view= '))
            query='select W_ID,W_NAME from workers where W_ID="{}"'.format(x)
            mc.execute(query)
            for i in mc:
                print(i)
            if mc.rowcount==0:
                print('WRONG INPUT TRY AGAIN')
                continue
        elif y==2:
            mc=mydb.cursor()
            x=int(input('Enter worker ID whose records you wish to view= '))
            query='select W_ID,CONTACTNO from workers where W_ID={}'.format(x)
            mc.execute(query)
            for i in mc:
                print(i)
            if mc.rowcount==0:
                print('WRONG INPUT TRY AGAIN')
                continue
        elif y==3:
            mc=mydb.cursor()
            x=int(input('Enter worker ID whose records you wish to view= '))
            query='select W_ID,DEPARTMENT from worker where W_ID={}'.format(x)
            mc.execute(query)
            for i in mc:
                print(i)
            if mc.rowcount==0:
                print('WRONG INPUT TRY AGAIN')
                continue
        elif y==4:
            mc=mydb.cursor()
            x=int(input('Enter worker ID whose records you wish to view= '))
            query='select * from workers where W_ID={}'.format(x)
            mc.execute(query)
            for i in mc:
                print(i)
        elif y==5:
            mc=mydb.cursor()
            query='select * from workers'
            mc.execute(query)
            for i in mc:
                print(i)
        y=int(input('Enter 1 to continue OR 2 to Exit'))
        if y==1:
            continue
        elif y==2:
            break
        else:
            print("Wrong input")
      
def add_info():
    while True:
        mc=mydb.cursor()
        print('ENTER THE FOLLOWING DETAILS')
        SRNO = int(input('Enter serial no : '))
        SALARY = int(input('Enter salary : '))
        W_ID = int(input('Enter worker ID : '))
        mc.execute("INSERT INTO FINANCIAL_INFO VALUES({},{},{})".format(SRNO,SALARY,W_ID))
        mydb.commit()
        print('RECORDS ADDED SUCCESSFULLY!!')
        mydb.commit()
        x=int(input('Enter 1 to view the added records, 0 to exit or any other number to continue adding records=  '))
        if x==1:
            new='select * from financial_info where SRNO={}'.format(SRNO)
            mc.execute(new)
            for i in mc:
                print(i)
        y=int(input('Enter 0 to exit or any other number to continue adding records=  '))
        if y==0:
            break
def delete_info():
    while True:
        mc=mydb.cursor()
        print('Enter the worker id whose records you wish to delete')
        x=int(input('Enter W_ID = '))
        query='delete from financial_info where W_ID={}'.format(x)
        mc.execute(query)
        mydb.commit()
        
        if mc.rowcount>0:
            print('RECORDS DELETED SUCCESSFULLY!!')
        else:
            print('RECORD NOT FOUND TRY AGAIN!!')
        y=int(input('Enter 1 to continue OR 2 to Exit'))
        if y==1:
            continue
        elif y==2:
            break
        else:
            print("Wrong input")

def update_info():
    while True:
        mc=mydb.cursor()
        y=input('Enter the Worker ID whose records you wish to update: ')
        print('Which colomn do you wish to edit:\n1-SRNO\n2-SALARY')
        x=int(input('ENTER CHOICE : '))
        if x==1:
            Sr_NEW=int(input('Enter new serial no : '))
            query='update financial_info set SRNO ={} where W_ID={}'.format(Sr_NEW,y)
            mc.execute(query)
            mydb.commit()
            print('RECORD UPDATED SUCCESSFULLY!!!')
        elif x==2:
            SAL_NEW=int(input('ENTER NEW SALARY= '))
            query='update financial_info set SALARY={} where W_ID={}'.format(SAL_NEW,y)
            mc.execute(query)
            mydb.commit()
            print('RECORD UPDATED SUCCESSFULLY!!')
        else:
            print('WRONG INPUT TRY AGAIN!!')
        y=int(input('Enter 1 to continue OR 2 to Exit : '))
        if y==1:
            continue
        elif y==2:
            break
        else:
            print("Wrong input")

def display_info():
    while True:
        mc=mydb.cursor
        print('Choose what records you wish to view\n1-SRNO\n2-SALARY\n3-EVERY RECORD EXISTING')
        y=int(input('Enter choice = '))
        if y==1:
            mc=mydb.cursor()
            x=int(input('Enter worker ID whose records you wish to view = '))
            query='select SRNO,W_ID from financial_info where W_ID={}'.format(x)
            mc.execute(query)
            for i in mc:
                print(i)
            if mc.rowcount==0:
                print('WRONG INPUT TRY AGAIN')
                continue
        elif y==2:
            mc=mydb.cursor()
            x=int(input('Enter worker ID whose records you wish to view = '))
            query='select W_ID,SALARY from financial_info where W_ID={}'.format(x)
            mc.execute(query)
            for i in mc:
                print(i)
            if mc.rowcount==0:
                print('WRONG INPUT TRY AGAIN')
                continue
        elif y==3:
            mc=mydb.cursor
            mc.execute("SELECT * FROM financial_info")
            for i in mc:
                print(i)
            if mc.rowcount==0:
                print('WRONG INPUT TRY AGAIN')
                continue
        else:
              print("WRONG INPUT")
        a=int(input('Enter 1 to continue OR 2 to Exit :'))
        if a==1:
            continue
        elif a==2:
            break
        else:
            print("Wrong input") 
def ORE_MENU():
    print('***********************METALLURGY INDUSTRY***********************')
    print('-----------------------------WELCOME-----------------------------')
    while True:
        print('WHICH FUNCTION DO YOU WISH TO PERFORM\n1-ADD RECORDS\n2-DELETE RECORDS\n3-UPDATE RECORDS\n4-DISPLAY RECORDS\n5-EXIT TO MAIN MENU')
        x=int(input('ENTER CHOICE = '))
        if x==1:
            add_ore()
        elif x==2:
            delete_ore()
        elif x==3:
            update_ore()
        elif x==4:
            display_ore()
        elif x==5:
            MAIN_MENU()
        else :
            print('-----WRONG INPUT----')
        y=int(input('ENTER 1 to continue  OR 0 TO GO TO MAIN MENU : '))
        if y==1:
            continue
        elif y==0:
            MAIN_MENU()
        else :
            print("-----WRONG INPUT----")

def WORKERS_MENU():
    print('***********************METALLURGY INDUSTRY***********************')
    print('-----------------------------WELCOME-----------------------------')
    while True:
        print('WHICH FUNCTION DO YOU WISH TO PERFORM\n1-ADD RECORDS\n2-DELETE RECORDS\n3-UPDATE RECORDS\n4-DISPLAY RECORDS\n5-EXIT TO MAIN MENU')
        x=int(input('ENTER CHOICE =  '))
        if x==1:
            add_worker()
        elif x==2:
            delete_worker()
        elif x==3:
            update_worker()
        elif x==4:
            display_workers()
        elif x==5:
            MAIN_MENU()
        else :
            print('-----WRONG INPUT----')
        y=int(input('ENTER 1 to continue  OR 0 TO GO TO MAIN MENU : '))
        if y==1:
            continue
        elif y==0:
            MAIN_MENU()
        else :
            print("-----WRONG INPUT----")
def FINANCIAL_MENU():
    print('***********************METALLURGY INDUSTRY***********************')
    print('-----------------------------WELCOME-----------------------------')
    
   
    while True:
        print('WHICH FUNCTION DO YOU WISH TO PERFORM\n>>1-ADD RECORDS\n>>2-DELETE RECORDS\n>>3-UPDATE RECORDS\n>>4-DISPLAY RECORDS\n>>5-EXIT TO MAIN MENU')
        x=int(input('ENTER CHOICE = '))
        if x==1:
            add_info()
        elif x==2:
            delete_info()
        elif x==3:
            update_info()
        elif x==4:
            display_info()
        elif x==5:
            MAIN_MENU()
        else:
            print("-----WRONG INPUT----")
        y=int(input('ENTER 1 to continue  OR 0 TO GO TO MAIN MENU : '))
        if y==1:
            continue
        elif y==0:
            MAIN_MENU()
        else :
            print("-----WRONG INPUT----")

def MAIN_MENU():
    print('***********************METALLURGY INDUSTRY***********************')
    print('-----------------------------WELCOME-----------------------------')
    while True:
        print('*****1-ORE\n*****2-WORKERS\n*****3-FINANCIAL INFORMATION\n*****4-EXIT')
        x=int(input('\n\nEnter the table you wish to proceed with = '))
        if x==1:
            ORE_MENU()
        elif x==2:
            WORKERS_MENU()
        elif x==3:
            FINANCIAL_MENU()
        elif x==4:
            break
        else:
            print('xx--------------------------------------------WRONG INPUT-------------------------------xx')
    
MAIN_MENU()
       
