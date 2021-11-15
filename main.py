import pygame, sys
import numpy as np
import functions as fun
import constants as cnst

pygame.init()

def run() -> None:

    # Initialize variables
    cnst.BOARD = np.zeros((cnst.BOARD_ROWS, cnst.BOARD_COLS))
    cnst.SCREEN = fun.create_screen()

    player = 2 
    gameover = False

    # Main loop
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not gameover:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = int(mouseY // 200) # rounding up/down numbers
                clicked_col = int(mouseX // 200)

                if fun.available_square(clicked_row, clicked_col):
                    if player == 1:
                        fun.mark_square(clicked_row, clicked_col, 1)
                        if fun.check_result(player):
                            gameover = True
                        player = 2

                    elif player == 2:
                        fun.mark_square(clicked_row, clicked_col, 2)
                        if fun.check_result(player):
                            gameover = True
                        player = 1
                    
                    fun.draw_figures(cnst.SCREEN)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    gameover = False
                    player = 2
                    fun.restart(cnst.SCREEN)

        pygame.display.update()


if __name__ == "__main__":
    run()
