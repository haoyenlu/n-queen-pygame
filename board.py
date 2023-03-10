import pygame

class Board:
    def __init__(self,n,block_size):
        self.n = n
        self.block_size = block_size

        self.surface = pygame.Surface((block_size*n,block_size*n))
        self.board_rect = [[0 for _ in range(n)] for _ in range(n)]
        self.init_board()

        self.queen = []

    
    def init_board(self):
        for i in range(self.n):
            for j in range(self.n):
                x = i * self.block_size
                y = j * self.block_size
                self.board_rect[i][j] = pygame.Rect(x,y,self.block_size,self.block_size)
                if (i + j) % 2 == 0:
                    pygame.draw.rect(self.surface,(255,255,255),self.board_rect[i][j],0)
                else:
                    pygame.draw.rect(self.surface,(125,125,125),self.board_rect[i][j],0)

    
    def place_queen(self,row,col):
        q = Queen(self.block_size)
        q.place(self.board_rect[col][row].center)
        self.queen.append(q)

    def remove_queen(self,row,col):
        self.queen[:] = [q for q in self.queen if q.rect.center != self.board_rect[col][row].center]
        color = (255,255,255) if (row+col)%2 == 0 else (125,125,125)
        pygame.draw.rect(self.surface,color,self.board_rect[col][row],0)


    
    def update(self):
        for q in self.queen:
            q.draw(self.surface)


class Queen:
    def __init__(self,block_size):
        self.image = pygame.image.load("queen.png")
        self.image = pygame.transform.smoothscale(self.image,(block_size,block_size))
        self.rect = self.image.get_rect()
    
    def place(self,position):
        self.rect.center = position

    def draw(self,surface):
        surface.blit(self.image,self.rect)

