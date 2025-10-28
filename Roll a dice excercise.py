# Dice Excercise
import random
print("Welcome to the dice game")
while True:
    Choice=input("press Enter to roll  a dice  or press q to quit.")
    Choice=Choice.strip()
    if Choice=='q':
        print('thanks will quit the game')
        break
    elif Choice =='':
        number=random.randint(1,6)
        print(f"Your number is {number}")
    else:
        print("Invalid Number")
print('The end')