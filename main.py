import random
items = ["rock","paper","scissor"]

user_score = 0
computer_score = 0
for round in range(5):

    computer = random.choice(items)
    user = input("rock paper and scissor: ").lower()
    print("computer choose:",computer)

    if (user == computer):
      print("match")
    elif user == "rock" and computer == "scissor":
        print("user win")
        user_score += 1
    elif user == "paper" and computer == "rock":
        print("computer win")
        computer_score += 1
    elif user == "scissor" and computer == "paper":
        print("user win")
        user_score += 1
    else:
        print("computer win")
        computer_score += 1

    print("final score")
    print("user score",user_score)
    print("coumputer score",computer_score)
    if user_score > computer_score:
       print("user win")
    elif(user_score < computer_score):
      print("computer win")
    else:
     print("equal")