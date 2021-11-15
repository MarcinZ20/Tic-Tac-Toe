import constants as cnst, pygame


def create_screen() -> pygame.Surface:
    screen = pygame.display.set_mode((cnst.WIDTH, cnst.HEIGHT))
    screen.fill(cnst.BACKGROUND_DARK)
    pygame.display.set_caption("TIC-TAC-TOE")
    grid(screen)

    return screen


def grid(screen: pygame.Surface) -> None:
    pygame.draw.line(screen, cnst.LINE_LIGHT, (200, 0), (200, 600), 10)
    pygame.draw.line(screen, cnst.LINE_LIGHT, (400, 0), (400, 600), 10)
    pygame.draw.line(screen, cnst.LINE_LIGHT, (0, 200), (600, 200), 10)
    pygame.draw.line(screen, cnst.LINE_LIGHT, (0, 400), (600, 400), 10)


def mark_square(row: int, col: int, player: int) -> None:
    cnst.BOARD[row][col] = player


def available_square(row: int, col: int) -> bool:
    return cnst.BOARD[row][col] == 0


def is_board_full() -> bool:
    for row in range(cnst.BOARD_ROWS):
        for col in range(cnst.BOARD_COLS):
            if cnst.BOARD[row][col] == 0: 
                return False
    return True


def draw_figures(screen: pygame.Surface):
    for row in range(cnst.BOARD_ROWS):
        for col in range(cnst.BOARD_COLS):
            if cnst.BOARD[row][col] == 1:
                pygame.draw.circle(screen, cnst.CIRCLE_GREEN, (int(col * 200 + 100), int(row * 200 + 100)), cnst.CIRCLE_RADIUS, cnst.CIRCLE_WIDTH)
            
            elif cnst.BOARD[row][col] == 2:
                pygame.draw.line(screen, cnst.CROSS_RED, (col * 200 + cnst.SPACE, row * 200 + 200 - cnst.SPACE), (col * 200 + 200 - cnst.SPACE, row * 200 + cnst.SPACE), 15)
                pygame.draw.line(screen, cnst.CROSS_RED, (col * 200 + cnst.SPACE, row * 200 + cnst.SPACE), (col * 200 + 200 - cnst.SPACE, row * 200 + 200 - cnst.SPACE), 15)


def check_result(player: int) -> bool:

    for col in range(cnst.BOARD_COLS):
        if cnst.BOARD[0][col] == player and cnst.BOARD[1][col] == player and cnst.BOARD[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    
    for row in range(cnst.BOARD_ROWS):
        if cnst.BOARD[row][0] == player and cnst.BOARD[row][1] == player and cnst.BOARD[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    if cnst.BOARD[0][0] == player and cnst.BOARD[1][1] == player and cnst.BOARD[2][2] == player:
        draw_dsc_diagonal_winning_line(player)
        return True

    if cnst.BOARD[0][2] == player and cnst.BOARD[1][1] == player and cnst.BOARD[2][0] == player:
        draw_asc_diagonal_winning_line(player) 
        return True
    
    return False


def draw_vertical_winning_line(col: int, player: int) -> None:
    posX = col * 200 + 100
    if player == 1:
        color = cnst.CIRCLE_GREEN
    elif player == 2:
        color = cnst.CROSS_RED

    pygame.draw.line(cnst.SCREEN, color, (posX, 15), (posX, cnst.HEIGHT - 15), 15)


def draw_horizontal_winning_line(row: int, player: int) -> None:
    posY = row * 200 + 100

    if player == 1:
        color = cnst.CIRCLE_GREEN
    elif player == 2:
        color = cnst.CROSS_RED

    pygame.draw.line(cnst.SCREEN, color, (15, posY), (cnst.WIDTH - 15, posY), 15)


def draw_asc_diagonal_winning_line(player: int) -> None:
    if player == 1:
        color = cnst.CIRCLE_GREEN
    elif player == 2:
        color = cnst.CROSS_RED

    pygame.draw.line(cnst.SCREEN, color, (15, cnst.HEIGHT - 15), (cnst.WIDTH - 15, 15), 15)


def draw_dsc_diagonal_winning_line(player: int) -> None:
    if player == 1:
        color = cnst.CIRCLE_GREEN
    elif player == 2:
        color = cnst.CROSS_RED

    pygame.draw.line(cnst.SCREEN, color, (15, 15), (cnst.WIDTH - 15, cnst.HEIGHT - 15), 15)


def reset_board() -> None:
    for row in range(cnst.BOARD_ROWS):
        for col in range(cnst.BOARD_COLS):
            cnst.BOARD[row][col] = 0


def restart(screen: pygame.Surface) -> None:
    screen.fill(cnst.BACKGROUND_DARK)
    grid(screen) 
    reset_board()
