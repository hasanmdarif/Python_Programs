import random
minimum = 1
maximum = 6


while 1:
    print("Rolling pair of Dices!!!")
    print("Player 1",end=" ")
    print(random.randint(minimum, maximum))
    print("Player 2",end=" ")
    print(random.randint(minimum, maximum))
    if(input("Roll the dices again?(Y/N) ") == "N"):
        break