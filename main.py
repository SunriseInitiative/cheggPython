# Write your code here :-)
import pygame

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
OFFSETX, OFFSETY = 200, 100
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

print("Dimensions Initialized")

# Colors
LIGHT_COLOR = (200, 200, 200)
DARK_COLOR = (100, 100, 100)
BLUE_TINT = (100, 150, 200)
ORANGE_TINT = (200, 150, 100)

print("Colors Initialized")

# Create the display
screen = pygame.display.set_mode((WIDTH * 2, HEIGHT * 2))
pygame.display.set_caption("8x8 Board")

print("Display Active")

def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 0:
                color = LIGHT_COLOR
            else:
                color = DARK_COLOR
            
            # Apply tint
            if row < 2:
                color = tuple(min(255, c + 50) for c in BLUE_TINT) if (row + col) % 2 == 0 else BLUE_TINT
            elif row >= 6:
                color = tuple(min(255, c + 50) for c in ORANGE_TINT) if (row + col) % 2 == 0 else ORANGE_TINT
            
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_board()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
