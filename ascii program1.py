# wap to check wheather the char is upper or lower or digit or special char  28/10/2026
ch=input("enter the value: ")
if 65<=ord(ch)<=90:
    print("Given character is uppercase")
elif 97<=ord(ch)<=122:
    print("Given character is lowercase")
elif 48<=ord(ch)<=57:
    print("Given character is digits")
else:
    print("Given character is special character")
