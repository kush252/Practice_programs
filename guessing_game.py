import random

game_title = "Guess the Number"
no_of_guesses = 0

print(game_title)
print("Welcome to the game!")
print("To start the game, please select a range")

begin = int(input("Enter the beginning of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Now the range is set from {begin} to {end}.")
the_number=int(random.randint(begin,end))
print("Lets start the game!")

while True:
  guess = input("Enter your guess: ")
  guess1=int(guess)
  if guess1 < the_number:
   print("Your guess is too low.Please try again.")
   no_of_guesses += 1
  elif guess1 > the_number:
   print("Your guess is too high.Please try again.")
   no_of_guesses += 1
  elif guess1 == the_number:
   print("Congratulations! You guessed the number!")
   no_of_guesses += 1
   print(f"You guessed the number in {no_of_guesses} guesses.")
   break

