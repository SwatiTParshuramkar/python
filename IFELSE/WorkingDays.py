working_days = int(input("Enter the Working days - "))
Absent_days = int(input("Enter the Absent day - "))
Total_days = int(input("Enter the Total day -"))
perc = (working_days-Absent_days)/Total_days*100
if perc <75 :
    print("Student Attendence is less than 75,Student not appear in exam")
else:
    print("Student Attendence is greater than 75,Student appear in exam")