def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        display = ""

        for char in secret_word:
            if char in guesses:
                display += char
            else:
                display += "_"

        print(display)

        for char in secret_word:
            if char not in guesses:
                return False

        return True

    return hangman_closure


# -------------------------
# Main Program
# -------------------------

secret_word = input("Enter the secret word: ")

hangman = make_hangman(secret_word)

while True:
    guess = input("Enter a letter: ")

    if hangman(guess):
        print("You guessed the word!")
        break