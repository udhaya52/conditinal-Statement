x=int(input("enter the x value: "))
y=int(input("enter the y value: "))
if x>0 and y>0:
    print(f"{x} and {y} values are present in the first quadrant")
elif x<0 and y>0:
    print(f"{x} and {y} values are present in the second quadrant")
elif x<0 and y<0:
    print(f"{x} and {y} values are present in the third quadrant")
elif x>0 and y<0:
    print(f"{x} and {y} values are present in the fourth quadrant")
elif x==0 and y==0:
    print(f"{x} and {y} values are present in the orgin")
elif x==0 and y!=0:
    print(f"{y} point in y axis")
else:
    print("point in x axis")



