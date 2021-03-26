#  Write a program in Python to identify the loop ND Describe the sequence of loop.

week = int(input("Enter the week"))
while (week <= 7) :
    day = input('Enter the morning/evening/afternoon').lower()
    if day == "morning" :
        print("It is Excercise")
        continue
    elif day == "afternoon":
        print("It is a time for cultural activity")
        continue
    elif day == "evening":
        print("It is time Study Time")
        continue
    else:
        print("Enter the correct day of time")
    week+=1
else:
    print("Try to make new scheduled") 