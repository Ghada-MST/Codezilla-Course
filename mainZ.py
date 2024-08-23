import os


def clear_screen():
  return "cls" if os.name == 'nt' else 'clear'


class Player:

  def __init__(self):
    self.symbol = ""
    self.name = ""

  def choose_name(self):
    while True:
      name = input("Enter your name (letters only): ")
      if name.isalpha():
        self.name = name.title()
        break
      print("Invalid choice, please enter your name in letters only")

  def choose_symbol(self):
    while True:
      symbol = input(f"{self.name}, choose your symbol (one letter only): ")
      if symbol.isalpha() and len(symbol) == 1:
        self.symbol = symbol.upper()
        break
      print("Invalid choice")


class Menu:

  def display_main_menu(self):
    message = """Welcome to Tic Tac Toe
1.Press one to begin the game
2. Press two to quit the game
"""
    choice = input(message)
    return choice

  def display_endgame_menu(self):
    message = """Game over
1.Press one to restart the game
2.Press two to exit the game"""
    choice = input(message)
    return choice


class Board:

  def __init__(self):
    self.board = [str(i) for i in range(1, 10)]

  def display_board(self):
    for i in range(0, 9, 3):
      print("|".join(self.board[i:i + 3]))
      if i < 6:
        print('-' * 5)

  def update_board(self, symbol, choice):
    if self.is_valid_move(choice):
      self.board[choice - 1] = symbol
      return True
    return False

  def is_valid_move(self, choice):
    return self.board[choice - 1].isdigit()

  def reset_board(self):
    self.board = [str(i) for i in range(1, 10)]


class Game:

  def __init__(self):
    self.board = Board()
    self.players = [Player(), Player()]
    self.menu = Menu()
    self.current_player_index = 0

  def start_game(self):
    while True:
      choice = self.menu.display_main_menu()
      if choice == "1":
        self.setup_players()
        self.play_game()
        break
      elif choice == "2":
        self.quit_game()
        break
      else:
        print("invalid choice")

  def quit_game(self):
    print("See you next time")

  def play_game(self):
    while True:
      self.play_turn()
      if self.check_win() or self.check_draw():
        choice = self.menu.display_endgame_menu()
        if choice == "1":
          self.restart_game()
        elif choice == "2":
          self.quit_game()
          break
        else:
          raise TypeError("invalid choice, choose 1 or 2")

  def setup_players(self):
    for number, player in enumerate(self.players, 1):
      print(f"Player {number}, enter your details: ")
      player.choose_name()
      player.choose_symbol()
      clear_screen()

  def switch_player(self):
    self.current_player_index = 1 - self.current_player_index

  def play_turn(self):
    player = self.players[self.current_player_index]
    self.board.display_board()
    print(f"{player.name}'s turn symbol:{player.symbol}")
    while True:
      try:
        cell_choice = int(input("Choose cell number from 1 to 9: "))
        if 1 <= cell_choice <= 9 and self.board.update_board(
            player.symbol, cell_choice):
          break
        else:
          print("Invalid mve, try again")
      except ValueError:
        print("Please enter numbers between 1 and 9")
    self.switch_player()

  def restart_game(self):
    self.board.reset_board()
    self.current_palyer_index = 0
    self.play_game()

  def check_win(self):
    win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                        [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combo in win_combinations:
      if (self.board.board[combo[0]] == self.board.board[combo[1]] ==
          self.board.board[combo[2]]):
        return True
    return False

  def check_draw(self):
    return all(not cell.isdigit() for cell in self.board.board)


if __name__ == "__main__":
  game = Game()
  game.start_game()
