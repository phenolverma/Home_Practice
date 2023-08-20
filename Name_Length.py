name = input("Please enter name = ")
if len(name) < 3:
    print("Name should have min 3 character")
elif len(name) > 50:
    print("Name should have max 50 character")
else:
    print("Name looks good")