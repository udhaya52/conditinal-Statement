import keyword
w=keyword.kwlist
word=input("enter the word")
if word in w:
    print("It is a keyword")
else:
    print("It is a not keyword")
