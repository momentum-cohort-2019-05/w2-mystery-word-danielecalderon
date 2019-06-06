import random
words = open("words.txt")
answer = random.choice(words)

print (answer)

guesses = []
[letter if letter in guesses else "_" for letter in answer]

"""Let the user choose a level of difficulty at the beginning of the program.
   Easy mode only has words of 4-6 characters;""" 
easy mode = len(4-6)
pass
"""normal mode only has words of 6-8 characters;"""
normal mode = len(6-8)
pass
"""hard mode only has words of 8+ characters."""
hard mode = len(8+)


"""At the start of the game, let the user know how many letters the computer's
   word contains."""

guess_word = Print("this is how many words" )

""""Ask the user to supply one guess (i.e. letter) per round. This letter can be
   upper or lower case and it should not matter. If a user enters more than one
   letter, tell them the input is invalid and let them try again."""

"""Let the user know if their guess appears in the computer's word."""
def print_word(word, guesses):
    output_letters = [display_letter(letter, guesses) 
                      for letter in word]
    print(" ".join(output_letters))
    
print_word(word, guesses)

"""Display the partially guessed word, as well as letters that have not been
   guessed. For example, if the word is BOMBARD and the letters guessed are a, b,
   and d, the screen should display:

```
B _ _ B A _ D
```"""

"""A user is allowed 8 guesses. Remind the user of how many guesses they have left
after each round."""

"""_A user loses a guess only when they guess incorrectly._ If they guess a letter
that is in the computer's word, they do not lose a guess."""

"""If the user guesses the same letter twice, do not take away a guess. Instead,
print a message letting them know they've already guessed that letter and ask
them to try again."""

"""The game should end when the user constructs the full word or runs out of
guesses. If the player runs out of guesses, reveal the word to the user when
the game ends."""

"""When a game ends, ask the user if they want to play again. The game begins
again if they reply positively."""

while True:
    print("""
    Would you like to play agian?"
    1) yes
    2) no
    """)
    option = input("y or n: ")

    # if option == "y":
    #     #play_game():
    #     pass
    #     elif option == "n":
    #         print ("come back again")
    #     break

