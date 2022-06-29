import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
blank = []
lives = 6
stages = hangman_art.stages
print(hangman_art.logo)
for _ in range(len(chosen_word)):
    blank += '_'
end_of_game = False
while not end_of_game:
    guess = input('please enter letter').lower()
    if guess in blank:
        print(f'You have already guessed {guess}')
    for i in range(0, len(chosen_word)):
        if guess == chosen_word[i]:
            blank[i] = guess
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose')
    print(blank)
    if '_' not in blank:
        end_of_game = True
        print('You win')

    print(stages[lives])
