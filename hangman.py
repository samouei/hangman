
import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    '''
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    '''
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    '''
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def check_game_won(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    '''
    
    # Check if letters_guessed is not an empty list
    if len(letters_guessed) != 0:
        for char in secret_word: # Loop through characters in secret_word
            is_char_in_letters_guessed = False
            for i in letters_guessed: # Loop through items in letters_guessed to find a match
                if char == i:
                    is_char_in_letters_guessed = True
                    break
            if not is_char_in_letters_guessed:
                return False
        return True
                       
    else:
        return False
    
def get_word_progress(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and underscores (_) that represents
      which letters in secret_word have not been guessed so far
    '''
    
    # Declare an empty list to add found letters to
    word_progress = [] 
    
    # Check if letters_guessed is not an empty list
    if len(letters_guessed) != 0:
        for char in secret_word: # Loop through characters in secret_word
            if char in letters_guessed:
                word_progress.append(char) # If letter is matched in letters_guessed add it to word_progress
            else:
                word_progress.append("_") # If letter is not matched add "_" to word_progress
        return "".join(word_progress)
    
    # If no letters have been guessed return "_"s equal to the length of secret_word                
    else:
       return len(secret_word) * "_" 


def get_remaining_possible_letters(letters_guessed):
    '''
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which 
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    '''
    # Sort letters_guessed for efficiency
    sorted_letters_guessed = sorted(letters_guessed)
    remaining_letters = []
    
    # Check if letters_guessed is not an empty list
    if len(letters_guessed) != 0:
        for char in string.ascii_lowercase: # Loop through the alphabet (lowercase)
                if char not in letters_guessed: # If letter hasn't been guessed before add it to remaining_letters
                    remaining_letters.append(char) 
                else:
                    continue
        return "".join(remaining_letters) # Turn list to string
     
    # If no letters have been guessed return the entire alphabet                        
    else:
        return string.ascii_lowercase
        

def check_game_score(secret_word, number_of_guesses):
    '''
    secret_word: string, the lowercase word the user is guessing
    number_of_guesses : int, the number of remaining guesses

    returns: int, total score for the game
    '''   
    
    # Declare an empty list to add unique letters to
    unique_letters = [] 
    
    for char in secret_word: # Loop through the letters in secret_word
        if char not in unique_letters: # If letter is unique add it to unique_letters
            unique_letters.append(char)
        else:
            pass
        
    # Calculate and return the total score
    score = (3 * number_of_guesses) + (2 * (len(secret_word) + len(unique_letters)))
    return score

def choose_letter_revealed(secret_word, remaining_letters):
    '''
    secret_word: string, the lowercase word the user is guessing
    remaining_letters : string, string of available letters

    returns: string, letters to choose from
    ''' 
    
    # Declare an empty list to add remaining letters to choose from
    choose_from = [] 
    
    for char in secret_word: # Loop through the letters in secret_word
        if char in remaining_letters: # If letter is also in remaining letters add it to choose_from 
            choose_from.append(char)
        else:
            pass   
    return "".join(choose_from) # Turn list to string and return
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    # Declare variables
    score = 0
    number_of_guesses = 10
    letters_guessed = []
    guess = ""
    
    # Greet user
    print("Welcome to Hangman!")
    print("I am thinking of a word that is" , len(secret_word) , "letters long.")
    print("--------------")
    
    # Until the game is not won and user has guesses left ask for input
    while not check_game_won(secret_word, letters_guessed) and number_of_guesses > 0:
        if number_of_guesses == 1:
            print("You have", number_of_guesses, "guess left.")
        else:
             print("You have", number_of_guesses, "guesses left.")
        print("Available letters:", get_remaining_possible_letters(letters_guessed))

        guess = input("Please guess a letter: ")
        guess = guess.lower() # Make sure input is lower case
        
        # Check if input is an alphabet
        if not guess.isalpha(): 
            print("Oops! That is not a valid letter. Please input a letter from the alphabet: " + get_word_progress(secret_word, letters_guessed))
            print("--------------")
        
        # Check if guess is in secret_word
        elif guess in secret_word:
            if guess not in letters_guessed:
                letters_guessed.append(guess)
                print("Good guess:", get_word_progress(secret_word, letters_guessed))
                print("--------------")

            else:
                print("Oops! You've already guessed that letter:", get_word_progress(secret_word, letters_guessed))
                print("--------------")
        
        # If guess is not in secret_word check if it was entered before
        else:
            if guess not in letters_guessed:
                letters_guessed.append(guess)
                number_of_guesses -= 1 # Deduct one guess per wrong guess
                print("Oops! That letter is not in my word:", get_word_progress(secret_word, letters_guessed))
                print("--------------")
    
            else:
                print("Oops! You've already guessed that letter:", get_word_progress(secret_word, letters_guessed))
                print("--------------")
           
    # Check if the game is won or lost         
    if check_game_won(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print("Your total score for this game is:", check_game_score(secret_word, number_of_guesses))
    else: 
        print("Sorry, you ran out of guesses. The word was", secret_word)
        

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

# -----------------------------------


def hangman_with_help(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make sure that
      the user puts in a letter.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    * If the guess is the symbol *, you should reveal to the user one of the 
      letters missing from the word at the cost of 2 guesses. If the user does 
      not have 2 guesses remaining, print a warning message. Otherwise, add 
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    '''
    # Declare variables
    score = 0
    number_of_guesses = 10
    letters_guessed = []
    guess = ""
    
    # Greet user
    print("Welcome to Hangman!")
    print("I am thinking of a word that is" , len(secret_word) , "letters long.")
    print("--------------")
    
    # Until the game is not won and user has guesses left ask for input
    while not check_game_won(secret_word, letters_guessed) and number_of_guesses > 0:
        if number_of_guesses == 1:
            print("You have", number_of_guesses, "guess left.")
        else:
             print("You have", number_of_guesses, "guesses left.")
        print("Available letters:", get_remaining_possible_letters(letters_guessed))

        guess = input("Please guess a letter: ")
        guess = guess.lower() # Make sure input is lower case
        
        # Check if input is an alphabet and not "*"
        if not guess.isalpha() and guess != "*":
            print("Oops! That is not a valid letter. Please input a letter from the alphabet: " + get_word_progress(secret_word, letters_guessed))
            print("--------------")
        
        # Check if enough guesses left for revealing letter, deduct 2 points per revealed_letter 
        elif guess == "*":
            if number_of_guesses >= 2:
                number_of_guesses -= 2 
                
                # Call choose_letter_revealed fuction to get string of letters to choose from
                choose_from = choose_letter_revealed(secret_word, get_remaining_possible_letters(letters_guessed))
                new = random.randint(0, len(choose_from)-1)
                revealed_letter = choose_from[new]
                letters_guessed.append(revealed_letter) # Add revealed letter to letters_guessed
                print("Letter revealed:", revealed_letter)
                print(get_word_progress(secret_word, letters_guessed))
                print("--------------")
            else: 
                print("Oops! Not enough guesses left:", get_word_progress(secret_word, letters_guessed))
                print("--------------")
                
        # Check if guess is in secret_word and if it has been guessed before
        elif guess in secret_word:
            if guess not in letters_guessed:
                letters_guessed.append(guess)
                print("Good guess:", get_word_progress(secret_word, letters_guessed))
                print("--------------")

            else:
                print("Oops! You've already guessed that letter:", get_word_progress(secret_word, letters_guessed))
                print("--------------")
                
        # If guess is not in secret_word check if it has been guessed before
        else:
            if guess not in letters_guessed:
                letters_guessed.append(guess)
                number_of_guesses -= 1 # Deduct one guess per wrong guess
                print("Oops! That letter is not in my word:", get_word_progress(secret_word, letters_guessed))
                print("--------------")
    
            else:
                print("Oops! You've already guessed that letter:", get_word_progress(secret_word, letters_guessed))
                print("--------------")
           
    # Check if the game is won or lost           
    if check_game_won(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print("Your total score for this game is:", check_game_score(secret_word, number_of_guesses))
    else: 
        print("Sorry, you ran out of guesses. The word was", secret_word)


# When you've completed your hangman_with_help function, comment the two similar
# lines below that were used to run the hangman function, and then uncomment
# those two lines and run this file to test!

# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # To test part 2, uncomment the following two lines.

#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############

    # To test part 3, comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_help(secret_word)

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass
