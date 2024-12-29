import random

lives = 6

game_over = False 

correct_letters = []

word_list = ['jjja', 'aosidja', 'paosdal']

chosen_word = random.choice(word_list)
    
while not game_over:

    guess = input('guess a letter: ').lower()
    display = ''

    for i in chosen_word:
        if i == guess:
            display += i
            correct_letters.append(guess)
        elif i in correct_letters:
            display += i
        else:
            display += '_'
            
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives = 0:
            game_over = True
            print('you loose')

    if '_' not in display:
        game_over = True
        print('win')
        