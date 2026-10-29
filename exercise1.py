n=int(input("enter a number"))
if n%3==0 and n%5==0:
    print("dingadingi")
elif n%5==0:
    print("dingi")
elif n%3==0:
    print("dinga")
else:
    print("given number is not divisible by 3 or 5")