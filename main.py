from replit import clear
from random import choice
from time import sleep
from art import logo, vs, game_over_logo
from game_data import data


def restart_game():
  game_over = False
  while game_over == False:
    restart = input("Restart game? (y/n) ")
    if restart == "y":

      # Clear screen between rounds:
      clear()
      sleep(1)
      # Restart game:
      higher_lower()
    else:
      print('''
      Good Bye!''')
      game_over = True
      return


def check_answer(guess, a_followers, b_followers):
  '''Use if statements to check if user is correct'''
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def higher_lower():

  # Display game logo
  print(logo)
  sleep(2)
  score = 0
  repeat_question = True
  while repeat_question:

    # Generate a random account from the game data.  
    account_a = choice(data)
    account_b = choice(data)

    if account_a == account_b:
      account_b = choice(data)
    

    def format_data(account):
      '''Format the account into printable format.'''
      account_name = account["name"]
      account_desc = account["description"]
      account_country = account["country"]
      return f"{account_name}, a {account_desc}, from {account_country}"
    print(f"Score: {score}")
    print("")
    print(f"A: {format_data(account_a)}.")
    print(vs)
    print(f"B: {format_data(account_b)}.")
    print('''

    ''')

    # Ask user for a guess.
    guess = input("Who has more followers? (A or B): ").lower()
    print('''
    
    ''')

    # Check if user is correct

    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    print(is_correct)

    # Give user feedback on their guess:
    if is_correct:
      print("Correct!")
      sleep(3)
      score += 1
      clear()
      
    else:
      repeat_question = False
      print("Sorry, wrong answer.")
      sleep(3)
      clear()
      print(game_over_logo)
      print(f'''
      Your Score: {score}
      
      
      ''')
      
      score = 0
      # Make the game repeatable
      sleep(2)
      restart_game()

 
higher_lower()

