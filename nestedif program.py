user_name='udhayakumar22@gmail.com'
password='udhaya@2005'
uname=input("enter your username: ")
if uname==user_name:
    up=input("enter your password: ")
    if up==password:
        print("you are logged in")
    else:
        print("invalid password")
else:
    print("invalid username")