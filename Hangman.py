import random
def hangman():
    words = ['Rockstar', 'Steam', 'Electronic Arts', 'Epic Games', 'Ubisoft', 'Gameloft']
    word = random.choice(words).lower()
    guessed_letters = []
    attempts = 6
    stages = [
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     /  
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |     
           -
        """,
        """
           --------
           |      
           |      
           |    
           |     
           -
        """
    ]
    print("Welcome to Hangman!")
    while attempts > 0:
        display_word = "".join([letter if letter in guessed_letters or letter == " " else "_" for letter in word]) 
        print(stages[attempts])
        print(f"Word: {display_word}")
        print(f"Attempts remaining: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        if "_" not in display_word:
            print(f"\nCongratulations! You guessed the word: {word}")
            break
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue
        guessed_letters.append(guess)
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not there.")
    if attempts == 0:
        print(stages[0])
        print(f"Game Over! The word was: {word}")
if __name__ == "__main__":
    hangman()
