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

clicked = False

run = True

white = (255, 255, 255)

# Storing the data of the board in a variable named board
# The board is basically a list 
board = [
    [0, 0, 0], 
    [0, 0, 0],
    [0, 0, 0]
]

winner = 0
game_over = False

pos = []

player = 1

def draw_marker():
    x_pos = 0
    for x in board:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, (50, 255, 50), (x_pos * 200 + 30, y_pos * 200 + 30), (x_pos * 200 + 170, y_pos*200 + 170), 3)
                pygame.draw.line(screen, (50, 255, 50), (x_pos * 200 + 30, y_pos * 200 + 170), (x_pos * 200 + 170, y_pos*200 + 30), 3)

            if y == -1:
                pygame.draw.circle(screen, (50, 255, 50), (x_pos * 200 + 100, y_pos * 200 + 100), 72, 3)

            y_pos += 1
        x_pos += 1


def check_winner():
    global winner
    global game_over

    y_pos = 0
    for x in board:
        # Check for columns
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -1:
            winner = 2
            game_over = True

        # Check rows

        if board[0][y_pos] + board[1][y_pos] + board[2][y_pos] == 3:
            winner = 1
            game_over = True
        if board[0][y_pos] + board[1][y_pos] + board[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1
    
    # Check cross
    if board[0][0] + board[1][1] + board[2][2] == 3 or board[2][0] + board[1][1] + board[0][2] == 3:
        winner = 1
        game_over = True
    
    if board[0][0] + board[1][1] + board[2][2] == -3 or board[2][0] + board[1][1] + board[0][2] == -3:
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

    draw_marker()


    # Checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        
        if event.type == pygame.MOUSEBUTTONUP and clicked:
            clicked = False
            pos = pygame.mouse.get_pos()
            cell_x = pos[0]
            cell_y = pos[1]
            if board[cell_x // 200][cell_y//200] == 0:
                board[cell_x // 200][cell_y//200] = player
                player *= -1
                check_winner()
            
            print(pos)

    
    pygame.display.update()


pygame.quit()

