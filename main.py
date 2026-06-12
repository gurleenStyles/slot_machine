#okay so first i creates a repo in my local machine and to add this on my github i have to  create a repo with no readme file (this is imp)then git init git git remote add origin <url> git add . git commit -m "first commit" git push -u origin main
import random 


MAX_LINES=3 
MAX_BET= 100#capttal make it's constant 
MIN_BET =1 #constant value that won't change in the program

ROWS =3
COLS =3

symbol_count={ #dictionary to store the count of each symbol in the slot machine
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8 #symbol.items(), it will give both the key and values from the dictionary 
}
symbol_value={ #dictionary to store the value of each symbol in the slot machine
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings=0
    winning_lines=[] #this will store the lines that we have won on
    for line in range(lines): #here line will start from index 0, if we are putting 2 lines it will check line 0 and 1
        symbol = columns[0][line] #this will get the symbol in the first column and the current line, we are checking the first column because if all the symbols in the line are the same then they will be the same as the first column
        

        for column in columns:
            symbol_to_check= column[line] #this will get the symbol in the current column and the current line
            if symbol != symbol_to_check:
                break #if the symbol in the current column and the current line is not the same as the symbol in the first column and the current line, then we will break out of the loop and move on to the next line
        else:
            winnings += values[symbol] * bet #if we didn't break out of the loop, it means that all the symbols in the line are the same, so we will add the winnings for that line to the total winnings, we will multiply the value of the symbol by the bet amount to get the winnings for that line
            winning_lines.append(line + 1) #add the line number to the list of winning lines
    return winnings, winning_lines


#immp partttt 

def get_slot_machine_spin(rows,cols, symbols):
    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):#it will add 2 a's, 4 b's, 6 c's and 8 d's to the all_symbols list
            all_symbols.append(symbol)

    columns =[[],[],[]] #this will represent values in each column 

    coulmns=[]
    for col in range(cols):
        column =[]
        current_symbols = all_symbols[:] #this will create a copy of the all_symbols list so that we can modify it without affecting the original list
        for _ in range(rows):
            value= random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        coulmns.append(column)
    return coulmns

#now we will transpose the columns to rows so that we can print the slot machine in a more readable format

def print_slot_machine(columns):
    for row in range(len(columns[0])): #we can write 3 here as we have a 3*3 matrix
        for i, column in enumerate (columns):#enumerate will give us both the index and the value of the column, so we can use the index to check if we are at the last column or not
            if i != len(columns)-1: #this will chek that if we reach the last element
                print(column[row], end=" | ") #this will print the value of the current column and row and end with a pipe symbol and a space, but it will not move to the next line
            else:
                print(column[row], end="")

        print()#this will move to the next line after printing all the columns for the current row


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

def get_bet():
    while True:
        amount = input("what would you like to bet on each line?")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("please enter a number")
    return amount

def spin(balance):
  lines =get_number_of_lines()
  while True:
    bet= get_bet() 
    total_bet = bet* lines
    if total_bet>balance:
        print(f"you don't have enough to bet that amount(${total_bet}), your current blance is: ${balance}")
    else:
        break
  print(f"you are betting to ${bet} on {lines}. total bet is equal to ${total_bet}")

  slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
  print_slot_machine(slots)
  winnings, winning_lines= check_winnings(slots, lines, bet, symbol_value)
  print (f"you won ${winnings}")
  print(f"you won on lines:", *winning_lines) #the * will unpack the list of winning lines and print them separated by a space
  balance += winnings - total_bet
  return balance

def main():
  balance = deposit()
  while True:
      print(f"current balance is ${balance}")
      answer=input ("press enter to play (q to quit)")
      if answer =="q":
          break
      balance = spin(balance)
    
  print (f"you are left with ${balance}")

main()