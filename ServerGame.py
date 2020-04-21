game_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

import game, pygame
from socket import *

'''# Pygame Stuff

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

def draw_text(x, y, game_over):
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

# Networks Stuff
server_port = 8888
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('',server_port))
server_socket.listen(1)
print("Welcome to Fuck Your 2048!")

game_running = True
connection_socket, addr = server_socket.accept()

while game_running:
    pygame.event.pump()
    encoded_grid = connection_socket.recv(1024)
    decoded_grid = encoded_grid.decode()

    if(decoded_grid == 'q'):
        game_running = False
        print("QUIT")
    else:
        array = decoded_grid.split(',')
        counter = 0
        game_over = False

        for i in range(0, 4):
            for j in range(0, 4):
                game_grid[i][j] = int(array[counter])
                counter += 1

        game.print_game(game_grid)
        #draw_board(game_over)

        dir = input("What's your move, motherfucker? (WASD only, Q for quit)")

        if (dir == 'a'):
            game_over = game.move_left(game_grid)
            game.print_game(game_grid)
            #draw_board(game_over)
            dir = None
        elif (dir == 'd'):
            game_over = game.move_right(game_grid)
            game.print_game(game_grid)
            #draw_board(game_over)
            dir = None
        elif (dir == 's'):
            game_over = game.move_down(game_grid)
            game.print_game(game_grid)
            #draw_board(game_over)
            dir = None
        elif (dir == 'w'):
            game_over = game.move_up(game_grid)
            game.print_game(game_grid)
            #draw_board(game_over)
            dir = None
        elif (dir == 'q'):
            print("QUIT")
            connection_socket.send(dir.encode())
            game_running = False

        list_grid = []
        for i in range(0, 4):
            for j in range(0, 4):
                list_grid.append(str(game_grid[i][j]))

        encode_grid = ','.join(list_grid)
        connection_socket.send(encode_grid.encode())

connection_socket.close()