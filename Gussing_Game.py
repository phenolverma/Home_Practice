number = 7
i = 1
while i <= 3:
    guess = int(input("Guess the number = "))
    if guess == number:
        print("Good Guess, You won")
        break
    else:
        i +=1
        print("You are wrong")
else:
    print("You are failed")



