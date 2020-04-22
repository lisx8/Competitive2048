game_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

import game, pygame
from socket import *

black = (0, 0, 0)
white = (255,255, 255)
orange = (255, 178, 102)

pygame.init()

game_width = 800
game_height = 1000

x_locations = [0, 200, 400, 600]
y_locations = [200, 400, 600, 800]
rec_width = 200

gameDisplay = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption('2048!')
gameDisplay.fill(white) # fills the window with white
myFont = pygame.font.SysFont('Comic Sans MS', 32) # haha
mySurface = pygame.Surface((800, 1000)) # makes a new surface on which to draw things
mySurface.fill(orange) # fills the new surface with oranges
gameDisplay.blit(mySurface, (0, 0)) # smacks the new surface, mySurface, onto the screen
pygame.display.update()

# Generates 2 random tiles for a new game.
#game.random_new_tile(game_grid)
#game.random_new_tile(game_grid)

'''def draw_text(x, y, game_over):
    if (game_over):
        more_words = myFont.render("GAME OVER!", True, black)
        gameDisplay.blit(more_words, ((y) * 200, (x + 1) * 200))
        pygame.display.update()
        return

    words = myFont.render(str(game_grid[x][y]), True, black)
    gameDisplay.blit(words, ((y) * 200, (x + 1) * 200))
    pygame.display.update()

def draw_rect(x, y, value, color):
    rectangle = pygame.Rect(x_locations[y], y_locations[x], rec_width, rec_width) # i can't be assed to figure out why x and y are backwards
    rec = pygame.draw.rect(mySurface, color, rectangle) # Change color value to the corresponding num value
    gameDisplay.blit(mySurface, (0, 0))
    pygame.display.update()

def draw_board(game_over):
    for i in range(0, 4):
        for j in range(0 ,4):
            color = game.find_color(i, j, game_grid)
            draw_rect(i, j, game_grid[i][j], color)

    for i in range(0, 4):
        for j in range(0, 4):
            draw_text(j, i, game_over)'''

# Draws the initial board with the two first tiles.
#draw_board(False)
#pygame.display.update()

server_port = 8888
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('',server_port))
server_socket.listen(1)
print("Welcome to Fuck Your 2048!")

turn = True # while it is still the server player's turn

while True:
    connection_socket, addr = server_socket.accept()
    encoded_grid = connection_socket.recv(1024)
    decoded_grid = encoded_grid.decode()
    array = decoded_grid.split(',')
    counter = 0

    for i in range(0, 4):
        for j in range(0, 4):
            game_grid[i][j] = int(array[counter])
            counter += 1

    game.print_game(game_grid)

    while turn:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game_over = game.move_left(game_grid)
                    game.print_game(game_grid)
                    print("left")
                    # draw_board(game_over)
                    turn = False

                elif event.key == pygame.K_RIGHT:
                    game_over = game.move_right(game_grid)
                    game.print_game(game_grid)
                    # draw_board(game_over)
                    print("right'")
                    turn = False

                elif event.key == pygame.K_DOWN:
                    game_over = game.move_down(game_grid)
                    game.print_game(game_grid)
                    # draw_board(game_over)
                    print("down")
                    turn = False

                elif event.key == pygame.K_UP:
                    game_over = game.move_up(game_grid)
                    game.print_game(game_grid)
                    # draw_board(game_over)
                    print("up")
                    turn = False

                elif event.key == pygame.K_q:
                    print("QUIT")
                    pygame.quit()
                    game_running = False
                    quit()
        pygame.display.update()

    list_grid = []
    for i in range(0, 4):
        for j in range(0, 4):
            list_grid.append(str(game_grid[i][j]))
    #change game_grid to a string separated by commas, encode it, send it back to client

    encode_grid = ','.join(list_grid)
    connection_socket.send(encode_grid.encode()) # for some reason it only kinda works when i don't have the .encode() bit
    connection_socket.close()

'''game_running = True
while game_running:
    connect_socket, addr = server_socket.accept()
    game_grid = connect_socket.recv(1024)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game_over = game.move_left(game_grid)
                game.print_game(game_grid)
                print()
                #draw_board(game_over)

            elif event.key == pygame.K_RIGHT:
                game_over = game.move_right(game_grid)
                game.print_game(game_grid)
                #draw_board(game_over)
                print()

            elif event.key == pygame.K_DOWN:
                game_over = game.move_down(game_grid)
                game.print_game(game_grid)
                #draw_board(game_over)
                print()

            elif event.key == pygame.K_UP:
                game_over = game.move_up(game_grid)
                game.print_game(game_grid)
                #draw_board(game_over)
                print()

            elif event.key == pygame.K_q:
                print("QUIT")
                pygame.quit()
                game_running = False
                quit()

game_running = True
while game_running:
    connect_socket, addr = server_socket.accept()
    game_grid = connect_socket.recv(1024)
    connect_socket.send(game_grid)
    connect_socket.close()'''