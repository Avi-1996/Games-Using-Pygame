import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Avinash')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

car_width=73

def car(x,y):
    gameDisplay.blit(carImg,(x,y))
def blocks(blockx,blocky,blockw,blockh,color):
    pygame.draw.rect(gameDisplay,color,[blockx,blocky,blockw,blockh])


def crash():
    message_display('You Crashed Game Over')


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',25)
    TextSurf, TextRect = text_object(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def text_object(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()
    





def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    block_startx = random.randrange(0,display_width)
    block_starty = -600
    block_speed = 7
    block_width = 100
    block_height  = 100

    
    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        
                
        x += x_change

        gameDisplay.fill(white)

        blocks(block_startx , block_starty , block_width , block_height , black)
        block_starty+=block_speed
        car(x,y)

        
        if x> (display_width-car_width) or x<0:
            crash()
        if block_starty > display_height:
            block_starty = 0-block_height
            block_startx = random.randrange(0,display_width)
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
