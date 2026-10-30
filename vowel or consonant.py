ch=input("enter your alphabet: ")
if "A"<=ch<="Z" or "a"<=ch<="z":
    if ch in "aeiouAEIOU":
        print(f"{ch} is a vowel")
    else:
        print(f"{ch} is  a consonant")
else:
    print(f"{ch} is not a alphabet")