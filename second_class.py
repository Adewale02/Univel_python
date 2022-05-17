import random

print("Guess the computer's choice to win a prize")
a = [1,2,3,4,5,6,7]
print("Select a number from", a)
random.shuffle(a)
trial = 3
score = 0

while trial > 0:
    print("\n Select a number from",a)
    com_choice = random.choice(a)
    user = int(input("Your choice\n:>"))
    if user == com_choice:
        print("You win")
        score+=2
        trial+=1
        print(f"You have won an extra trial")
        print(f"{trial} trial(s) left")
    else:
        if user> com_choice:
            print("Too high")
        else:
            print("Too low")
        trial -=1
        print(f"{trial} trial(s) left")
print(f"\n You scored {score} points")
print("Game over ):")

        
