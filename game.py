import random

puzzles = ["Kali", "Mint", "Debian", "Arch", "Gentoo", "Fedora", "Ubuntu"]

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

lives = 6
guessed_letters = []

puzzle = puzzles[random.randint(0, len(puzzles) - 1)]
display_puzzle = ' '.join(['_' if char.isalpha() else '' for char in puzzle])

print("Welcome to Hangman!")
print(HANGMANPICS[0])
print("Lives: {}".format(lives))
print("Current word: {}".format(' '.join(display_puzzle)))

while lives > 0 and '_' in display_puzzle:
    guess = input("Guess a letter: ").lower()

    if guess.isalpha() and len(guess) == 1:
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in puzzle.lower():
            for i in range(len(puzzle)):
                if puzzle[i].lower() == guess:
                    display_puzzle = display_puzzle[:2 * i] + puzzle[i] + display_puzzle[2 * i + 1:]
        else:
            lives -= 1
            print("Incorrect guess. Lives remaining: {}".format(lives))
            print(HANGMANPICS[6 - lives])

        guessed_letters.append(guess)

        print("\nLives: {}".format(lives))
        print("Current word: {}".format(' '.join(display_puzzle)))
        #print("Guessed letters: " + ', '.join(guessed_letters))
    else:
        print("Invalid input. Please enter a single letter.")

if '_' not in display_puzzle:
    print("Congratulations! You guessed the word.")
else:
    print("Game over. The word was: {}".format(puzzle))
