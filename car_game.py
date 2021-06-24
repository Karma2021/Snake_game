# car game

command = ""
started = False
while "quit" != command:
    command = input("Enter any word:  ")
    if command == "start":
        if not started:
            started = True
            print("Car started..")
        else:
            print("Car already started !")
    elif command == "stop":
        if not started:
            print("Car already stopped..")
        else:
            started = False
            print("Car stopped..")
    elif command == "help":
        print("""
                  ***
                  
         start = to start the car
         stop = to stop the car
         quit = quit
         
                  ***
         """)
    elif command == "quit":
        print('program finished')
        break
    else:
        print("error! invalid input")
