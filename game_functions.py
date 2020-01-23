from random import choice


WORDS_LIST = ['SKILLFACTORY',
              'TESTING',
              'BLACKBOX',
              'PYTEST',
              'UNITTEST',
              'COVERAGE']

LOGO = '''
             _ _                   
            | | |                  
  __ _  __ _| | | _____      _____    __ _  __ _ _ __ ___   ___
 / _` |/ _` | | |/ _ \ \ /\ / / __|  / _` |/ _` | '_ ` _ \ / _ \\
| (_| | (_| | | | (_) \ V  V /\__ \ | (_| | (_| | | | | | |  __/
 \__, |\__,_|_|_|\___/ \_/\_/ |___/  \__, |\__,_|_| |_| |_|\___|
  __/ |                               __/ |
 |___/                               |___/ '''


def show_menu():
    print('Enter 1 to start new game\n'
          'Enter 2 to learn the rules\n'
          'Enter 0 to exit')


def show_rules():
    print('\n1. Try to guess the word. Enter one letter per step.\n'
          '2. If you guess correctly, you will see letters.\n'
          '3. Else, you will get a penalty point.\n'
          '4. Four penalty points - the game is over.\n'
          'Good luck!\n')


def option_handler(option):
    try:
        option = int(option)
        if option == 0:
            return 0
        elif option == 1:
            play_game()
        elif option == 2:
            show_rules()
            show_menu()
            option_handler(input())
        else:
            print('\nNo such option!\n')
            show_menu()
            option_handler(input())
    except ValueError:
        print('\nNo such option!\n')
        show_menu()
        option_handler(input())


def print_hidden_word(word, letters: list):
    print()
    if letters:
        print(*[f'{char} ' if char in letters else '_ ' for char in word])
    else:
        print(*['_ ' for _ in word])


def is_valid(letter):
    return len(letter) == 1


def is_win(word, letters: list):
    return set(letters) == set(word)


def play_game():
    word = choice(WORDS_LIST)
    score = 0
    letters = []
    print_hidden_word(word, letters)
    while score < 4:
        letter = input('\nYour turn: ').strip().capitalize()
        if is_valid(letter):
            if letter in word:
                letters.append(letter)
                if is_win(word, letters):
                    print(f'\nYou are win! Word is {word}\n')
                    show_menu()
                    option = input()
                    option_handler(option)
                    break
                print_hidden_word(word, letters)
            else:
                score += 1
                print('\nPenalty points: ', score)
        else:
            print('Remember! Only one letter per step!')
    else:
        print('\nYou are loose. Try again!\n'
              'You will be lucky next time!\n')
        show_menu()
        option = input()
        option_handler(option)
