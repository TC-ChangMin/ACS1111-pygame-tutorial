# Example 2

# Import and initialize pygame
import pygame
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    # self.surf = pygame.Surface((width, height))
    # self.surf.fill((255, 0, 255))
    self.surf = pygame.image.load(image)
    self.x = x
    self.y = y

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

# Make an instance of GameObject
# box = GameObject(120, 300, 50, 50)
apple = GameObject(120, 300, 'images/apple.png')

# Create the game loop
running = True
while running:
    # Look at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw the box
    # box.render(screen)
    apple.render(screen)
    
    # Update the window
    pygame.display.flip()
