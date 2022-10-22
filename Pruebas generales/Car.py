import math
command = ""
started = False
while True:
    command = input("> ")
    if command.lower() == "start":
        if started:
            print("The car is already in motion")
        else:
            print("The car has started brrrrr")
            started = True
    elif (command.lower() == "stop"):
        if started:
            print("The car has stopped brrn't")
            started = False
        else:
            print("The car is not in motion yet")
    elif (command.lower() == "help"):
        print('''Start: Starts the car
Stop: Stops the car
Quit: Quits the game
        ''')
    elif (command.lower() == "quit"):
        break
    else:
        print("Sorry, I don't know that command")
print("End of program")
