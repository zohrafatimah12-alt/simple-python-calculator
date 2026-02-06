students=int(input("Enter the number of students:"))
for s in range(students):
    print(f"\n Student {s+1}")
    name=input("Enter Name:")
    marks=[]
    subjects=int(input("Enter the no of subjects:"))
    for i in range(subjects):
        mark=int(input(f"Enter marks for subjects {i+1} :"))
        marks.append(mark)
    total=sum(marks)
    average=total/subjects
    if average>=90:
        grade="A"
    elif average>=80:
        grade="B"
    elif average>=70:
        grade="C"
    elif average>=60:
        grade="D"
    else:
        grade="F"
    print("\n---Result---")
    print("Name",name)
    print("Total:",total)
    print("Average",average)
    print("Grade:",grade)
    if average>=40:
        print("Status:Pass")
    else:
        print("Status:Fail")


    
    
