u=["xyz","yzx","zxy","rrr"]
p=["123","231","321","111"]
x=input("enter a user name:")
y=input("enter a password:")
if x in u:
    i=u.index(x)
    if p[i]==y:
        print("successfull login")
    else:
        print("invalid password")
else:
    print("invalid user name")
