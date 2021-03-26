num =int(input("Enter The number"))
s=0
i=1
while i < num:
    if num%i == 0 :
        s=s+i
    i=i+1
if s == num :
    print(num,"perfect Number")
else:
    print(num, "not a Perfect number")