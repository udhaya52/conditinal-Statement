#suppose we enter negative number its print only single digit becz of -89 is less than 10
# so we use absolute inbuilt function for negativ eto postive convert.
n=abs(int(input("enter a number: ")))
if n<10:
    print(n,"is single digit")
elif  n<100:
    print(n,"is double  digits")
elif n<1000:
    print(n,"is triple  digits")
else:
    print(n,"is multiple digit")