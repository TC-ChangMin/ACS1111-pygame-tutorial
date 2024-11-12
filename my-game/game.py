import pygame
from random import randint, choice
from files.Confusion import Explosion
from files.ST import ST
from files.Lunchly import Lunchly
from files.Prime import Prime
from files.Player import Player
from files.Sparkle import Sparkle
from files.DM import DM
from files.ScoreBoard import ScoreBoard
from files.Points import PointsSprite

pygame.init()
pygame.mixer.init()

goku_sound = pygame.mixer.Sound("audio/drippy_cheese.mp3")
rahhh_sound = pygame.mixer.Sound("audio/rahhh.mp3")
huh_sound = pygame.mixer.Sound("audio/huh.mp3")
sigma_sound = pygame.mixer.Sound("audio/sigma.mp3")

lives = 3

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Load the background image
background = pygame.image.load('images/background.png') 
background = pygame.transform.scale(background, (500, 500))
# ----------------------------------------------
def display_lives(screen, lives):
    for i in range(lives):
        screen.blit(pygame.image.load('images/lives.png'), (480 - (i + 1) * 40, 10))  # Adjust the position if needed

# Making Groups
all_sprites = pygame.sprite.Group()
fruit_sprites = pygame.sprite.Group()
explosion_sprites = pygame.sprite.Group()
dm_sprite = pygame.sprite.Group()

# Make Fruit instances
for n in range(1, 2):
  lunchly = Lunchly()
  prime = Prime()
  dm = DM()
  fruit_sprites.add(lunchly)
  fruit_sprites.add(prime)
  dm_sprite.add(dm)
  all_sprites.add(lunchly)
  all_sprites.add(prime)
  all_sprites.add(dm)

    

# Instance of Player
player = Player()

# Make enemy
enemy = ST()

# Add sprites to group
all_sprites.add(player)
all_sprites.add(enemy)

# Score
score = ScoreBoard(30, 30, 0)
all_sprites.add(score)

# Get the clock
clock = pygame.time.Clock()

def make_explosion(x, y):
  explosion = Explosion(x, y)
  explosion_sprites.add(explosion)

def make_pop(x, y):
  explosion = Sparkle(x, y)
  explosion_sprites.add(explosion)

# Create the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        player.left()
      elif event.key == pygame.K_RIGHT:
        player.right()
      elif event.key == pygame.K_UP:
        player.up()
      elif event.key == pygame.K_DOWN:
        player.down()
        
# Check for the stun event (when the timer finishes)
    if event.type == pygame.USEREVENT:
        player.un_stun()  
        pygame.time.set_timer(pygame.USEREVENT, 0)  

  # Clear screen and draw background
  screen.blit(background, (0, 0))  

  # Move and render Sprites
  for entity in all_sprites:
    entity.move()
    entity.render(screen)
    if entity != player: 
      pass

  # Displaying lives
  display_lives(screen, lives)

  # Check Colisions
  fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
  if fruit:
    make_pop(fruit.x, fruit.y)
    goku_sound.play()  
    points = PointsSprite(fruit.x, fruit.y, 100)
    score.update(50)
    all_sprites.add(points)
    fruit.reset()

  dm = pygame.sprite.spritecollideany(player, dm_sprite)
  if dm: 
    make_pop(dm.x, dm.y)
    points = PointsSprite(dm.x, dm.y, 100)
    score.update(100)
    all_sprites.add(points)
    sigma_sound.play()
    player.stun()
    dm.reset()

# Fruit enemy collisions
  fruit = pygame.sprite.spritecollideany(enemy, fruit_sprites)
  if fruit:
    make_explosion(fruit.x, fruit.y)
    huh_sound.play()
    points = PointsSprite(fruit.x, fruit.y, 100)
    score.update(-25)
    all_sprites.add(points)
    fruit.reset()

  fruit = pygame.sprite.spritecollideany(enemy, dm_sprite)
  if fruit:
    make_explosion(fruit.x, fruit.y)
    huh_sound.play()
    points = PointsSprite(fruit.x, fruit.y, 100)
    score.update(-75)
    all_sprites.add(points)
    fruit.reset()

  # Check collision player and enemy
  if pygame.sprite.collide_rect(player, enemy):
    rahhh_sound.play() 
    player.reset() 
    enemy.reset()  
    lives -=1
    if (lives <= 0):
      pygame.quit()

  # Animate the explosions
  for explosion in explosion_sprites:
    explosion.render(screen)
    if explosion.playing == False: 
      explosion.kill()

  # Update the window
  pygame.display.flip()

  # Tick the clock!
  clock.tick(30)
