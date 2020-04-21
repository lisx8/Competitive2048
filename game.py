import random

# Array holding the values for the random tiles that are generated after each move. Since there is a higher chance
# of getting a 2 than a 4, there are more 2s than 4s in the array.
generate_values = [2, 2, 4, 2, 2]

# Prints game to console
def print_game(game_grid):
    for i in range(0, 4):
        print(game_grid[i])

    print()

def check_game_status(game_grid):
    # Checks if any location on the game grid is empty, which automatically means that the game is not over.
    for i in range(0, 4):
        for j in range(0, 4):
            if game_grid[i][j] == 0:
                return False

    # If no spots are empty, all tiles that can move must therefore be right beside each other.
    # Checks to see if any neighboring tiles can combine. Since if tile (2,1) can combine with (2,2) then vice versa
    # must hold, and it's only necessary to check the right and bottom neighbor of each tile.
    for i in range(0, 3):
        for j in range(0, 3):
            if((game_grid[i][j] == game_grid[i][j + 1]) or (game_grid[i][j] == game_grid[i + 1][j])):
                return False

    # Checks the last column's bottom neighbors individually, since this is never checked in the previous for loop.
    for i in range(0, 3):
        if (game_grid[i][3] == game_grid[i + 1][3]):
            return False

    return True

# Generates a random new tile, either 2 or 4, in a random empty location, with 2 being more likely.
def random_new_tile(game_grid):
    new_value = random.choice(generate_values)

    # Finds all array values for where the tile == 0, stores their (x, y) coordinates, then randomly chooses
    # one of these locations to hold the newly generated tile.
    empty_tiles = []

    for i in range(0, 4):
        for j in range(0, 4):
            if game_grid[i][j] == 0:
                temp = [i, j]
                empty_tiles.append(temp)

    if (empty_tiles):
        new_location = random.choice(empty_tiles)
        game_grid[new_location[0]][new_location[1]] = new_value

def move_left(game_grid):
    moved = 0
    tot_score = 0
    def add_left(arr):
        temp = 0
        # Moves everything to the far left side of the grid.
        for x in range(0, 4):
            if (arr[0] == 0):
                if (arr[1] != 0 or arr[2] != 0 or arr[3] != 0):
                    temp += 1
                arr[0] = arr[1]
                arr[1] = arr[2]
                arr[2] = arr[3]
                arr[3] = 0

            if (arr[1] == 0):
                if (arr[2] != 0 or arr[3] != 0):
                    temp += 1
                arr[1] = arr[2]
                arr[2] = arr[3]
                arr[3] = 0

            if (arr[2] == 0):
                if (arr[3] != 0):
                    temp += 1
                arr[2] = arr[3]
                arr[3] = 0

        score = 0
        # Adds all values together if they're the same, and keeps track of the total score of this move.
        if(arr[0] == arr[1] and arr[0] != 0):
            arr[0] += arr[1]
            score = score + arr[0] + arr[1]
            arr[1] = arr[2]
            arr[2] = arr[3]
            arr[3] = 0
            temp += 1

        if(arr[1] == arr[2] and arr[1] != 0):
            arr[1] += arr[2]
            score = score + arr[1] + arr[2]
            arr[2] = arr[3]
            arr[3] = 0
            temp += 1

        if(arr[2] == arr[3] and arr[2] != 0):
            arr[2] += arr[3]
            score = score + arr[2] + arr[3]
            arr[3] = 0
            temp += 1

        return (temp, score)

    for i in range(0, 4):
        value = add_left(game_grid[i])
        moved += value[0]
        tot_score += value[1]

    if (moved):
        random_new_tile(game_grid)

    return (check_game_status(game_grid), tot_score)

