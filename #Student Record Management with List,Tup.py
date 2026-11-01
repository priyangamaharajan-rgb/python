#Student Record Management with List,Tuple,Dictionary and csv
import csv
students=[{"RollNo":"101","Name":"Anitha","Department":"CSE","Marks":86},
          {"RollNo":"102","Name":"Bala","Department":"CSE","Marks":91},
          {"RollNo":"103","Name":"Chitra","Department":"ECE","Marks":78}]
#Tuple example:fixed course details
course=("Python",4)
print("Course Tuple:",course)
#Write text file
with open("Students.txt","w")as file:
    for student in students:
        file.write(str(student)+"\n")
#Write csv file
with open("Students.csv","w",newline="")as file:
    fields=["RollNo","Name","Department","Marks"]
    writer=csv.DictWriter(file,fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)
#Read csv file
print("\n--Records from csv--")
with open("Students.csv","r")as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row["RollNo"],row["Name"],row["Department"],row["Marks"])
