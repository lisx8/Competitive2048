game_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

import game, pygame
from socket import *

player_score = 0

# Networks Stuff
server_port = 8888
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('',server_port))
server_socket.listen(1)
print("Welcome to Competitive 2048!")

game_running = True
connection_socket, addr = server_socket.accept()

while game_running:
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

        print("Player 2's move! (WASD only, Q for quit) ")
        print()
        game.print_game(game_grid)

        print("Your current score: " + str(player_score))
        dir = input("Player 1's move! (WASD only, Q for quit) ")
        print()

        if (dir == 'a'):
            temp = game.move_left(game_grid)
            game_over = temp[0]
            player_score += temp[1]
            game.print_game(game_grid)
            dir = None
        elif (dir == 'd'):
            temp = game.move_right(game_grid)
            game_over = temp[0]
            player_score += temp[1]
            game.print_game(game_grid)
            dir = None
        elif (dir == 's'):
            temp = game.move_down(game_grid)
            game_over = temp[0]
            player_score += temp[1]
            game.print_game(game_grid)
            dir = None
        elif (dir == 'w'):
            temp = game.move_up(game_grid)
            game_over = temp[0]
            player_score += temp[1]
            game.print_game(game_grid)
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