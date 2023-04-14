import pygame
import random

# Initialzing
pygame.init()

# define some colors that will be used in the game
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set some variables for the game window size, score, level, snake speed, and direction
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
score = 0
last_score = 0
level = 1
snake_speed = 15
direction = 'RIGHT'

# Set up a font that will be used to display text on the screen
font = pygame.font.SysFont("Verdana", 20)


# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")


# Define the Snake class && methods to move, change direction, check for collisions
class Snake:
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = 'RIGHT'

    def move(self, food_position):
        if self.direction == 'RIGHT':
            self.position[0] += 10
        elif self.direction == 'LEFT':
            self.position[0] -= 10
        elif self.direction == 'UP':
            self.position[1] -= 10
        elif self.direction == 'DOWN':
            self.position[1] += 10

        self.body.insert(0, list(self.position))

        if self.position == food_position:
            return 1
        else:
            self.body.pop()
            return 0

    def change_direction(self, new_direction):
        if new_direction == 'RIGHT' and not self.direction == 'LEFT':
            self.direction = 'RIGHT'
        elif new_direction == 'LEFT' and not self.direction == 'RIGHT':
            self.direction = 'LEFT'
        elif new_direction == 'UP' and not self.direction == 'DOWN':
            self.direction = 'UP'
        elif new_direction == 'DOWN' and not self.direction == 'UP':
            self.direction = 'DOWN'

    def check_collision(self):
        # Check if head of snake out of screen
        if self.position[0] > SCREEN_WIDTH - 10 or self.position[0] < 0:
            return 1
        elif self.position[1] > SCREEN_HEIGHT - 10 or self.position[1] < 0:
            return 1
        # Check if head of snake crossing its body
        for body_part in self.body[1:]:
            if self.position == body_part:
                return 1
        return 0

    def draw(self):
        for pos in self.body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))


# Define the Food class which contains the food's position, color, and a food's position.
class Food:
    def __init__(self):
        self.position = [0, 0]
        self.color = RED
        self.random_position()

    def random_position(self):
        self.position = [random.randrange(1, (SCREEN_WIDTH//10)) * 10,
                         random.randrange(1, (SCREEN_HEIGHT//10)) * 10]

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.position[0]+5, self.position[1]+5), 5)


# Create the Snake and Food objects
snake = Snake()
food = Food()

# Game Loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:  #to change the direction of the snake accordingly.
            if event.key == pygame.K_RIGHT:
                snake.change_direction('RIGHT')
            elif event.key == pygame.K_LEFT:
                snake.change_direction('LEFT')
            elif event.key == pygame.K_UP:
                snake.change_direction('UP')
            elif event.key == pygame.K_DOWN:
                snake.change_direction('DOWN')

    # Move the snake and check for collisions
    food_eaten = snake.move(food.position)
    if food_eaten:
        score += 1
        food = Food() #a new Food object is created, and the food variable is updated with this new object.
    if snake.check_collision():
        pygame.quit()

    # Update the screen
    screen.fill(WHITE)  # fill the screen with the background color
    snake.draw() #to draw the snake and the food on the screen.
    food.draw() #to draw the snake and the food on the screen.

    # Update the score and level
    score_text = font.render("Score: " + str(score), True, BLACK)
    level_text = font.render("Level: " + str(level), True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (SCREEN_WIDTH - level_text.get_width() - 10, 10))

    # Check if the player has passed to the next level
    if score > last_score and score % 4 == 0:
        level += 1
        snake_speed += 5
        last_score = score

    pygame.display.update()
    pygame.time.Clock().tick(snake_speed)