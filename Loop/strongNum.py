num=int(input("Enter the number"))
fact=1
sum=0
a=num
while a>0 :
    digit = a%10
    fact=fact*digit
    sum=sum+fact
    a=a//10
if sum==num:
    print(num,"Is a Strong Number")
else:
    print(num,"Is a Not Strong Number")
