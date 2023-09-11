import random

def get_user_choice():
  """Prompt the user to choose rock, paper, or scissors."""
  choices = ['rock', 'paper', 'scissors']
  print('Choose rock, paper, or scissors:')
  user_choice = input()
  while user_choice not in choices:
    print('Invalid choice! Please choose rock, paper, or scissors:')
    user_choice = input()
  return user_choice

def get_computer_choice():
  """Generate a random choice (rock, paper, or scissors) for the computer."""
  return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
  """Determine the winner based on the user's choice and the computer's choice."""
  if user_choice == computer_choice:
    return 'tie'
  elif (user_choice == 'rock' and computer_choice == 'scissors') or \
      (user_choice == 'paper' and computer_choice == 'rock') or \
      (user_choice == 'scissors' and computer_choice == 'paper'):
    return 'user'
  else:
    return 'computer'

def display_result(user_choice, computer_choice, winner):
  """Show the user's choice, the computer's choice, and the result."""
  print('Your choice:', user_choice)
  print('Computer choice:', computer_choice)
  if winner == 'tie':
    print('It\'s a tie!')
  elif winner == 'user':
    print('You win!')
  else:
    print('Computer wins!')

def play_again():
  """Ask the user if they want to play another round."""
  print('Do you want to play again? (y/n)')
  play_again = input()
  return play_again == 'y'


def main():
  while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, winner)
    if not play_again():
      break


if __name__ == '__main__':
  main()
