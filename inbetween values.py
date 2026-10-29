# print first and last value of list if length of list is even else print inbetween value using slicing

list=eval(input("enter the list"))

if(len(list)%2==0):
    print(list[0],list[-1])
else:
    print(list[1:len(list)-1:1])