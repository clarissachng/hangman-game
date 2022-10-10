# Create a random list of words for the game to choose from.
wordList = ['fares', 'soup', 'mount', 'extend', 'brown', 'expert', 'tired', 'humidity', 'backpack', 'crust', 
             'dent', 'market', 'knock', 'windy', 'coin', 'throw', 'silence', 'bluff', 'downfall', 'climb', 
             'match', 'excite', 'thinking', 'coat', 'emerald', 'coherent', 'multiple', 'square', 'dream', 'mutation',
             'strict', 'film', 'guide', 'strain', 'settle', 'marching', 'optimal', 'medley', 'rage', 'figure',
             'plague', 'there', 'reusable', 'refinery', 'suffer', 'affirm', 'captive', 'flipping', 'prolong', 'main']

# Get word from the wordlist
def GetWord():
  import random
  
  word = random.choice(wordList)
  return word.upper()

# Function of main hangman game
def Hangman(word):
  # Number of dashes which = to the length of the word
  completeWord = "-" * len(word)
  guessed = False
  # Create empty lists to input guessed letters and guessed words
  guessedLetters = []       
  guessedWords = []     
  # Number of tries for the game
  lives = 7      
  print("Let's play Hangman!")
  print("You can guess a letter or a word each round.")
  print(completeWord)
  print(f"You have {lives} live(s) left!\n")

  while not guessed and lives > 0:
    userGuess = input("Plese put in your next guess:\n").upper()
    # If the user guesses a letter
    if len(userGuess) == 1 and userGuess.isalpha():  
      # If the user has guessed the letter   
      if userGuess in guessedLetters:       
        print("You already guessed the letter", userGuess)
      # If the guessed letter is not in the word and has not been guessed yet
      # User loses a life and letter will be stored into the guessed letters list
      elif userGuess not in word:       
        print(userGuess, "is not the word.")
        lives -= 1
        guessedLetters.append(userGuess)
      # If the gussed letter is in the word
      else:       
        print(userGuess, "is in the word!")
        guessedLetters.append(userGuess)
        # Change the word string to a list 
        wordAsList = list(completeWord)
        # Enumerate the word to get the index i and letter of the index for each iteration
        x = [i for i, letter in enumerate(word) if letter == userGuess]
        # use a for loop for the indicies to replace the dashes to the guessed letter 
        for index in x:
          wordAsList[index] = userGuess
        completeWord = "".join(wordAsList)  # convert the list to a string
        # if the guessed letter completes the word
        if "-" not in completeWord:
          guessed = True

    # If the user has a word with the same word length with the secret word
    elif len(userGuess) == len(word) and userGuess.isalpha(): 
      # User already guessed the word 
      if userGuess in guessedWords:     
        print("You've already guessed the word", userGuess)
      # User has not gussed the word yet and it's incorrect
      # User will lose a life and the word will be store into the guessed words list
      elif userGuess != word:       
        print(userGuess, "is not the word :(")
        lives -= 1        
        guessedWords.append(userGuess)
      # User guessed the correct word
      else:
        guessed = True
        completeWord = word

    # If user inputs other charcters besides the alphabet
    else:
      print("\nNot a valid guess. Please enter your guess again.")

    print(f"You have {lives} live(s) left!")
    print(completeWord, "\n")
  
  if guessed:
    print(f"\nYou found the word! It was {word}!")
  else:
    print(f"\nGame over :( The word was {word}")

# Main function

def Main():
  word = GetWord()
  Hangman(word)

  ans = input('Would you like to play again? (Y/N)\n')
  if (ans.upper() == 'Y'):
    word = GetWord()
    Hangman(word)
  else:
    print('See you next time!')

#Code to run the game
Main()