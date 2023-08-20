car_command = ""
comm_start = ""
comm_end = ""

print("Lets begin")
while True:
    car_command = input("> ").upper()
    if car_command == comm_start:
        print("You have already started the car")
        comm_start = ""
    elif car_command == comm_end:
        print("You have already stopped the car")
        comm_end = ""
    elif car_command == 'HELP':
        print('''
        Start - To start the car
        Stop - To stop the card
        Quit - Exit
        ''')
    elif car_command == 'START':
        comm_start = 'START'
        print("Car is started")
    elif car_command == 'STOP':
        comm_end = 'STOP'
        print("Car is stopped")
    elif car_command == 'QUIT':
        print("See you next time")
        break
    else:
        print("Try Again")