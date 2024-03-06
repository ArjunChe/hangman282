import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.


    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has

    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE (set) letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_of_guesses: list
        A list of the guesses that have already been tried
    word_list: str
        A list of words
    Methods:
    -------
    check_guess(guess)
        Checks if the guess is in the word.
    ask_for_guess()
        Asks the user for a guess.
    '''
    def __init__(self, word_list, num_lives=5):
      self.word = list(random.choice(self.word_list).lower())
      self.word_guessed = ['_']*len(self.word)
      self.num_letters = len(set(self.word))
      self.num_lives = num_lives
      self.word_list = word_list
      self.list_of_guesses = []

      print(f"The mystery word has:  {len(self.word)} characters")
      print(f"{self.word_guessed}")
      pass

    def check_guess(self, guess) -> None:
        '''
        Checks if the guess is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The guess to be checked

        '''
        lc_guess = guess.lower()
        if lc_guess in list(self.word):
          print (f"Good guess! {lc_guess} is in the word.")
        if guess in list(self.word):
            self.num_letters -= 1
            for i, g in enumerate(list(self.word)):
              if g == lc_guess:
                self.word_guessed[i] == g
              else:
                self.num_lives -=1
                print(f"Sorry, {lc_guess} is not in the word")
                print(f"You have {self.num_lives} lives left")
        pass



    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_guess method.
        '''
        while True:
          guess = input("Please enter a single letter:")
          if guess.isalpha() == False and len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
          elif guess in self.list_of_guesses:
            print("You already tried that letter")
          else:
            self.check_guess(guess)
            self.list_of_guess.append(guess)
        pass