def move_right(game_grid):
    moved = 0
    tot_score = 0
    def add_right(arr):
        temp = 0
        # Moves everything to the far right side of the grid.
        for x in range(0, 4):
            if (arr[3] == 0):
                if (arr[2] != 0 or arr[1] != 0 or arr[0] != 0):
                    temp += 1
                arr[3] = arr[2]
                arr[2] = arr[1]
                arr[1] = arr[0]
                arr[0] = 0

            if (arr[2] == 0):
                if (arr[1] != 0 or arr[0] != 0):
                    temp += 1
                arr[2] = arr[1]
                arr[1] = arr[0]
                arr[0] = 0

            if (arr[1] == 0):
                if (arr[0] != 0):
                    temp += 1
                arr[1] = arr[0]
                arr[0] = 0

        score = 0
        # Adds all values together if they're the same, and keeps track of the total score of this move.
        if (arr[3] == arr[2] and arr[3] != 0):
            arr[3] += arr[2]
            score = score + arr[3] + arr[2]
            arr[2] = arr[1]
            arr[1] = arr[0]
            arr[0] = 0
            temp += 1

        if (arr[2] == arr[1] and arr[2] != 0):
            arr[2] += arr[1]
            score = score + arr[2] + arr[1]
            arr[1] = arr[0]
            arr[0] = 0
            temp += 1

        if (arr[1] == arr[0] and arr[1] != 0):
            arr[1] += arr[0]
            score = score + arr[1] + arr[0]
            arr[0] = 0
            temp += 1

        return (temp, score)

    for i in range(0, 4):
        value = add_right(game_grid[i])
        moved += value[0]
        tot_score += value[1]

    if (moved):
        random_new_tile(game_grid)

    return (check_game_status(game_grid), tot_score)

def move_up(game_grid):
    moved = 0
    tot_score = 0
    def add_up(column):
        # Moves everything to the far left side of the grid.
        temp = 0
        for x in range(0, 4):
            if (game_grid[0][column] == 0):
                if ((game_grid[1][column ] != 0) or (game_grid[2][column ] != 0) or (game_grid[3][column ] != 0)):
                    temp += 1
                game_grid[0][column] = game_grid[1][column]
                game_grid[1][column] = game_grid[2][column]
                game_grid[2][column] = game_grid[3][column]
                game_grid[3][column] = 0

            if (game_grid[1][column] == 0):
                if ((game_grid[2][column ] != 0) or (game_grid[3][column ] != 0)):
                    temp += 1
                game_grid[1][column] = game_grid[2][column]
                game_grid[2][column] = game_grid[3][column]
                game_grid[3][column] = 0

            if (game_grid[2][column] == 0):
                if (game_grid[3][column ] != 0):
                    temp += 1
                game_grid[2][column] = game_grid[3][column]
                game_grid[3][column] = 0

        score = 0
        # Adds all values together if they're the same, and keeps track of the total score of this move.
        if (game_grid[0][column] == game_grid[1][column] and game_grid[0][column] != 0):
            game_grid[0][column] += game_grid[1][column]
            score = score + game_grid[0][column] + game_grid[1][column]
            game_grid[1][column] = game_grid[2][column]
            game_grid[2][column] = game_grid[3][column]
            game_grid[3][column] = 0
            temp += 1

        if (game_grid[1][column] == game_grid[2][column] and game_grid[1][column] != 0):
            game_grid[1][column] += game_grid[2][column]
            score + score + game_grid[1][column] + game_grid[2][column]
            game_grid[2][column] = game_grid[3][column]
            game_grid[3][column] = 0
            temp += 1

        if (game_grid[2][column] == game_grid[3][column] and game_grid[2][column] != 0):
            game_grid[2][column] += game_grid[3][column]
            score = score + game_grid[2][column] + game_grid[3][column]
            game_grid[3][column] = 0
            temp += 1

        return (temp, score)

    for i in range(0, 4):
        value = add_up(i)
        moved += value[0]
        tot_score += value[1]

    if (moved):
        random_new_tile(game_grid)

    return (check_game_status(game_grid), tot_score)

