import pygame

# Initialize Pygame
pygame.init()

# Define the screen size (800x800 for an 8x8 grid)
screen = pygame.display.set_mode((800, 800))

# Set colors for the chessboard squares
white = (255, 255, 255)
black = (0, 0, 0)

# Draw the chessboard
def draw_chessboard():
    square_size = 100  # Each square will be 100x100 pixels
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, white, pygame.Rect(col * square_size, row * square_size, square_size, square_size))
            else:
                pygame.draw.rect(screen, black, pygame.Rect(col * square_size, row * square_size, square_size, square_size))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_chessboard()
    pygame.display.flip()

pygame.quit()
