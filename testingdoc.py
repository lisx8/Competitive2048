game_grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

'''import pygame, game

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

X = 400
Y = 400

text = ["banana", "boing", "boy"]

display_surface = pygame.display.set_mode((X, Y ))
pygame.display.set_caption('Show Text')
#font = pygame.font.Font('freesansbold.ttf', 32)
display_surface.fill(white)

#create a new Surface
myNewSurface = pygame.Surface((500, 300))

#change its background color
myNewSurface.fill((55,155,255))

#blit myNewSurface onto the main screen at the position (0, 0)
display_surface.blit(myNewSurface, (0, 0))

#update the screen to display the changes
pygame.display.update() #or  display.flip()

def get_rekt(x, y, width, color):
    for i in range(0, 6):
        rectangle = pygame.Rect(i*(x+1), i*(y+1), width, width)
        rec = pygame.draw.rect(myNewSurface, color, rectangle)  # Change color value to the corresponding num value
        display_surface.blit(myNewSurface, (0, 0))
        pygame.display.update()

while True:
    for event in pygame.event.get():
        print("are we here yet")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.print_game(game_grid)
            elif event.key == pygame.K_RIGHT:
                print("huhdfkjshf")

        for i in range(0, 3):
            temp = text[i]
            words = font.render(temp, True, green)
            textRect = words.get_rect()
            textRect.center = (i*200 // 2+100, i*200 // 2+100)
            display_surface.blit(words, textRect)
            pygame.display.update()'''

import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

pygame.init()
# Create a game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Set title
pygame.display.set_caption("UKDevGuy tutorial")
game_running = True
# Game loop
while game_running:
    # Loop through all active events
    for event in pygame.event.get():
        # Control character movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("Move the character forwards")
            elif event.key == pygame.K_s:
                print("Move the character backwards")
            elif event.key == pygame.K_a:
                print("Move the character left")
            elif event.key == pygame.K_d:
                print("Move the character right")

    # Content here
    # Update our display
    #pygame.display.update()

# Uninitialize all pygame modules and quit the program
pygame.quit()
quit()