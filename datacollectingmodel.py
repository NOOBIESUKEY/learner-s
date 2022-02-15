#python file
#small model how user data is collected




while(True):
    import datetime
    x = "Time and Date = "+ str(datetime.datetime.now())
    newline = "\n"
    space = ", "

    name = input("\n\nEnter your name = ")
    Name = "Name = " + name
    print("so" ,name)


    print("what would you prefer to do?(Press 1 to select Exercise and 2 for Diet)")
    whhat = int(input())

    if whhat == 1:
        print("you selected exercise...")
        what = "Selection = exercise"
        print("")
        print("you have these options: (Press corresponding number to select an exercise...)\n"
              " 1. Squats\n"
              " 2. Lunges\n"
              " 3. Push-ups\n"
              " 4. Abdominal Crunches\n"
              " 5. Bent-over Row.\n")
        choise = {"1": "Squats",
                  "2": "Lunges",
                  "3": "Push-ups",
                  "4": "Abdominal Crunches",
                  "5": "Bent-over Row"}
        selection = choise[input("Select = ")]
        print("you selected " + selection)
        subselection = "sub-selection = " + selection

    elif whhat == 2:
        print("you selected diet..." )
        what = "Selection = diet"
        print("")
        print("you have these options: (Press corresponding number to select an exercise...)\n"
              " 1. Salmon\n"
              " 2. Milk\n"
              " 3. Seaweed\n"
              " 4. Egg yolk\n"
              " 5. Soy\n")
        choise = {"1": "Salmon",
                  "2": "Milk",
                  "3": "Seaweed",
                  "4": "Egg yolk",
                  "5": "Soy"}
        selection = choise[input("Select = ")]
        print("you selected " + selection)
        subselection = "sub-selection = " + selection


    info = Name + space + what + space + subselection + space + x + newline
    # print(type(info))
    print("**Data Collected**")

    with open("database.txt", "a") as f:
         f.write(info)
         # print(f)
    
