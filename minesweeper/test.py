import minesweeper as ms

HEIGHT = 3
WIDTH = 3
MINES = 5

# Colors
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
WHITE = (255, 255, 255)

game = ms.Minesweeper(height=HEIGHT, width=WIDTH, mines=MINES)
game.print()
move = ms.MinesweeperAI()
print(game.is_mine((0,0)))
print("Minesweeper().mines: " + str(game.mines))
print("MinesweeperAI().mines: " + str(move.mines))
# check Knowledge known_mines
know = ms.Sentence(((1,1),(0,1),(0,2)), 1)
print(know)
print(know.known_safes())
# print(move.mines)