s_1 = int(input("Enter the First side"))
s_2 = int(input("Enter the Second side"))
s_3 = int(input("Enter the Third side"))
if s_1 == s_2 == s_3 :
    print("The equivalnt Triangle")
if ( s_1 == s_2 and s_1 !=s_3) or (s_2 == s_1 and s_2 != s_3) or (s_3 == s_1 and s_3 != s_2) :
    print("The Isoscalence Triangle")
