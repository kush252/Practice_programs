import random

game_title = "Guess the Number"
no_of_guesses = 0

print(game_title)
print("Welcome to the game!")
print("To start the game, please select a range")

begin = int(input("Enter the beginning of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Now the range is set from {begin} to {end}.")
the_number = random.randint(begin, end)
print(the_number)
print("Lets start the game!")


while True:
  guess = input("Enter your guess: ")
  try:
    guess1 = int(guess)
  except ValueError:
    print("Please enter a valid integer.")
    continue
  no_of_guesses += 1
  if guess1 < the_number:
    print("Your guess is too low. Please try again.")
  elif guess1 > the_number:
    print("Your guess is too high. Please try again.")
  else:
    print("Congratulations! You guessed the number!")
    print(f"You guessed the number in {no_of_guesses} guesses.")
    break

