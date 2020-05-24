import pygame, time, random
import sys
from pygame.locals import *
# pygame.init()
# mainClock = pygame.time.Clock()
#
# WINDOWWIDTH = 400
# WINDOWHEIGHT = 400
# windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
# pygame.display.set_caption('Collision Detection')
#
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 255, 255)
#
# foodcounter = 0
# NEWFOOD = 40
# FOODSIZE = 20
# player = pygame.Rect(300, 100, 50, 50)
# foods = []
# for i in range(20):
#     foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE),
#                              random.randint(0, WINDOWHEIGHT - FOODSIZE),
#                              FOODSIZE, FOODSIZE))
# moveLeft = False
# moveRight = False
# moveUp = False
# moveDown = False
#
# MOVESPEED = 6
#
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == KEYDOWN:
#             if event.key == K_LEFT or event.key == K_a:
#                 moveLeft = True
#                 moveRight = False
#             if event.key == K_RIGHT or event.key == K_d:
#                 moveLeft = False
#                 moveRight = True
#             if event.key == K_UP or event.key == K_w:
#                 moveDown = False
#                 moveUp = True
#             if event.key == K_DOWN or event.key == K_s:
#                 moveDown = True
#                 moveUp = False
#         if event.type == KEYUP:
#             if event.key == K_ESCAPE:
#                 pygame.quit()
#                 sys.exit()
#             if event.key == K_LEFT or event.key == K_a:
#                 moveLeft = False
#             if event.key == K_RIGHT or event.key == K_d:
#                 moveRight = False
#             if event.key == K_UP or event.key == K_w:
#                 moveUp = False
#             if event.key == K_DOWN or event.key == K_s:
#                 moveDown = False
#             if event.key == K_x:
#                 player.top = random.randint(0, WINDOWHEIGHT - player.height)
#                 player.left = random.randint(0, WINDOWWIDTH - player.width)
#         if event.type == MOUSEBUTTONUP:
#             foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE,
#                                      FOODSIZE))
#     foodcounter += 1
#     if foodcounter >= NEWFOOD:
#         foodcounter = 0
#         foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE),
#                                  random.randint(0, WINDOWHEIGHT - FOODSIZE),
#                                  FOODSIZE, FOODSIZE))
#     windowSurface.fill(WHITE)
#
#     if moveDown and player.bottom < WINDOWHEIGHT:
#         player.top += MOVESPEED
#     if moveUp and player.top > 0:
#         player.top -= MOVESPEED
#     if moveLeft and player.left > 0:
#         player.left -= MOVESPEED
#     if moveRight and player.right < WINDOWWIDTH:
#         player.left += MOVESPEED
#     pygame.draw.rect(windowSurface, RED, player)
#
#     for food in foods[:]:
#         if player.colliderect(food):
#             foods.remove(food)
#
#     for i in range(len(foods)):
#         pygame.draw.rect(windowSurface, GREEN, foods[i])
#
#     pygame.display.update()
#     mainClock.tick(40)
# Animation
pygame.init()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),
                                        0, 32)
pygame.display.set_caption('Animation')

# Set up direction variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'
MOVESPEED = 10
 # Set up the colors.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 255)

 # Set up the box data structure.
b1 = {'rect': pygame.Rect(300, 80, 50, 100), 'color': RED, 'dir': UPRIGHT}
b2 = {'rect': pygame.Rect(250, 200, 20, 20), 'color': GREEN, 'dir': UPLEFT}
b3 = {'rect': pygame.Rect(100, 150, 60, 60), 'color': BLUE, 'dir': DOWNLEFT}
boxes = [b1, b2, b3]
 # Run the game loop.
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw the white background onto the surface.
    windowSurface.fill(WHITE)

    for b in boxes:
             # Move the box data structure.
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED
         # Check whether the box has moved out of the window.
        if b['rect'].top < 0:
            # The box has moved past the top.
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT

        if b['rect'].bottom > WINDOWHEIGHT:
                # The box has moved past the bottom.
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['rect'].left < 0:
            # The box has moved past the left side.
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
        if b['rect'].right > WINDOWWIDTH:
            # The box has moved past the right side.
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT

         # Draw the box onto the surface.
        pygame.draw.rect(windowSurface, b['color'], b['rect'])

     # Draw the window onto the screen.
    pygame.display.update()
    time.sleep(0.02)

# Hello World
# pygame.init()
#
# windowSurface = pygame.display.set_mode((1000, 800), 0, 32)
# pygame.display.set_caption('Animation')
#
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# PURPLE = (128, 0, 128)
#
# basicFont = pygame.font.SysFont(None, 48)
#
# text = basicFont.render('Hello World!', True, RED, BLUE)
# textRect = text.get_rect()
# textRect.centerx = windowSurface.get_rect().centerx
# textRect.centery = windowSurface.get_rect().centery
#
# pygame.draw.polygon(windowSurface, PURPLE, ((100, 0), (200, 0), (200, 200),
#                                             (50, 275), (0, 100)), 1)
# pygame.draw.line(windowSurface, WHITE, (100, 0), (50, 100))
# windowSurface.blit(text, textRect)
# pixArray = pygame.PixelArray(windowSurface)
# pixArray[100][100] = GREEN
# pygame.display.update()
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
