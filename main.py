import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Car Racing Game')

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Load car image
car_img = pygame.image.load('car.png')
car_width = 73
car_height = 82

# Function to draw the car on the display
def draw_car(x, y):
    game_display.blit(car_img, (x, y))

# Function to display a message
def display_message(text, font_size):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.center = (display_width/2, display_height/2)
    game_display.blit(text_surface, text_rect)

# Function to check collision
def check_collision(car_x, car_y, obstacle_x, obstacle_y, obstacle_width, obstacle_height):
    if car_y < obstacle_y + obstacle_height:
        if car_x > obstacle_x and car_x < obstacle_x + obstacle_width or car_x + car_width > obstacle_x and car_x + car_width < obstacle_x + obstacle_width:
            return True
    return False

# Main game loop
def game_loop():
    # Initial car position
    car_x = display_width * 0.45
    car_y = display_height * 0.8

    # Car movement speed
    car_speed = 0

    # Obstacle variables
    obstacle_width = 100
    obstacle_height = 100
    obstacle_x = random.randrange(0, display_width - obstacle_width)
    obstacle_y = -600
    obstacle_speed = 7

    # Game over flag
    game_over = False

    # Clock object to control frame rate
    clock = pygame.time.Clock()

    # Game loop
    while not game_over:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_speed = -5
                elif event.key == pygame.K_RIGHT:
                    car_speed = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    car_speed = 0

        # Update car position
        car_x += car_speed

        # Update obstacle position
        obstacle_y += obstacle_speed

        # Clear the display
        game_display.fill(black)

        # Draw the car and obstacle
        draw_car(car_x, car_y)
        pygame.draw.rect(game_display, red, [obstacle_x, obstacle_y, obstacle_width, obstacle_height])

        # Check for collision
        if check_collision(car_x, car_y, obstacle_x, obstacle_y, obstacle_width, obstacle_height):
            game_over = True

        # Check if obstacle went off the screen
        if obstacle_y > display_height:
            obstacle_y = 0 - obstacle_height
            obstacle_x = random.randrange(0, display_width - obstacle_width)

        # Update the display
        pygame.display.update()

        # Set the frame rate
        clock.tick(60)

    # Display game over message
    display_message("Game Over", 90)
    pygame.display.update()

    # Wait for 2 seconds before quitting
    pygame.time.wait(2000)

    # Quit the game
    pygame.quit()
    quit()

# Start the game
game_loop()
