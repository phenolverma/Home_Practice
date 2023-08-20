weight = float(input("Enter the weight = "))
kg_lbs = input("Weight in KG(K/k) or LBS(L/l) = ")
if kg_lbs.upper() == 'K':
    print("Weight in LBS = ", weight * 0.45)
else:
    print("Weight in KG = ", weight / 0.45)