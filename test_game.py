from game_functions import print_hidden_word, is_valid, is_win, show_menu, show_rules
import game_functions
import pytest


def test_print_hidden_word(capsys):
    print_hidden_word('TEST', [])
    assert capsys.readouterr().out == '\n_  _  _  _ \n'
    print_hidden_word('XXXX', ['X'])
    assert capsys.readouterr().out == '\nX  X  X  X \n'
    print_hidden_word('SKILL', ['S', 'I'])
    assert capsys.readouterr().out == '\nS  _  I  _  _ \n'


def test_is_valid():
    assert is_valid('a') is True
    assert is_valid('df') is False
    assert is_valid('') is False


def test_is_win():
    assert is_win('test', ['t', 's', 'e']) is True
    assert is_win('skill', ['s', 'l']) is False
    assert is_win('xxxx', []) is False


def test_show_menu(capsys):
    show_menu()
    assert capsys.readouterr().out == 'Enter 1 to start new game\n'\
                                      'Enter 2 to learn the rules\n'\
                                      'Enter 0 to exit\n'


def test_show_rules(capsys):
    show_rules()
    assert capsys.readouterr().out == '\n1. Try to guess the word. Enter one letter per step.\n'\
                                      '2. If you guess correctly, you will see letters.\n'\
                                      '3. Else, you will get a penalty point.\n'\
                                      '4. Four penalty points - the game is over.\n'\
                                      'Good luck!\n\n'


def test_play_game_win(capsys):

    input_values = ['t', 'E', 's', 'i', 'n', 'g', '0']
    game_functions.WORDS_LIST = ['TESTING']

    def spoof_input(prompt=None):
        if prompt:
            print(prompt, end='')
        return input_values.pop(0)

    game_functions.input = spoof_input
    game_functions.play_game()

    out, err = capsys.readouterr()

    assert out == ''.join(['\n_  _  _  _  _  _  _ \n\nYour turn: ',
                           '\nT  _  _  T  _  _  _ \n\nYour turn: ',
                           '\nT  E  _  T  _  _  _ \n\nYour turn: ',
                           '\nT  E  S  T  _  _  _ \n\nYour turn: ',
                           '\nT  E  S  T  I  _  _ \n\nYour turn: ',
                           '\nT  E  S  T  I  N  _ \n\nYour turn: ',
                           '\nYou are win! Word is TESTING\n'
                           '\nEnter 1 to start new game\n'
                           'Enter 2 to learn the rules\n'
                           'Enter 0 to exit\n'])
    assert err == ''


def test_play_game_fail(capsys):

    input_values = ['h', 'y', 'f', 'j', '0']
    game_functions.WORDS_LIST = ['TESTING']

    def spoof_input(prompt=None):
        if prompt:
            print(prompt, end='')
        return input_values.pop(0)

    game_functions.input = spoof_input
    game_functions.play_game()

    out, err = capsys.readouterr()

    assert out == ''.join(['\n_  _  _  _  _  _  _ \n\nYour turn: ',
                           '\nPenalty points:  1\n\nYour turn: ',
                           '\nPenalty points:  2\n\nYour turn: ',
                           '\nPenalty points:  3\n\nYour turn: ',
                           '\nPenalty points:  4\n'
                           '\nYou are loose. Try again!'
                           '\nYou will be lucky next time!\n'
                           '\nEnter 1 to start new game\n'
                           'Enter 2 to learn the rules\n'
                           'Enter 0 to exit\n'])
    assert err == ''


def test_play_game_invalid_input(capsys):

    input_values = ['t', 'yy', 'y', 'p', 'f', 'j', '0']
    game_functions.WORDS_LIST = ['TESTING']

    def spoof_input(prompt=None):
        if prompt:
            print(prompt, end='')
        return input_values.pop(0)

    game_functions.input = spoof_input
    game_functions.play_game()

    out, err = capsys.readouterr()

    assert out == ''.join(['\n_  _  _  _  _  _  _ \n\nYour turn: ',
                           '\nT  _  _  T  _  _  _ \n\nYour turn: ',
                           'Remember! Only one letter per step!\n\nYour turn: ',
                           '\nPenalty points:  1\n\nYour turn: ',
                           '\nPenalty points:  2\n\nYour turn: ',
                           '\nPenalty points:  3\n\nYour turn: ',
                           '\nPenalty points:  4\n'
                           '\nYou are loose. Try again!'
                           '\nYou will be lucky next time!\n'
                           '\nEnter 1 to start new game\n'
                           'Enter 2 to learn the rules\n'
                           'Enter 0 to exit\n'])
    assert err == ''


@pytest.mark.parametrize('input_value,output', [
                         ('0', ''),
                         ('2', '\n1. Try to guess the word. Enter one letter per step.\n'
                               '2. If you guess correctly, you will see letters.\n'
                               '3. Else, you will get a penalty point.\n'
                               '4. Four penalty points - the game is over.\n'
                               'Good luck!\n'
                               '\nEnter 1 to start new game\n'
                               'Enter 2 to learn the rules\n'
                               'Enter 0 to exit\n'),
                         ('3', '\nNo such option!\n'
                               '\nEnter 1 to start new game\n'
                               'Enter 2 to learn the rules\n'
                               'Enter 0 to exit\n'),
                         ('g', '\nNo such option!\n'
                               '\nEnter 1 to start new game\n'
                               'Enter 2 to learn the rules\n'
                               'Enter 0 to exit\n')])
def test_option_handler(capsys, input_value, output):

    def spoof_input(prompt=None):
        if prompt:
            print(prompt, end='')
        return 0

    game_functions.input = spoof_input
    game_functions.option_handler(input_value)

    out, err = capsys.readouterr()

    assert out == output
    assert err == ''
