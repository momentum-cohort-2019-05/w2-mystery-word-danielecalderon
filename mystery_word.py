import random
import re

words = open("words.txt") 
source_words = words.read()
#print (source_words)
source_words = source_words.lower().split()
#print (source_words)

def easy_mode(word_list):
    easy_word_list = []
    for word in word_list:                    
        if len(word) >= 3 and len(word) <= 5:
            easy_word_list.append(word)
    return easy_word_list

"""normal mode only has words of 6-8 characters;"""
def normal_mode(word_list):
    normal_mode_list = []
    for word in word_list:
        if len(word) >= 6 and len(word) <= 7:
            normal_mode_list.append(word)
    return normal_mode_list

"""hard mode only has words of 8+ characters."""
def hard_mode(word_list):
    hard_mode_list = []
    for word in word_list:
        if len(word) >= 8:
            hard_mode_list.append(word)
    return hard_mode_list

def answer_word(word_list): 
    answer_word = random.choice(word_list)
    #return answer_word
    return (answer_word)  
    #i = self._randbelow(len(seq))

def difficulty(): 
    difficulty = input("What difficulty do you want? Please enter (e)asy, (m)edium or (h)ard.\n")
    difficulty = difficulty.lower()
    if difficulty == "e":
        answer = answer_word(easy_mode(source_words))
    elif difficulty == "m":
        answer = answer_word(normal_mode(source_words))
    elif difficulty == "h":
        answer = answer_word(hard_mode(source_words))
        #print (answer)
    return answer 
    game()

def game(answer):
    guesses = []
    fails = 0
    print("The word you're looking for has {} letters.".format(len(answer)))

def game_start():
    
    
    #while True:
        print("""
        Would you like to play?"
        1) yes
        2) no
        """)
        option = input("y or n: ")

        if option == "y":
            difficulty()
            #answer_word(word_list)
        elif option == "n":
            print ("come back again")

game_start()

#game(answer)

#
#difficulty()
#answer_word(word_list)


# guesses = []
# letters_guessed = []
# guesses = 8


# """Let the user choose a level of difficulty at the beginning of the program.
   
#    Easy mode only has words of 4-6 characters;""" 

# [letter if letter in guesses else "_" for letter in answer]

#For letter in answer:





# guess_word = Print("this is how many words" )

# """"Ask the user to supply one guess (i.e. letter) per round. This letter can be
#    upper or lower case and it should not matter. If a user enters more than one
#    letter, tell them the input is invalid and let them try again."""

# """Let the user know if their guess appears in the computer's word."""
# #

# """Display the partially guessed word, as well as letters that have not been
#    guessed. For example, if the word is BOMBARD and the letters guessed are a, b,
#    and d, the screen should display:

# ```
# B _ _ B A _ D
# ```"""

# """A user is allowed 8 guesses. Remind the user of how many guesses they have left
# after each round."""

# """_A user loses a guess only when they guess incorrectly._ If they guess a letter
# that is in the computer's word, they do not lose a guess."""

# """If the user guesses the same letter twice, do not take away a guess. Instead,
# print a message letting them know they've already guessed that letter and ask
# them to try again."""

# """The game should end when the user constructs the full word or runs out of
# guesses. If the player runs out of guesses, reveal the word to the user when
# the game ends."""

# """When a game ends, ask the user if they want to play again. The game begins
# again if they reply positively."""

