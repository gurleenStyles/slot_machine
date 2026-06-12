#okay so first i creates a repo in my local machine and to add this on my github i have to  create a repo with no readme file (this is imp)then git init git git remote add origin <url> git add . git commit -m "first commit" git push -u origin main
MAX_LINES=3 #constant value that won't change in the program
def deposit():
    while True:#we are asking from the user until they give us a valid input

        amount = input("how much would you like to deposit?")#by deault input is taken as a string
    
        if amount.isdigit(): #valid whole number not negative 0-infinity
            amount =int(amount)
            if amount>0:
                break #while will run untill this break is reached
            else:
                print("amount must be grater than 0")#never executed because of the isdigit() check
        else:
            print("please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines= input("enter the number of lines to bet on(1-"+ str(MAX_LINES)+ ")? ")
        if lines.isdigit():
            lines =int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("enter a valid number of lines")
    return lines


def main():
  balance = deposit()
  lines =get_number_of_lines()
  print (balance,lines)

main()