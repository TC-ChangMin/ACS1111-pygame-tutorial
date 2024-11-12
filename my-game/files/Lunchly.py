import pygame
from random import randint, choice
from files.GameObject import GameObject
from files.Lanes import lanes

class Lunchly(GameObject):
  def __init__(self):
    super(Lunchly, self).__init__(0, 0, 'images/lunchly.png')
    self.original_image = pygame.image.load('images/lunchly.png')
    self.flipped_image = pygame.transform.flip(self.original_image, True, False)  # Flip horizontally
    self.surf = self.original_image  
    self.dx = 0 
    self.dy = 0  
    self.reset()

  def move(self):
    super().move()
    if self.dy > 0: 
      self.surf = self.flipped_image
    else:  
      self.surf = self.original_image

    if self.y > 500 or self.y < -64: 
      self.reset()

  def reset(self):
    self.x = choice(lanes)
    direction = randint(0, 1) 
    
    if direction == 0: 
      self.y = 500  
      self.dy = -((randint(0, 200) / 100) + 1)  
    else: 
      self.y = -64 
      self.dy = (randint(0, 200) / 100) + 1  
    
    self.surf = self.original_image 
# ----------------------------------------------