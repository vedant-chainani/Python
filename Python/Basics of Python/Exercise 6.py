import random
#1:Rock
#2:Paper
#3:Scissor
lst = ['Rock','Paper','Scissor']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print("Rock Paper Scissor Game\n")
print("1.Rock\n2.Paper\n3.Scissor")

# making the game in while loop
while no_of_chance < chance:
    _input = str(input('Rock,Paper,Scissor:'))
    _random = random.choice(lst)

    if _input == _random:
        print("Tie Both 0 point to each \n ")

    # if user enter 1
    if _input == "Rock" and _random == "Paper":
        computer_point = computer_point + 1
        print(f"Your Input is {_input} and Computer Input is {_random}")
        print("Computer wins 1 point")
        print(f"Computer has {computer_point} Point(s) and You have {human_point} Points")

    elif _input == "Rock" and _random == "Scissor":
        human_point = human_point + 1
        print(f"Your Input is {_input} and Computer Input is {_random}")
        print("You Win 1 point")
        print(f"Computer has {computer_point} Point(s) and You have {human_point} Points ")

    # if user enter 2
    if  _input == "Paper" and _random == "Scissor":
        computer_point = computer_point + 1
        print(f"Your Input is {_input} and Computer Input is {_random}")
        print("Computer wins 1 point")
        print(f"Computer has {computer_point} Point(s) and You have {human_point} Points")

    elif _input == "Paper" and _random == "Rock":
        human_point = human_point + 1
        print(f"Your Input is {_input} and Computer Input is {_random}")
        print("You Win 1 point")
        print(f"Computer has {computer_point} Point(s) and You have {human_point} Points")

    # if user enter 3

    elif _input == "Scissor" and _random == "Paper":
        human_point = human_point + 1
        print(f"Your input is {_input} and computer guess is {_random}")
        print("You Win 1 point")
        print(f"Computer has {computer_point} Point(s) and You have {human_point} Points")
    elif _input == "Scissor" and _random == "Rock":
        computer_point = computer_point + 1
        print(f"Your Input is {_input} and Computer Input is {_random}")
        print("Computer wins 1 point")
        print(f"Computer has {computer_point} Point(s) and You have {human_point} Points")

    if _input not in lst:
        print("you have input wrong \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if computer_point > human_point:
    print("Computer wins and you loose")

if computer_point < human_point:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")
