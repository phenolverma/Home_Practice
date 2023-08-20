num = [1,2,3,4,5,5]
uniq = []
for number in num:
    if number not in uniq:
        uniq.append(number)
print("After duplicate removel the list is = ", uniq)
