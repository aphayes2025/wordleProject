"""
aidan hayes
Wordle project with no GUI
"""
import random
ATTEMPTS = 7


# driver
def main():
    print("Hi, welcome to Aidan's Wordle.")
    print("Directions: Capital Letters means you got the word in the right spot.")
    print("Lower case letters means wrong spot but in word.")
    print("Empty means it's not in the word. Good Luck!")
    word = get_random_word()
    guesses = 1
    while guesses < ATTEMPTS:
        user_guess = str(input("Guess a 5 letter word: "))
        while len(user_guess) != 5:
            print("Your guess must be 5 letters long. Try again!")
            user_guess = str(input("Guess a 5 letter word: "))
        guess = checking_word(user_guess, word)
        if guess.lower() == word:
            print(f"Congrats you completed the Wordle today. You got it on your {guesses} try.")
            exit()
        else:
            print(f'{guess}')
            guesses += 1
    if guesses > 6:
        print(f"Sorry, better luck next time. The word was {word}.")


# to get random word from a list
def get_random_word():
    list_words = ['apple', 'shark', 'pecan', 'fight', 'place', 'farts', 'usual', 'horse', 'reply', 'weigh', 'boast',
                  'bloom']
    randWord = random.choice(list_words)
    return randWord


# to find which letters are in word
def checking_word(user_word, actual_word):
    new_word = ''
    for i in range(len(actual_word)):
        if user_word[i] == actual_word[i]:
            new_word += actual_word[i].capitalize()
        elif user_word[i] in actual_word:
            new_word += user_word[i]
        else:
            new_word += '_'
    return new_word

main()


