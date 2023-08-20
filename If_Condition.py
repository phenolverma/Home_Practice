weight = float(input("Enter the weight "))
convert = input("Weight in Kg(K/k) or LBS(L/l) ")
if convert == 'K' or convert == 'k':
    print("Weight in KG = ", weight)
else:
    print("Weight in LBS = ", weight*1.44)