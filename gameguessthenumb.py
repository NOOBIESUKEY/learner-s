# first silly game by me..
# guess  the number game...(edit value of jam variable to change winning number)


jam = 354
print("\nWelcome to game : Guess the Number: ")  
n = float(input("Guess the number = "))
t = 1
while(True):
    if n>jam :
        t = t+1
        print(" Winning number is less than entered number.\n ")
        n = float(input("Guess again = "))  
    elif n < jam:
        t = t+1
        print(" Winning number is greater than entered number.\n" )
        n = float(input("Guess again = "))
    else:
        print("You won.👌😍❤👌")
        break

print("\nYou gussed the number in " , t , "times.")
        
