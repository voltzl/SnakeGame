import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Set the width and height of the game window
window_width = 800
window_height = 600

# Set the size of each grid cell and the initial snake speed
cell_size = 20
snake_speed = 15

# Create the game window
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Clock object to control the game speed
clock = pygame.time.Clock()

# Define the font for displaying the score
font = pygame.font.SysFont(None, 48)

def show_score(score):
    score_surface = font.render('Score: ' + str(score), True, white)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (window_width / 2,  10)
    game_window.blit(score_surface, score_rect)

def game_over():
    game_over_surface = font.render('Game Over', True, white)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_width / 2, window_height / 2)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

def run_game():
    # Initialize the snake
    snake_position = [[100, 50], [90, 50], [80, 50]]
    snake_body = 3
    direction = 'RIGHT'

    # Initialize the food
    food_position = [random.randrange(1, (window_width // cell_size)) * cell_size,
                     random.randrange(1, (window_height // cell_size)) * cell_size]
    food_spawn = True

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    direction = 'RIGHT'
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    direction = 'LEFT'
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    direction = 'UP'
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    direction = 'DOWN'

        # Update snake position
        if direction == 'RIGHT':
            snake_position[0][0] += cell_size
        elif direction == 'LEFT':
            snake_position[0][0] -= cell_size
        elif direction == 'UP':
            snake_position[0][1] -= cell_size
        elif direction == 'DOWN':
            snake_position[0][1] += cell_size

        # Check for snake-food collision
        if snake_position[0] == food_position:
            food_spawn = False
            snake_body += 1

        # Spawn new food
        if not food_spawn:
            food_position = [random.randrange(1, (window_width // cell_size)) * cell_size,
                             random.randrange(1, (window_height // cell_size)) * cell_size]
        food_spawn = True

        # Clear the game window
        game_window.fill
