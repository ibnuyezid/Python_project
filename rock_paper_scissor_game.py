import random
user_input=''
user_wins=0
computer_wins=0
option=['rock','scissor','paper']
while user_input!='q':
        user_input=input("Type rock/paper or scissor and 'Q' to quit ").lower()
         
        if user_input not in option:
            continue
        random_number=random.randint(0,2)
        computer_pick=option[random_number]
        print("computer choose", computer_pick+".")
        if user_input == 'rock' and computer_pick=='scissor':
            print("You won ")
            user_wins+=1
        elif user_input == 'scissor' and computer_pick=='paper':
            print("You won ")
            user_wins+=1
        elif user_input == 'paper' and computer_pick=='rock':
            print("You won ")
            user_wins+=1
        else:
            print("You lost")
            computer_wins+=1
print("you won",user_wins,"times.")
print("you lost",computer_wins,"times.")
print("GoodBuy")




