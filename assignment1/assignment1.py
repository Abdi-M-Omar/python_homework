# Task 1: Hello
# This function takes no arguments and returns the exact string "Hello!"

def hello():
    return "Hello!"


# Test print - this is only for checking manually
print(hello())

# Task 2: Greet with a formatted string
def greet(name):
    return f"Hello, {name}!"


print(greet("James"))

# ----------------------------------------------------
# Task 3: Multiply two numbers
# This function accepts two numbers and returns
# their product.
# Example:
# calc(5, 6) -> 30
# ----------------------------------------------------
def calc(val1, val2, operation="multiply"):
    try:
        match operation:
            case "add":
                return val1 + val2
            case "subtract":
                return val1 - val2
            case "multiply":
                return val1 * val2
            case "divide":
                return val1 / val2
            case "modulo":
                return val1 % val2
            case "int_divide":
                return val1 // val2
            case "power":
                return val1 ** val2
            case _:
                return "Unknown operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    # ----------------------------------------------------
# Task 4: Data Type Conversion
# This function converts a value to the requested type.
# Supported types: int, float, str
# If the conversion fails, return an error message.
# ----------------------------------------------------
def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {data_type}."
    
# ----------------------------------------------------
# Task 5: Grading System
# This function accepts any number of grades using *args,
# calculates the average, and returns the corresponding
# letter grade.
# ----------------------------------------------------
def grade(*args):
    try:
        average = sum(args) / len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    except TypeError:
        return "Invalid data was provided."

# ----------------------------------------------------
# Task 6: Repeat a string using a for loop
# This function repeats a string 'count' times.
# Use a for loop with range(), not string multiplication.
# ----------------------------------------------------
def repeat(text, count):
    result = ""

    for i in range(count):
        result += text

    return result
# ----------------------------------------------------
# Task 7: Student Scores using **kwargs
# If mode is "best", return the student's name with the
# highest score.
# If mode is "mean", return the average score.
# ----------------------------------------------------
def student_scores(mode, **kwargs):
    if mode == "best":
        best_student = max(kwargs, key=kwargs.get)
        return best_student

    elif mode == "mean":
        return sum(kwargs.values()) / len(kwargs)
    # ----------------------------------------------------
# Task 8: Titleize
# Convert a string into title case following the rules:
# - First word is always capitalized.
# - Last word is always capitalized.
# - Middle words are capitalized unless they are
#   one of the "little words".
# ----------------------------------------------------
def titleize(text):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]

    words = text.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        elif word.lower() in little_words:
            words[i] = word.lower()
        else:
            words[i] = word.capitalize()

    return " ".join(words)
# ----------------------------------------------------
# Task 9: Hangman
# Reveal the letters in the secret word that appear
# in the guess string. Replace all other letters with
# an underscore (_).
# ----------------------------------------------------
def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"

    return result
# ----------------------------------------------------
# Task 10: Pig Latin
# Convert an English sentence into Pig Latin.
# Rules:
# 1. If a word starts with a vowel, add "ay".
# 2. If it starts with consonants, move them to the
#    end and add "ay".
# 3. Treat "qu" as a single consonant cluster.
# ----------------------------------------------------
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []

    for word in words:

        # Rule 1: Word begins with a vowel
        if word[0] in vowels:
            result.append(word + "ay")
            continue

        # Find where the first vowel occurs
        index = 0
        while index < len(word):

            # Handle "qu" together
            if word[index:index + 2] == "qu":
                index += 2
                continue

            if word[index] in vowels:
                break

            index += 1

        # Move beginning consonants to the end
        pig_word = word[index:] + word[:index] + "ay"
        result.append(pig_word)

    return " ".join(result)