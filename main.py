def deposit():
    while True:#we are asking from the user until they give us a valid input

        amount = input("how much would you like to deposit?")#by deault input is taken as a string
    
        if amount.isdigit(): #valid whole number not negative 0-infinity
            amount =int(amount)
            if amount>0:
                break #while will run untill this break is reached
            else:
                print("amount must be grater than 0")
        else:
            print("please enter a valid number")
        return amount