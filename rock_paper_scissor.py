import random

emojis = {'r': '🪨', 's': '✂️', 'p': '📄'}
choices = ('r', 'p', 's')

def play_game():
    
    while True:
        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()

        if user_choice not in choices:
            print('Invalid choice! Please choose "r", "p", or "s".')
            
            continue

        computer_choice = random.choice(choices)

        print(f'You chose {emojis[user_choice]}')
        print(f'Computer chose {emojis[computer_choice]}')

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'r' and computer_choice == 's') or \
             (user_choice == 'p' and computer_choice == 'r') or \
             (user_choice == 's' and computer_choice == 'p'):
            print("You win!")
        else:
            print("Computer wins!")

play_game()