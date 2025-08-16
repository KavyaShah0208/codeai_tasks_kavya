import random
from words import word_list1
from words import word_list2
from words import word_list3
#wordlist = ["tiger","lion","camel","deer","leopard","horse"]

difficulty = input("Enter diffulty level (1,2 or 3) :  ")

if difficulty == '1':
   word = random.choice(word_list1)
elif difficulty == '2'  :   
   word = random.choice(word_list2) 
elif difficulty == '3': 
   word = random.choice(word_list3)  
else:   
   print("Invalid input,choose again. ")
   difficulty = input("Enter diffulty level (1,2 or 3) :  ")


length = str(len(word))
print("It is a " + length + " letter word" )

length = int(length)

blank = 0
while(blank<length):    
    print("_", end =" ")
    blank = blank + 1

print("")

print("")

n = 0
game_over = False
correct = []
lives = length +1

print("You have " + str(lives) + " chances to guess the word")

print(word)
while not game_over: 
    
    guess = input("Enter a guess: ").lower() 
    a=len(guess)
    
   # while a != int(length) :
      # print('Inavlid input,Try again')
       #guess = ''
       #guess = input("Enter a guess: ").lower
      # a=len(guess)

    display =""
    letter_present=[]
    for letter in word: 
      if letter == guess[n] :    
        display += letter
        correct.append(guess)
        n = n+1
      elif letter in correct :
        display += letter
        n = n+1

      else:   
        display += "_"  
        n = n+1      

    for letter in guess :   
       if letter in word and letter not in display:
          letter_present.append(letter)

    x = len(letter_present)
    
    if  x>0:  
       print(str(letter_present) + ' are there in the word but the positions are incorrect')
   
    letter_present=[]
    n=0
    print(display)
    x=0
      
    if "_" not in display:
        game_over = True
        print("Word Guessed:"+ word)
