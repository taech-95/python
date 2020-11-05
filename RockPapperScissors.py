import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock,paper,scissors]
userChoise = int(input("Please select 0 for Rock, 1 for Paper, 2 for scissors\n"))
print("You chose")
print(images[userChoise])
imagesLength=len(images)-1
computerChoise = random.randint(0,imagesLength)
print("Computer chose")
print(images[computerChoise])

if userChoise==computerChoise:
    print("Nobody win")
elif userChoise==1 and computerChoise==0:
    print("You win")
elif userChoise==2 and computerChoise==1:
    print("You win")
elif userChoise==0 and computerChoise==2:
     print("You win")
else:
    print("You lose")