import random

#def play_game():
source_words = open("words.txt" , "r")
words = (source_words.readlines())
answer = random.choice(words)
print (answer)             


guesses = []
letters_guessed = 8


while guesses != 0:
    letter = input("Enter a letter: ")
    if letter in answer:
        print ("You got one!")
    # else:
    #     #letters_guessed = letters_guessed - 1
    #     print ("You have %d guesses left.") % (guesses)
    #     #letters_guessed.append(letters_guessed)

#play_game()

# """Let the user choose a level of difficulty at the beginning of the program.
   
#    Easy mode only has words of 4-6 characters;""" 
# def easy mode():
                                
#     for answer in words                    
#     if len(answer) >= 3 and len(answer) <= 5
    
# pass
# """normal mode only has words of 6-8 characters;"""
# def normal mode()
# word                                
#     for answer in words                    
#     if len(word) >= 6 and len(word) <= 8
# pass
# """hard mode only has words of 8+ characters."""
# def hard mode = len(8+)



# play_game()


# [letter if letter in guesses else "_" for letter in answer]




# """At the start of the game, let the user know how many letters the computer's
#    word contains."""

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

# # while True:
# #     print("""
# #     Would you like to play?"
# #     1) yes
# #     2) no
# #     """)
# #     option = input("y or n: ")

# # if option == "y":
# #         #play_game():
        
# # elif option == "n":
# #             print ("come back again")
# # break

