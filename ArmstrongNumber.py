num = int(input("Enter the number"))
sum=0
temp = num
while temp > 0 :
    digit = temp %10
    sum =sum+(digit ** len(str(num)))
    temp = temp // 10
# print(sum)
if num == sum :
    print(num,"It is Armstrong")
else:
    print(num,"It is Not Armstrong")