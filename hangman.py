import random

def choose_word():
    word_list = ["python", "java", "javascript", "kotlin", "swift", "ruby", "csharp", "cplusplus", "php", "go", "data-science", "machine-learning", "artificial-intelligence", "web-development", "software-engineering"]
    return random.choice(word_list).lower()

def play_hangman():
    word_to_guess = choose_word()
    word_letters = set(word_to_guess)  # Letters in the word
    alphabet = set(chr(i) for i in range(ord('a'), ord('z') + 1))  # All lowercase alphabets
    used_letters = set()  # What the user has guessed

    lives = 6  # Number of incorrect attempts allowed

    # Add a hint based on the type of word
    hint = ""
    if "-" in word_to_guess:  # Check for hyphenated words
        hint = "This is a compound word or phrase."
    elif word_to_guess in ["python", "java", "javascript", "kotlin", "swift", "ruby", "csharp", "cplusplus", "php", "go"]: # Check for programming languages
        hint = "This is a programming language."
    # Add more hints as you like (e.g., by category)
    #elif word_to_guess in ["apple", "banana", "orange"]:
    #    hint = "This is a fruit."

    while len(word_letters) > 0 and lives > 0:
        print("You have used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word_to_guess]
        print("Current word: ", " ".join(word_list))

        if hint: #Print hint if available
            print("Hint:", hint)

        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Correct guess!")
            else:
                lives -= 1
                print("Letter is not in the word.")

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print("You died, sorry. The word was", word_to_guess)
    else:
        print("You guessed the word", word_to_guess, "!!")


if __name__ == "__main__":
    print("Welcome to Hangman!")
    play_hangman()
    while True:
      play_again = input("Play again? (yes/no): ").lower()
      if play_again != 'yes':
        break
      play_hangman()
    print("Thanks for playing!")
