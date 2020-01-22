#  ИГРА В ВИСИЛЕЦУ
#  Слова, котрые игра умеет загадывать:
#  skillfactory, testing, blackbox, pytest, unittest, coverage
#  за каждый промах - штрафное очко, 4 штрафных очка - проигрыш

from game_functions import show_menu, option_handler, LOGO


print(LOGO)
print('\nHello!')
show_menu()
option = input()
option_handler(option)
