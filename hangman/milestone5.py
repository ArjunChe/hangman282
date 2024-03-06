import random

class Hangman:
  
  def __init__(self, word_list, num_lives):
    self.word_list = word_list
    self.num_lives = 5
    self.word = list(random.choice(self.word_list).lower())
    self.word_guessed = ['_']*len(self.word)
    self.num_letters = len(set(self.word))
    self.list_of_guesses=[]
    
    print(f"The mystery word has:  {len(self.word)} characters")
    print(f"{self.word_guessed}")
    pass

  def check_guess(self, guess) -> None:
        if guess in list(self.word):
          self.num_letters -= 1                   
          for i, G in enumerate(self.word):
            if G == guess:
              self.word_guessed[i] = G
          print(f"Good guess! {guess} is in the word.")
          print(f"Your word so far : {self.word_guessed}")
        else:
          self.num_lives -=1
          print(f"Sorry, {guess} is not in the word. You have {self.num_lives} lives left")
          print(f"Your word so far : {self.word_guessed}")
        pass



  def ask_for_input(self):
        while True:
          guess = input("Please enter a single letter:").lower()
          if guess.isalpha() == False or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")            
          elif guess in self.list_of_guesses:
            print("You already tried that letter")                      
          else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
          break              

def play_game(word_list):
  game = Hangman(word_list, num_lives=5) 
  while game.num_lives > 0:
    game.ask_for_input()
    if game.num_lives == 0:
      print(f"You lost. The word was : {game.word}.")      
      break
    elif game.num_letters == 0:
      print("Congratulations, you won!") 
      break 
if __name__ == '__main__':
  word_list = ["button", "smoke", "literate", "momentous", "cactus", "toys", "pedal", "sneeze", "grandiose", "wool", "symptomatic", "willing", "behave", "automatic", "cats", "festive", "growth", "sparkle", "girl", "sand", "word", "drip", "overt", "helpless", "wanting", "notice", "lowly", "soft", "decision", "crate", "wakeful", "languid", "disappear","same", "station", "inquisitive", "vein", "tart", "frogs", "cattle", "fade", "hateful", "iron", "ruddy", "purple", "dislike", "measure", "historical"]
  play_game(word_list)
