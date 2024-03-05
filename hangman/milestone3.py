def check_guess(guess):
  lc_guess = guess.lower()
  if lc_guess in word:
    print (f"Good guess! {lc_guess} is in the word.")
  else:
    print (f"Sorry, {lc_guess} is not in the word. Try again.")

def ask_for_input():
  return check_guess('A')
  while True:
    guess = input("Please enter a single letter:")
    if guess.isalpha() and len(guess) == 1:
      break
    else:
      print("Invalid letter. Please, enter a single alphabetical character.")
      