def move_down(game_grid):
    moved = 0
    tot_score = 0
    def add_down(column):
        temp = 0
        # Moves everything to the far bottom side of the grid
        for x in range(0, 4):
            if (game_grid[3][column] == 0):
                if ((game_grid[2][column] != 0) or (game_grid[1][column] != 0) or (game_grid[0][column] != 0)):
                    temp += 1
                game_grid[3][column] = game_grid[2][column]
                game_grid[2][column] = game_grid[1][column]
                game_grid[1][column] = game_grid[0][column]
                game_grid[0][column] = 0

            if (game_grid[2][column] == 0):
                if ((game_grid[1][column] != 0) or (game_grid[0][column] != 0)):
                    temp += 1
                game_grid[2][column] = game_grid[1][column]
                game_grid[1][column] = game_grid[0][column]
                game_grid[0][column] = 0

            if (game_grid[1][column] == 0):
                if (game_grid[0][column] != 0):
                    temp += 1
                game_grid[1][column] = game_grid[0][column]
                game_grid[0][column] = 0

        score = 0
        # Adds all values together if they're the same, and keeps track of the total score of this move.
        if (game_grid[3][column] == game_grid[2][column] and game_grid[3][column] != 0):
            game_grid[3][column] += game_grid[2][column]
            score = score + game_grid[3][column] + game_grid[2][column]
            game_grid[2][column] = game_grid[1][column]
            game_grid[1][column] = game_grid[0][column]
            game_grid[0][column] = 0
            temp += 1

        if (game_grid[2][column] == game_grid[1][column] and game_grid[2][column] != 0):
            game_grid[2][column] += game_grid[1][column]
            score = score + game_grid[2][column] + game_grid[1][column]
            game_grid[1][column] = game_grid[0][column]
            game_grid[0][column] = 0
            temp += 1

        if (game_grid[1][column] == game_grid[0][column] and game_grid[1][column] != 0):
            game_grid[1][column] += game_grid[0][column]
            score = score + game_grid[1][column] + game_grid[0][column]
            game_grid[0][column] = 0
            temp += 1

        return (temp, score)

    for i in range(0, 4):
        value = add_down(i)
        moved += value[0]
        tot_score += value[1]

    if (moved):
        random_new_tile(game_grid)

    return (check_game_status(game_grid), tot_score)

past_yell = (255, 255, 216) # https://www.schemecolor.com/pastel-world-color-palette.php
past_oran = (255, 221, 170) # https://www.schemecolor.com/pastel-orange-with-cream.php
past_grn = (224, 254, 254) # https://www.schemecolor.com/pastel-world-color-palette.php
past_mint = (170, 240, 210) # https://www.schemecolor.com/pastel-blues-and-mint.php
past_aqua = (91, 200, 178) # https://www.schemecolor.com/blue-green-pastels.php
past_blue = (211, 238, 255) # https://www.schemecolor.com/pastel-world-color-palette.php
past_cob = (141, 182, 217) # https://www.schemecolor.com/pastel-blues-and-mint.php
past_grey = (222, 226, 217) # https://www.schemecolor.com/pastel-bouquet-color-palette.php
past_pink = (244, 173, 198) # https://www.schemecolor.com/very-nice.php
past_lave = (245, 225, 253) # https://www.schemecolor.com/pastel-purple-dream-color-combination.php
past_purp = (179, 153, 212)
past_red = (255, 154, 162) # https://www.schemecolor.com/pastel-infinity-stones.php

def find_color(x, y, game_grid):
    if (game_grid[x][y] == 0):
        return past_yell
    elif (game_grid[x][y] == 2):
        return past_oran
    elif (game_grid[x][y] == 4):
        return past_grn
    elif (game_grid[x][y] == 8):
        return past_mint
    elif (game_grid[x][y] == 16):
        return past_aqua
    elif (game_grid[x][y] == 32):
        return past_blue
    elif (game_grid[x][y] == 64):
        return past_cob
    elif (game_grid[x][y] == 128):
        return past_grey
    elif (game_grid[x][y] == 256):
        return past_lave
    elif (game_grid[x][y] == 512):
        return past_pink
    elif (game_grid[x][y] == 1024):
        return past_purp
    elif (game_grid[x][y] >= 2048):
        return past_red