name = input("Enter the name")
i=0
s=0
while i < len(name):
    if "a" in name[i] :
        s+=1
    i+=1
if s>1:
    print("Enter in the room", s)
else:
    print("Don't Enter in the room", s)