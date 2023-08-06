import pygame
from tictactoe import *
import time
board = initial_state()


pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


def draw_x_o(x_o, dim_x, dim_y):

    if(x_o=='X'):
        pygame.draw.line(screen, (0, 0, 255), (100+15+(dim_x*133.33), 100+15+(dim_y*133.33)), (233.33-15+(dim_x*133.33), 233.33-15+(dim_y*133.33)), 2)
        pygame.draw.line(screen, (0, 0, 255), (100 + 15 + (dim_x * 133.33), 233.33 - 15 + (dim_y * 133.33)),
                         (233.33 - 15 + (dim_x * 133.33), 100 + 15 + (dim_y * 133.33)), 2)

    else:
        pygame.draw.circle((screen),  (0, 0, 255), (100+(133.33*dim_x)+(133.33/2),100+(133.33*dim_y)+(133.33/2)),55,3)






def play_again():
    pygame.draw.rect(screen, (0, 0, 255),
                     [460, 530, 90, 40], 2)

def draw_grid():

    pygame.draw.line(screen, (0,0,255), (225 , 100), (225, 500), 2)
    pygame.draw.line(screen, (0, 0, 255), (375, 100), (375, 500), 2)
    pygame.draw.line(screen, (0, 0, 255), (100, 225),
                         (500, 225),2)
    pygame.draw.line(screen, (0, 0, 255), (100, 375),
                     (500, 375), 2)



def positions(x,y):
    #x = x%225
    temp = 3

    for i in range(1,4):
        if (100+(i * 133.33) > x):
            x = i
            break
    for i in range(1,4):
        if(100+(i * 133.33)>y):
            y = i
            break

    return min(x-1,temp),min(y-1,temp)


def main():
    run = True
    draw_grid()
    while run:

        #title = pygame.font.Font("OpenSans-Regular.ttf", 28).render("Play Tic Tact Toe!")


        check = False
        #play_again()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif utility(board) != 0 or terminal(board):
                check = True
                break

            elif event.type == pygame.MOUSEBUTTONDOWN and player(board)=="X":
                positionx,positiony = pygame.mouse.get_pos()
                print(positionx,positiony)
                if positionx < 100 or positionx > 500 or positiony > 500 or positiony < 100:
                    continue

                x,y = positions(positionx,positiony)

                print(positionx, positiony)


                draw_x_o(player(board), x, y)
                print(x,y)
                board[x][y] = player(board)
                #board = result(board,(x,y))

            elif player(board) == "O":

                x,y = minimax(board)

                draw_x_o(player(board), x, y)

                board[x][y] = player(board)


        if check:
            #print(board)
            print("Congrats: " + winner(board))
            break





        pygame.display.flip()

    pygame.quit()







main()