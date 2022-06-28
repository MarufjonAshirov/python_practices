import random

words = ['hello', 'break']
guess = input('please enter letter').lower()
chosen_word = words[random.randint(0, len(words))]
blank = []
for i in range(0, len(chosen_word)):
    if guess == chosen_word[i]:
        blank.insert(i, guess)
    else:
        blank.insert(i, '_')
print(blank)
