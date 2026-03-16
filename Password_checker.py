password=input("enter password")
length=len(password)
print("password  length:",length)
if length<6:
    print("password strength:weak")
elif  length<10:
    print("password strength:medium")
else:
    print("password strength:strong")