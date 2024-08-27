# Importing pygame
import pygame

# Initializing pygame
pygame.init()

# Defining screen width and height
WIDTH, HEIGHT = 600, 600

# Creating the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Changing the title of the game window
pygame.display.set_caption("Tic-Tac-Toe")

font = pygame.font.SysFont(None, 80)

clicked = False

run = True

white = (255, 255, 255)

green = (50, 255, 50)

player = 1

draw = False

winner = 0
game_over = False

# Storing the data of the board in a variable named board
# The board is basically a list 
board = [
    [0, 0, 0], 
    [0, 0, 0],
    [0, 0, 0]
]


def check_draw():

    global draw
    global game_over

    if not game_over:

        if 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
            if winner == 0:
                draw = True
                game_over = True


def display_draw_text():
    draw_text = "Its a Draw!"
    draw_img = font.render(draw_text, True, (0, 0, 255))
    screen.blit(draw_img, (140, 270))


def draw_winning_text(winner):

    win_text = f"Player {winner} WON!"
    winner_image = font.render(win_text, True, (0, 0, 255))
    screen.blit(winner_image, (140, 270))

def draw_markers():
    x_pos = 0
    for list in board:
        y_pos = 0
        for element in list:
            if element == 1:
                pygame.draw.line(screen, (50, 255, 50), (x_pos * 200 + 30, y_pos * 200 + 30), (x_pos * 200 + 170, y_pos*200 + 170), 3)
                pygame.draw.line(screen, (50, 255, 50), (x_pos * 200 + 30, y_pos * 200 + 170), (x_pos * 200 + 170, y_pos*200 + 30), 3)
            
            if element == -1:
                pygame.draw.circle(screen, (50, 255, 50), (x_pos * 200 + 100, y_pos * 200 + 100), 72, 3)

            y_pos += 1
        x_pos += 1


def check_winner():

    global winner
    global game_over

    y_pos = 0
    for list in board:

        # Checking for each row
        if sum(list) == 3:
            winner = 1
            game_over = True
        if sum(list) == -3:
            winner = 2
            game_over = True

        # Checking for each column

        if board[0][y_pos] + board[1][y_pos] + board[2][y_pos] == 3:
            winner = 1
            game_over = True
        if board[0][y_pos] + board[1][y_pos] + board[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1
    
    # Checking the diagonal 
    if board[0][0] + board[1][1] + board[2][2] == 3 or board[0][2] + board[1][1] + board[2][0] == 3:
        winner = 1
        game_over = True
    
    if board[0][0] + board[1][1] + board[2][2] == -3 or board[0][2] + board[1][1] + board[2][0] == -3:
        winner = 2
        game_over = True




# Creating the game loop
while run:

    # Changing the color of the screen to white using the .fill() method
    screen.fill(white)

    # Drawing the vertical lines of the tic tac toe board
    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (400, 0), (400, 600), 5)

    # Drawing the horizontal lines of the tic tac toe board
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (600, 200), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 400), (600, 400), 5)

    draw_markers()

    # Checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if game_over == 0:
            
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True

            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                print(pos)
                
                x = pos[0]
                y = pos[1]

                x_pos = x // 200
                y_pos = y // 200

                if board[x_pos][y_pos] == 0:
                    board[x_pos][y_pos] = player
                    player *= -1
                    check_winner()
                    check_draw()
    
    if game_over == True:
        if draw == True:
            display_draw_text()
        else:
            draw_winning_text(winner)
    
    pygame.display.update()


pygame.quit()

