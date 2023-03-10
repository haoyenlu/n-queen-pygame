import pygame
import sys
import board



pygame.init()

try:
    n_queen = int(sys.argv[1])
except:
    print("Enter how many square of board:")
    n_queen = int(input())


block_size = 50
board_offset = (10,10)
screen_width = block_size * n_queen + 20
screen_height = block_size * n_queen + 20

screen = pygame.display.set_mode((screen_width,screen_height))


board = board.Board(n_queen,block_size)


board_list = [['.' for _ in range(n_queen)] for _ in range(n_queen)]
cols, diag, anti_diag = [False]*n_queen, [False]*(2*n_queen-1), [False]*(2*n_queen-1)
solutions = []

solving = False

def backtrack(row):
    if row == n_queen:
        solutions.append(["".join(row) for row in board_list])
        yield False
    for col in range(n_queen):
        if not cols[col] and not diag[row+col] and not anti_diag[row-col]:
            board_list[row][col] = 'Q'
            cols[col], diag[row+col], anti_diag[row-col] = True, True, True
            board.place_queen(row,col)
            yield True
            yield from backtrack(row+1)
            board_list[row][col] = '.'
            board.remove_queen(row,col)
            cols[col], diag[row+col], anti_diag[row-col] = False, False, False

bt_generator = None

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Start Algorithm")
                solving = True
                bt_generator = backtrack(0)

    
    if solving:
        try:
            result = next(bt_generator)
            if result == False:
                bt_generator.close()
        except StopIteration:
            solving = False
            print("Solved")
            print(solutions)
    
        



    screen.blit(board.surface,(board_offset))
    board.update()
    pygame.display.update()




