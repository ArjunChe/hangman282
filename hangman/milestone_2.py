import random
word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry']
print(word_list)
word = random.choice(mylist)

guess = input("Please enter a single letter:")
if guess.isalpha() and len(guess) == 1:
  print ("Good Guess!")
else:
  print ("Oops! That is not a valid input.")



