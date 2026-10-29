# wap to print if char is upper convert to lower
#  if char is lower convert into upper
# if char is digits add  10
# if char is special print ascii value of that char

ch=input("enter character: ")
if 65<=ord(ch)<=90:
    upper= ord(ch) + 32
    print(f"{chr(upper)}  convert into upper into lower")
elif 97<=ord(ch)<=122:
    lower= ord(ch) - 32
    print(f"{chr(lower)}  convert into lower into upper")
elif 48<=ord(ch)<=57:
    digit=int(ch)+10
    print(f"{digit}  add the 10 ")
else:
    print(f"{ord(ch)}  convert into char to ascii value")
''' ord use for convert letter to number and chr use to number to char'''
