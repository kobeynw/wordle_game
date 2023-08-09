import random


def intro(num_guess):
    print(f"\nWelcome to Wordle! In this game, you will have {num_guess} guesses to guess the random 5-letter word!\n"
          "If you guess a correct letter in the correct location, it will appear as a '!'.\n"
          "If you guess a correct letter in the wrong location, it will appear as a '?'.\n"
          "All other letters will appear as a '*'. Good luck!\n")


def exact_match(guess, char_index, char, answer):
    if char in answer:
        if guess[char_index] == answer[char_index]:
            return True
    return False


def in_answer(char, answer):
    if char in answer:
        return True
    return False


def read_text(text):
    with open(text) as file:
        return file.readlines()


def wordle(text, num_guess):
    intro(num_guess)
    word_bank = read_text(text)
    answer = random.choice(word_bank)
    answer = answer.replace('\n', '')
    letters_not_in_word = []
    attempt = 0
    while True:
        if attempt == int(num_guess):
            print(f"\nMaybe next time! The answer is {answer}.")
            break
        result = ""
        attempt += 1
        guess = input(f"\nGuess # {attempt}: \n")
        char_index = 0
        for char in guess:
            if exact_match(guess, char_index, char, answer):
                result += "!"
            elif in_answer(char, answer):
                result += "?"
            else:
                result += "*"
                if char not in letters_not_in_word:
                    letters_not_in_word.append(char)
            char_index += 1
        print(result)
        if guess == answer:
            print("\nCorrect! Way to go!")
            break
        print(f"\nLetters guessed that are not in the word:\n{', '.join(letters_not_in_word)}\n")


if __name__ == "__main__":
    wordle('wordle-answers-alphabetical.txt', num_guess=6)
