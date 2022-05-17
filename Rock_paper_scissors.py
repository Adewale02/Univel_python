'''import random

print("Beat the computer in a game of Rock, Paper and Scissors.")
R = 0
P = 1
S =2
trial = 3
score = 0

items =["R","P", "S"]
random.shuffle(items)
com_choice = random.choice(items)
print (com_choice)

user = (input("Choose R, P or S:")).upper()
print(user)
while trial > 0:

    if user == "R" and com_choice == "P":
        print("You lose")
        trial -=1
    elif user == "P" and com_choice == "S":
        print("You lose")
        trial -=1
    elif user == "S" and com_choice == "R":
        print("You lose")
        trial -=1
        
            
    elif user== "S" and com_choice == "P":
        print("You win")
        trial +=1
        score +=2
    elif user == "P" and com_choice == "R":
        print("You win")
        trial +=1
        score +=2
    elif user == "R" and com_choice =="S":
        print("You win")
        trial +=1
        score +=2
else:
  print("It's a draw")
print(f'{trial}trials left')

print("Game over")
print("You scored", score)'''

a = [1,2,3,4,5]

b= [6,7,8,9,10]

b[3]= 82

print(b)
for element in a:
    print(element)

'''print(a[2:5])

h = [x**2 for x in range(10)]

print(h)'''

'''p =[1,2,4,7,8,9,10]
m = sum(p)/7

c =[(x-m)**2 for x in p]
print(c)
d= sum(c)

sd = (d/7)**0.5
print(sd)'''

t = [x if x%2 ==0 else 0 for x in range(10)]

print(t)

print(8//2)


