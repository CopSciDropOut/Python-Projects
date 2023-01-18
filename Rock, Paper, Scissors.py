import random

"""""
player = 0
computer = 0 
"""
for cycle in range(6):
    user = input("Please Choose either:Rock Paper Scissor: "  )
    computer = random.randint(1,3)

    if computer == 1:
        answer = "rock"
    elif computer == 2: 
        answer = "paper"
    elif computer == 3: 
        answer = "scissors"
    print(answer)
    
    if answer == user:
        print('Tie')
    if user == 'rock' > answer == 'scissors' or user == 'scissors' > answer == 'paper' or user == 'paper' > answer == 'rock' or user == 'rock' > answer == 'scissors' :
        print("You Won")
    else:
        print("computer won ")

        

        
        
        
        
