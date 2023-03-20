import csv
import os

cnics=[]
accounts=[]
accounts_cninc=[]
with open("Cnics.csv") as f:
    read=csv.reader(f)
    next(read)
    for row in read:
    #    print(row)
    #    print(row)
       try:
        cnics.append(row[0])
       except:
           pass
    f.close()
with open("Accounts.csv") as f:
    read=csv.reader(f)
    next(read)
    for row in read:
        try:
         accounts.append(row[0].strip())
         accounts_cninc.append(row[1].strip())
        except:
           pass
    f.close()
# print(cnics)
print(accounts_cninc)
# print(accounts)
# os.remove('Cnics.csv')
# os.remove('Accounts.csv')
cnic_own=input("Enter your cnic number")



if cnic_own.strip() in cnics:
    print("Thanks for confirming that you are a local resident")

    account_own=input("Enter your account number (if have or write no)")
    find_index=[]
    for index,i in enumerate(accounts):
        if i.strip() ==account_own.strip():
            find_index.append(index)
            print(index)

    if account_own in accounts and accounts_cninc[find_index[0]]==cnic_own.strip():
        print("Thanks for confirming your account")
        age=int(input("Enter your age:- "))
        if age <60 :
            company=input("From which sector you belongs to goverment  or private ? (press g for goverment and p for private)")
            if (company=='g'):
                salary=int(input("Enter your salary = "))
                print(salary<100000)
                if salary <50000:
                    print("1 lacs loan can be granted")
                if salary <= 100000 and salary > 50000:
                     print("3 lacs loan can be granted")
                elif salary > 100000:
                    print("5 lacs loan can be granted")
            elif company=='p':
                print("We need to first authorize for your company")
        elif age >60 :
            print("Sorry we didnt offer loans to retired persons") 

    # elif not(account_own in accounts and accounts_cninc[find_index[0]==cnic_own.strip()]):
    #     print("Incorrect input ,please enter again or register")
    else:
        registration=input("Do you want to regiter ? (press y for yes or n for no)")
        if registration=='y':
           registration_account_name=input("Enter your name :- ")
           registration_account_cnic=input("Enter your cnic :- ")
           new_account='a'+registration_account_cnic[-3:]
           accounts.append(new_account)
           print("Congratulations!,Account registraction is complted")
           age=int(input("Enter your age:- "))
           if age <60 :
                company=input("From which sector you belongs to goverment  or private ? (press g for goverment and p for private)")
                if (company=='g'):
                    salary=int(input("Enter your salary = "))
                    # print(salary<= 100000)


                    if salary <= 50000:
                        print("2 lacs loan can be granted")
                    elif salary <= 100000 and salary >= 50000:
                        print("5 lacs loan can be granted")
                    elif salary > 100000:
                        print("5 lacs loan can be granted")
                elif company=='p':
                    print("We need to first authorize for your company")
           elif age >60 :
                print("Sorry we didnt offer loans to retired persons")
        elif registration=='n':
            print("Sorry we didnt deal with the person not holding our institution account ")
    
else:
    print("Sorry we only deal we local resident")


with open("Cnics.csv",'w') as f:
    writer = csv.writer(f)
    writer.writerow(['CNICs'])
    for row in cnics:
       a=[row]
       writer.writerow(a)
    f.close()
with open("Accounts.csv",'w') as f:
   writer = csv.writer(f)
   writer.writerow(['Account No','Cnic'])
   for index,row in enumerate(accounts):
       a=[row]
       writer.writerow([a,accounts_cninc[index]])
   f.close()
