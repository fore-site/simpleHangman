import random

# function that replaces all instance of the letter in the new hangman word
def replace_all_index(choice, selected_word, hangman):
    for i,j in enumerate(selected_word):
        if j == choice:
            hangman[i] = choice

# function that pluralizes or singularizes "turn"
def turn():
    return 'turn' if length == 1 else "turns"

# list of words to be randomly generated in the game.
words = ['python', 'programming', 'scraping', 'internet', 'web']

selected_word = random.choice(words)

length = len(selected_word)

# create empty hangman list
hangman = ['_'] * length

#print the hangman list as a string
print('_ '.join(hangman))

choice = input('Enter a letter: ').lower()
while length >= 1:
    if len(choice) == 1:
        # check if the letter has already been correctly selected before
        if choice in hangman:
            length -= 1
            print(f'{length} {turn()} left')
            print(f"You have already picked this letter earlier.\n {' '.join(hangman)}")
            choice = input('Select a new letter: ').lower()
            continue
        # check if the letter exists in the original word
        if choice in selected_word:
            # use the index in the original word to replace all the letters in the hangman word.
            replace_all_index(choice, selected_word, hangman)
            print(' '.join(hangman))
            # check if the original word is equal to the hangman word. If it is, break out of loop
            if list(selected_word) == hangman:
                print(f'Congratulations! You found the word.')
                break
        else:
            length -= 1
            # check if the game has gotten to the last turn, represented by length
            if length == 0:
                print(f'You failed! The word is {selected_word}')
                break
            else:
                print(f'{length} {turn()} left')
                print(' '.join(hangman))
        choice = input('Enter a letter: ').lower()
    else:
        # if user inputs more than one letter
        choice = input('Enter only a single letter: ').lower()
        continue
