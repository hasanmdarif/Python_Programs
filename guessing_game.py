from random import *
print("========== THE GUESSING GAME ==========")
print("You will be given 100 coins initially. \nYou have to guess the correct number between 1 to 100(including both) which the program picks.\nEvery wrong guess will take away 5 coin from you but you'll be told if the guessed number is smaller or greater than the correct number. \nYou have to keep maximum coins with you")

best_score = 0
while(True):
  current_score = 100
  number = randint(1, 100)
  print("Current Coins : ", current_score)
  while(True):
    guess = int(input("Guess the number: "))
    if(guess<number):
      print("Your guess", guess ,"is smaller than than the correct number")
    elif(guess>number):
      print("Your guess", guess ,"is greater than than the correct number")
    else:
      print("YAYYY...!!!! Your guess is RIGHT")
      if(current_score>best_score):
        best_score = current_score
      print("Coins in this game : ", current_score)
      print("Highest coins gained in the best game so far : ", best_score)
      break
    current_score-=5
    print("Current Coins : ", current_score)
  cont = input("Do you want to play another round? (y/n)")
  if(cont=='y' or cont=='Y'):
    continue
  else:
    exit(0)


