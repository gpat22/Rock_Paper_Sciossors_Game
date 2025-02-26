import random
playing = True
emojis = {
    'r':'🪨',
    'p':'📃',
    's':'✂️'
}
c = tuple(emojis.keys())
#compare input
def res(computer,player):
    if computer == player:
        return "Its a Tie"
    elif ((computer == 's' and player == 'p') or
          (computer == 'r' and player == 's') or
          (computer == 'p' and player == 'r')):
        return "Computer Wins"
    elif ((computer == 'r' and player == 'p') or
          (computer == 'p' and player == 's') or
          (computer == 's' and player == 'r')):
        return "Player Wins"

while playing:
    # computer will choose random option between r/p/s
    computer_choice = random.choice(c)
    choice = input("Rock, Paper or Scissors ? (r/p/s) ").lower()
    if choice not in c:
        print("Invalid Input")
        continue
    result = res(computer_choice,choice)
    print(f"Player selected {emojis[choice]} \nand Computer Selected {emojis[computer_choice]} \n{result}")
    play = input("Want to continue playing (y/n) ").lower()
    if play == 'y':
        playing = True
    else:
        playing = False
else:
    print("Thank you for playing")