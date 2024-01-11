import random
import pygame
from pygame.transform import scale


pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)

SCREENWIDTH = 800
SCREENHEIGHT = 600
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

pygame.display.set_caption("Cookie Clicker")
icon = pygame.image.load('Cookie.png')
pygame.display.set_icon(icon)

score = 0
font = pygame.font.SysFont("Ariel", 32)

shop_button_rect = pygame.Rect(SCREENWIDTH -200, 10, 180, 50)
shop_open = False
multiplier = 1
cookie = pygame.image.load('Cookie.png')
cookie = pygame.transform.scale(cookie, (cookie.get_width() // 2, cookie.get_height() // 2))

cookie_rect = cookie.get_rect()
cookie_rect.centerx = SCREENWIDTH // 2
cookie_rect.centery = SCREENHEIGHT // 2


running = True

scale = 1

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
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      mouse_x, mouse_y = pygame.mouse.get_pos()
      if cookie_rect.collidepoint(mouse_x, mouse_y):
        score += multiplier
        scale = 0.20
      elif shop_button_rect.collidepoint(mouse_x, mouse_y):
        shop_open = not shop_open
  scale += (0.25 - scale) * 0.4
  pygame.draw.rect(screen, GREEN, shop_button_rect)
  shop_text = font.render("Shop", True, WHITE)
  shop_text_rect = shop_text.get_rect()
  shop_text_rect.centerx = shop_button_rect.centerx
  shop_text_rect.centery = shop_button_rect.centery
  screen.blit(shop_text, shop_text_rect)
  if shop_open:
    shop_bg_rect = pygame.Rect(SCREENWIDTH // 4, SCREENHEIGHT // 2, SCREENHEIGHT // 2)
    pygame.draw.rect(screen, (128, 128, 128), shop_bg_rect)
    shop_title_text = font.render("Shop", True, WHITE)
    shop_text_rect = shop_title_text.get_rect()