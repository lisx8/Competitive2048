game_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

import game #, pygame
from socket import *

player_score = 0
clear_power = 3
pass_power = 3

# Generates 2 random tiles for a new game.
game.random_new_tile(game_grid)
game.random_new_tile(game_grid)

server_name = '192.168.2.16'
server_port = 8888
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name,server_port))

print("Welcome to Competitive 2048, Player 2!")
print()

game_running = True

while game_running:
    if(dir != 'p'):
        list_grid = []
        for i in range(0, 4):
            for j in range(0, 4):
                list_grid.append(str(game_grid[i][j]))

        encode_grid = ','.join(list_grid)
        client_socket.send(encode_grid.encode())
        encoded_grid = client_socket.recv(1024)
        decoded_grid = encoded_grid.decode()
    else:
        client_socket.send(dir.encode())

    if(decoded_grid == 'q'):
        game_running = False
        print("QUIT")
    elif(decoded_grid == 'p'):
        pass
    elif(decoded_grid == 'o'):
        print("Player 1 caused a game over!")
        break
    else:
        array = decoded_grid.split(',')
        counter = 0

        for i in range(0, 4):
            for j in range(0, 4):
                game_grid[i][j] = int(array[counter])
                counter = counter + 1

        print("Player 1's move! (WASD only, Q for quit) ")
        print()
        game.print_game(game_grid)

        print("Your current score: " + str(player_score))
        dir = input("Your move! (WASD only, Q for quit) ")
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
        elif (dir == 'c') and (clear_power):
            temp = game.clear_board(game_grid)
            player_score = temp[0]
            game_grid = temp[1]
            game.random_new_tile(game_grid)
            game.random_new_tile(game_grid)
            game.print_game(game_grid)
            dir = None
            clear_power -= 1
        elif (dir == 'p') and (pass_power):
            pass_power -= 1

            temp_dir = input("You forced Player 1 to pass! Your turn! (WASD only, Q for quit) ")
            print()
            if (temp_dir == 'a'):
                temp = game.move_left(game_grid)
                game_over = temp[0]
                player_score += temp[1]
                game.print_game(game_grid)
                temp_dir = None
            elif (temp_dir == 'd'):
                temp = game.move_right(game_grid)
                game_over = temp[0]
                player_score += temp[1]
                game.print_game(game_grid)
                temp_dir = None
            elif (temp_dir == 's'):
                temp = game.move_down(game_grid)
                game_over = temp[0]
                player_score += temp[1]
                game.print_game(game_grid)
                temp_dir = None
            elif (temp_dir == 'w'):
                temp = game.move_up(game_grid)
                game_over = temp[0]
                player_score += temp[1]
                game.print_game(game_grid)
                temp_dir = None

            game.print_game(game_grid)
        elif (dir == 'q'):
            print("QUIT")
            client_socket.send(dir.encode())
            game_running = False

        if(not game_over):
            continue
        else:
            client_socket.send('o'.encode())
            break

client_socket.close()