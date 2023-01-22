import random

print("Enter choice: 1: Rock, 2: Paper, 3: Scissor")
choice = input("Choice (1/2/3): ")
choice = int(choice)

computer_choice = random.randint(1,3)
print(f"Computer choice: {computer_choice}")

if choice == computer_choice:
    print("Draw")
elif choice ==1:
    if computer_choice==2:
        print("Computer wins")
    else:
        print("You win")
elif choice ==2:
    if computer_choice == 1:
        print("Computer win")
    else:
        print("You win")
elif choice ==3:
    if computer_choice == 1:
        print("Computer wins")
    else:
        print("You wins")
