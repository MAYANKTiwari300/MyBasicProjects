import random
def game_win(computer,user):
    
    if computer == user:
        return None
    elif computer == "s":
        if user == "w":
            return False
        elif user == "g":
            return True
        # else:
        #     return "Invalid input! Please choose either 's', 'w', or 'g'."
    elif computer == "w":
        if user == "s":
            return True
        elif user == "g":
            return False
        # else:
        #     return "Invalid input! Please choose either 's', 'w', or 'g'."
    elif computer == "g":
        if user == "s":
            return False
        elif user == "w":
            return True
        # else:
        #     return "Invalid input! Please choose either 's', 'w', or 'g'."
    # else:
    #     return "Invalid input! Please choose either 's', 'w', or 'g'."




# if user not in ["s","w","g"]:
#         return "Invalid input! Please choose either 's', 'w', or 'g'."
#     elif computer == user:
#         return None
#     elif computer == "s":
#         if user == "w":
#             return False
#         elif user == "g":
#             return True
       
#     elif computer == "w":
#         if user == "s":
#             return True
#         elif user == "g":
#             return False
        
#     elif computer == "g":
#         if user == "s":
#             return False
#         elif user == "w":
#             return True    
    
random_num = random.randint(1,3)
print("For computer turn: Snake(s), Water(w) and Gun(g)")
if random_num == 1:
    computer = "s"
elif random_num == 2:
    computer = "w"
else:
    computer = "g" 

user = input("For user turn: Snake(s),water(w) and Gun(g): ").lower()
print(f"\ncomputer choose {computer}")
print(f"\nuser choose {user}")
result = game_win(computer,user)

if result is None:
    print("The game is a tie")
elif result:
    print("You win and computer loses")
else:
    print("You Lose and computer wins")    
