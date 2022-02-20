# python 
# snake-warer-gun game 

import random

print("\nWelcome to GSW(Gun-Snake-Water)game...")
user_name = input("\nEnter your name : ")

how_many = int(input("\nHow many times you want to replay this game?\n"))

it = int(0)

opt = ["s", "g", "w"]

user_point = 0

com_point = 0

while it != how_many:
    it += 1
    com_in = random.choice(opt)
    print("\nPress S for snake, G for gun and W for water : ")
    user_in = input()
    print("Computer selected " + com_in + ".")

    # if int(it) == int(how_many):
    #     result = user_name + " got " + str(user_point) + "points."
    #     print(result)
    #     break

    if user_in == "s" or user_in == "S":
        if com_in == "s":
            print("match tied")
        elif com_in == "w":
            print("You won")
            user_point += 1
        elif com_in == "g":
            print("you loose.")
            com_point += 1

    elif user_in == "w" or user_in == "W":
        if com_in == "w":
            print("match tied")
        elif com_in == "g":
            print("You won")
            user_point += 1
        elif com_in == "s":
            print("you loose.")
            com_point += 1

    elif user_in == "g" or user_in == "G":
        if com_in == "g":
            print("match tied")
        elif com_in == "s":
            print("You won")
            user_point += 1
        elif com_in == "w":
            print("you loose.")
            com_point += 1


result = "\n" + user_name + " got " + str(user_point) + " points and bot got " + str(com_point) + " points.\n"
print(result)

if user_point >= com_point:
    print("You won...")
else:
    print("You loose...")




