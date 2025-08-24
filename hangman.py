import random as rd
from types import CoroutineType

name=input("What is your name?\n ")
print(f"Welcome to the Hangman game {name}!")
fruits_list=["pear","apricot","orange","grapes","mango","plum","lime","jackfruit"]
print("In this game you have to guess the word by guessing the letters in the word.")
print("Hint: The word is a fruit.")
fruit_selected=rd.choice(fruits_list)
guess_list=[]
#print(fruit_selected)
no_of_letters=len(fruit_selected)
no_of_dashes=no_of_letters
for x in range(no_of_letters):
  print("_",end=" ")
  
xyz=int(no_of_letters-1)

guess_avail=no_of_letters+2
print(f"\nYou have {guess_avail} guesses.")
while guess_avail > 0:
  guess=input("\nEnter your guess.\n")
  if guess in fruit_selected:
    print("You guessed it correctly!")
    guess_list.append(guess)
    
    #print(guess_list)
    for x in fruit_selected:
      if len(guess_list)==1:
        if x==guess_list[0]:
            print(guess_list[0],end=" ")
            continue
      
      if len(guess_list)==2:
        if x==guess_list[0]:
            print(guess_list[0],end=" ")
            continue
        if x==guess_list[1]:
          print(guess_list[1],end=" ")
          continue
      
        
      if len(guess_list)==3:
        if x==guess_list[0]:
            print(guess_list[0],end=" ")
            continue
        if x==guess_list[1]:
          print(guess_list[1],end=" ")
          continue
        if x==guess_list[2]:
          print(guess_list[2],end=" ")
          continue
      
          
      if len(guess_list)==4:
        if x==guess_list[0]:
            print(guess_list[0],end=" ")
            continue
        if x==guess_list[1]:
          print(guess_list[1],end=" ")
          continue
        if x==guess_list[2]:
          print(guess_list[2],end=" ")
          continue
        if x==guess_list[3]:
          print(guess_list[3],end=" ")
          continue
      
      
      if len(guess_list)==5:
        if x==guess_list[0]:
            print(guess_list[0],end=" ")
            continue
        if x==guess_list[1]:
          print(guess_list[1],end=" ")
          continue
        if x==guess_list[2]:
          print(guess_list[2],end=" ")
          continue
        if x==guess_list[3]:
          print(guess_list[3],end=" ")
          continue
        if x==guess_list[4]:
          print(guess_list[4],end=" ")
          continue
      
      
      if len(guess_list)==6:
        if x==guess_list[0]:
            print(guess_list[0],end=" ")
            continue
        if x==guess_list[1]:
          print(guess_list[1],end=" ")
          continue
        if x==guess_list[2]:
          print(guess_list[2],end=" ")
          continue
        if x==guess_list[3]:
          print(guess_list[3],end=" ")
          continue
        if x==guess_list[4]:
          print(guess_list[4],end=" ")
          continue
        if x==guess_list[5]:
          print(guess_list[5],end=" ")
          continue
            

      if len(guess_list)==7:
        if x==guess_list[0]:
            print(guess_list[0],end=" ")
            continue
        if x==guess_list[1]:
          print(guess_list[1],end=" ")
          continue
        if x==guess_list[2]:
          print(guess_list[2],end=" ")
          continue
        if x==guess_list[3]:
          print(guess_list[3],end=" ")
          continue
        if x==guess_list[4]:
          print(guess_list[4],end=" ")
          continue
        if x==guess_list[5]:
          print(guess_list[5],end=" ")
          continue
        if x==guess_list[6]:
          print(guess_list[6],end=" ")
          continue
      

      if len(guess_list)==8:
        if x==guess_list[0]:
            print(guess_list[0],end=" ")
            continue
        if x==guess_list[1]:
          print(guess_list[1],end=" ")
          continue
        if x==guess_list[2]:
          print(guess_list[2],end=" ")
          continue
        if x==guess_list[3]:
          print(guess_list[3],end=" ")
          continue
        if x==guess_list[4]:
          print(guess_list[4],end=" ")
          continue
        if x==guess_list[5]:
          print(guess_list[5],end=" ")
          continue
        if x==guess_list[6]:
          print(guess_list[6],end=" ")
          continue
        if x==guess_list[7]:
          print(guess_list[7],end=" ")
          continue
      

      if len(guess_list)==9:
        if x==guess_list[0]:
            print(guess_list[0],end=" ")
            continue
        if x==guess_list[1]:
            print(guess_list[1],end=" ")
            continue
        if x==guess_list[2]:
          print(guess_list[2],end=" ")
          continue
        if x==guess_list[3]:
          print(guess_list[3],end=" ")
          continue
        if x==guess_list[4]:
          print(guess_list[4],end=" ")
          continue
        if x==guess_list[5]:
          print(guess_list[5],end=" ")
          continue
        if x==guess_list[6]:
          print(guess_list[6],end=" ")
          continue
        if x==guess_list[7]:
          print(guess_list[7],end=" ")
          continue
        if x==guess_list[8]:
          print(guess_list[8],end=" ")
          continue
      
      
      print("_",end=" ")
      
    guess_avail-=1
    if(len(guess_list)==no_of_letters):
       guess_avail=0
       print("Yayy You won !!")
    
  if guess not in fruit_selected:
    print("You did not guess it correctly. Try again.")
    guess_avail-=1

    