from replit import clear
from random import choice, randint
from time import sleep
from art import logo, vs
from game_data import data


def restart_game():
  game_over = False
  while game_over == False:
    restart = input("Restart game? (y/n) ")
    if restart == "y":
      clear()
      sleep(1)
      higher_lower()
    else:
      print("Good Bye!")
      game_over = True
      return


def higher_lower():
  # Display game logo
  print(logo)
  for k in data:

    random_person = randint(k, len(data))
    print(random_person)
    # for v in k:
    #   random_person = randint(k[v], len(data))
    #   print(random_person)
      

higher_lower()


restart_game()