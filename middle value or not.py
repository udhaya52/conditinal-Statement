l = eval(input("enter your list: "))
if len(l) % 2 == 1:
    mid_value = l[len(l) // 2]
    if type(mid_value) == str:
        print(mid_value,'is a string')
    else:
        print(mid_value, 'is not string')
else:
    print("middle value not present")

