import random
print("welcome to the number guessing game")
print("You have atmost 3 chances to guess correct.")
print("Think of number from 1 to 10 ")

while True:
    guess=random.randint(1,10)
    chance=0
    while chance<3:
        user_guess=int(input("Enter your guess (1-10): "))
        if user_guess>10 or user_guess<1:
            print("guess is in invalid range!!")
            print(f"You took {chance} chances.")
            chance += 1

            continue
        if user_guess==guess:
            print(f"correct its {guess}")
            break
        elif user_guess<guess:
            print("your guess is less than the actual guess.")
        elif user_guess>guess:
            print("your guess is more than the actual guess")
        chance+=1
    if chance==3:
        print("Finished all 3 chances..")
        print(f"The correct guess was: {guess}")
    play_again=input("""
                 Wanna play again?
                 if Yes,then enter 'Y' 
                 Else press any key to exit.:  """).strip().upper()
    if play_again!="Y":
        break
    else:
        continue
        
