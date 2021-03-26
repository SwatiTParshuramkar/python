num1 = int(input("Enter the  1st number"))
num2 = int(input("Enter the 2nd number"))
while (num1%num2) != 0 :
    rem=num1 % num2
    num1=num2
    num2=rem
print("HCF is", num2)
