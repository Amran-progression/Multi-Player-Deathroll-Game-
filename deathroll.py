import random

player1 = input("What is your name, player 1?: ")
player2 = input("What is your name, player 2?: ")
roll_first = (random.randint(1, 2))


def roll():
    if roll_first == 1:
        try:
            number = int(input(f"What would you like to play to, {player1.title()}? "))
            print(f"{player1.title()} chose to play to: {number}\n")
        except ValueError:
            print("Invalid input. Please only put numbers!\n")
            roll()
    else:
        try:
            number = int(input(f"What would you like to play to, {player2.title()}? "))
            print(f"{player2.title()} chose to play to: {number}\n")
        except ValueError:
            print("Invalid input. Please only put numbers!\n")
            roll()


    p1 = int(number)
    p2 = int(number)

    while p1 and p2 and number > 1:
            p1input = input(f"{player1.title()}, please type 'roll': ")
            if p1input == "roll":
                p1 = random.randint(1, p2)
                print(f"{player1.title()} rolled a: {p1}\n")
            else:
                print("only type 'roll', please... try again.")
                p1inputlastchance = input(f"{player1.title()}, please type 'roll' - this is your last chance: \n")
                if p1inputlastchance == "roll":
                    p1 = random.randint(1, p2)
                    print(f"{player1.title()} rolled a: {p1}\n")


            if p1 == 1:
                print(f"\nthe game is over, {player2.title()} won!")
                break

            p2input = input(f"{player2.title()}, please type 'roll': ")
            if p2input == "roll":
                p2 = random.randint(1, p1)
                print(f"{player2.title()} rolled a: {p2}\n")
            else:
                print("Only type 'roll', please... try again.")
                input(f"\n{player2.title()}, please type 'roll': ")

            if p1 == 1:
                print(f"The game is over, {player2.title()} won!")
                break
            elif p2 == 1:
                print(f"The gamer is over, {player1.title()} won!")
                break

roll()

