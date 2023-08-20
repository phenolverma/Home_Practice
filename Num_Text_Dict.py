Phone = input("Enter the number = ")
dict = {'1':'One','2':'Two','3':'Three','4':'Four'}
to_text = ""
for num in Phone:
    to_text = to_text + " " + dict.get(num)
print(to_text)
