import random
import pygame
from pygame.mouse import set_pos
from pygame.transform import scale


pygame.init()

# color variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)

# screen variables
SCREENWIDTH = 800
SCREENHEIGHT = 600
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

# game variables
pygame.display.set_caption("Cookie Clicker")
icon = pygame.image.load('Cookie.png')
pygame.display.set_icon(icon)

# gamescore variables
score = 0
font = pygame.font.SysFont("Ariel", 32)

# Autoclicker variables
autoclicker_level = 0
autoclicker_price = 500
autoclicker_increnent = 1
autoclicker_rate = 0

shop_button_rect = pygame.Rect(SCREENWIDTH -200, 10, 180, 50)
shop_multiplier_button_rect = pygame.Rect(SCREENWIDTH // 4 + 10, SCREENHEIGHT // 2 + 10, SCREENWIDTH // 8, SCREENHEIGHT // 8)
autoclicker_rect = pygame.Rect(SCREENWIDTH // 2 + 80, SCREENHEIGHT // 2 + 10, SCREENWIDTH // 8, SCREENHEIGHT // 8)
shop_open = False
multiplier = 1
cookie = pygame.image.load('Cookie.png')
cookie = pygame.transform.scale(cookie, (cookie.get_width() // 2, cookie.get_height() // 2))

cookie_rect = cookie.get_rect()
cookie_rect.centerx = SCREENWIDTH // 2
cookie_rect.centery = SCREENHEIGHT // 2


running = True

scale = 1
particles = []
def create_particle():
    particle = {}
    particle['x'] = cookie_rect.centerx + random.randint(-25, 25)
    particle['y'] = cookie_rect.centery + random.randint(-25, 25)
    particle['size'] = random.randint(8, 13)
    particle['color'] = (255, 255, 255)
    particle['vx'] = random.randint(-15, 15)
    particle["vy"] = random.randint(-15, 15)
    return particle
# main game loop
def handle_autoclicker_upgrade():
    global score, autoclicker_level, autoclicker_price, autoclicker_rate
  
    if score >= autoclicker_price:
      score -= autoclicker_price

      autoclicker_level += 1
      autoclicker_price *= 2
      autoclicker_rate += autoclicker_increnent
      # Prints a message to inform the player that the upgrade was successful
    print(f"Autoclicker upgraded to level {autoclicker_level}!")

# while loops and game loops
while running:
  
  screen.fill(BLACK)
  score_text = font.render(f"Score: {score}", True, WHITE)
  score_rect = score_text.get_rect()
  score_rect.topleft = (10, 10)
  screen.blit(score_text, score_rect)
  temp_surface = pygame.Surface((cookie_rect.width, cookie_rect.height))
  temp_surface.blit(cookie, (0, 0))
  temp_surface = pygame.transform.scale(temp_surface,               (int(cookie_rect.width * scale), int(cookie_rect.height * scale)))
  temp_rect = temp_surface.get_rect()
  temp_rect.centerx = cookie_rect.centerx
  temp_rect.centery = cookie_rect.centery
  screen.blit(temp_surface, temp_rect)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      mouse_x, mouse_y = pygame.mouse.get_pos()
      if cookie_rect.collidepoint(mouse_x, mouse_y):
        score += multiplier
        scale = 0.20
        for i in range(10):
          particle = create_particle()
          particles.append(particle)
          
      elif shop_button_rect.collidepoint(mouse_x, mouse_y):
        shop_open = not shop_open
      elif shop_multiplier_button_rect.collidepoint(mouse_x, mouse_y) and shop_open == True:
          # print("Mulitplier")
          multiplier += 1
      elif autoclicker_rect.collidepoint(mouse_x, mouse_y) and shop_open == True:
        print("Autoclicker")
  scale += (0.25 - scale) * 0.4
  for particle in particles:
    particle['x'] -= particle['vx']
    particle['y'] += particle['vy']
    particle['size'] -= 0.5
    pygame.draw.rect(screen, particle['color'], (particle['x'], particle['y'], particle['size'], particle['size']))
    particles = [particle for particle in particles if particle['size'] > 0]
  pygame.draw.rect(screen, GREEN, shop_button_rect)
  shop_text = font.render("Shop", True, WHITE)
  shop_text_rect = shop_text.get_rect()
  shop_text_rect.centerx = shop_button_rect.centerx
  shop_text_rect.centery = shop_button_rect.centery
  screen.blit(shop_text, shop_text_rect)
  if shop_open:
    shop_bg_rect = pygame.Rect(SCREENWIDTH // 4, SCREENHEIGHT // 4, 
                               SCREENWIDTH // 2, SCREENHEIGHT // 2)
    pygame.draw.rect(screen, (128, 128, 128), shop_bg_rect)
    #Shop button
    shop_title_text = font.render("Shop", True, WHITE)
    shop_title_text_rect = shop_title_text.get_rect()
    shop_text_rect = shop_title_text.get_rect()
    shop_title_text_rect.top = shop_bg_rect.top + 10
    screen.blit(shop_title_text, shop_title_text_rect)

    shop_multiplier_button_rect = pygame.Rect(SCREENWIDTH // 2 + 10, 
                                  SCREENHEIGHT // 2 + 10, 
                                  SCREENWIDTH // 4 - 20, 
                                  SCREENHEIGHT // 4 - 20)
    # draw the rectangle on the screen.
    pygame.draw.rect(screen, BLUE, shop_multiplier_button_rect)

  # creates a text surface object, on which text is drawn on it.
  multiplier_text = font.render(f"Multiplier: {multiplier}", True, WHITE)
  multiplier_textrect = multiplier_text.get_rect()
  multiplier_textrect.centerx = shop_multiplier_button_rect.centerx
  multiplier_textrect.centery = shop_multiplier_button_rect.centery
  screen.blit(multiplier_text, shop_multiplier_button_rect)
  
  autoclicker_rect = pygame.Rect(SCREENWIDTH // 2 +80, SCREENHEIGHT // 2 +10, SCREENWIDTH // 8, SCREENHEIGHT // 8)
  pygame.draw.rect(screen, YELLOW, autoclicker_rect)
  autoclicker_text = font.render("Shop", True, BLACK)
  autoclicker_textrect = autoclicker_text.get_rect()
  autoclicker_textrect.centerx = autoclicker_rect.centerx
  autoclicker_textrect.centery = autoclicker_rect.centery
  screen.blit(autoclicker_text, autoclicker_textrect)

  #We will continue here
  score += autoclicker_rate
  pygame.display.flip()
"""
   
    """