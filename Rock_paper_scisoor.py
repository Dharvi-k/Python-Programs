import random
list=[1,2,3]
round=0
comp_score=0
user_score=0
print("""Welcome to the Game.
        You will get 3 chances..
        press "Q" to quit.""")
print("""Click :-
        1:Rock
        2:Paper
        3:Scissor""")
while round<3:
    comp_guess=random.choice(list)
    user_guess=input("Enter your choice: ").upper()

    if user_guess=="Q":
        exit()
    elif user_guess not in ["1","2","3"]:
        print("Invalid input !!")
        continue
    else:
        user_guess=int(user_guess)
        if comp_guess==user_guess:
            print("""
                You=Rock
                computer=Rock
                It's a tie!
                    """)
        elif comp_guess==1 and user_guess==2:
            user_score+=1
            print(""" 
                    You:Paper
                    Computer:Rock""")
            print(f"Your score:{ user_score}")
            print(f"Computer score:{ comp_score}")
        elif comp_guess==1 and user_guess==3:
            comp_score+=1
            print(""" 
                    You:Scissor
                    Computer:Paper""")
            print(f"Your score:{ user_score}")
            print(f"Computer score:{ comp_score}")
        elif comp_guess==2 and user_guess==1:
            comp_score+=1
            print(""" 
                    You:Rock
                    Computer:Paper""")
            print(f"Your score:{ user_score}")
            print(f"Computer score:{ comp_score}")
        
        elif comp_guess==2 and user_guess==3:
            user_score+=1
            print(""" 
                    You:Scissor
                    Computer:Paper""")
            print(f"Your score:{ user_score}")
            print(f"Computer score:{ comp_score}")
        elif comp_guess==3 and user_guess==1:
            user_score+=1
            print(""" 
                    You:Rock
                    Computer:Scissor""")
            print(f"Your score:{ user_score}")
            print(f"Computer score:{ comp_score}")
        elif comp_guess==3 and user_guess==2:
            comp_score+=1
            print(""" 
                    You:Paper
                    Computer:Scissor""")
            print(f"Your score:{ user_score}")
            print(f"Computer score:{ comp_score}")
        
        round+=1
    
print("*******FINAL SCORE*******")       
print(f"Your score:{user_score}")
print(f"Computer score:{comp_score}")
if user_score==comp_score:
    print("It's a tie")
elif user_score<comp_score:
    print("Computer win!!")
else:
    print("You win!!!")

