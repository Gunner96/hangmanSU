# NAME: KUNAL
# PHONE: 9933562045
# EMAIL: bhaichungtamang@gmail.com

import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
stages = hangman_art.stages
dialogue = hangman_words.dialogue


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
print(chosen_word)

print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"

while not 0:
    guess = str(input("Guess a letter: ").lower())
    if len(guess) > 1:
        print("I know you\'r nervous, please enter a single character.")
        continue
    if guess in display:
        print("The letter is already chosen, trying to buy time I see.👀")
        continue

    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"You choose {guess}, {dialogue[lives]}")
        
        if lives == 0:
            print("You lose.")
            print(f"The word was {chosen_word}")
            break

    if "_" not in display:
        print(f"{chosen_word} is the word, You win. Hangman at ease, Next!!!")
        break

    print(stages[lives])
    print(f"{' '.join(display)}")