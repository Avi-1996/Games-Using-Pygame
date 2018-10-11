import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)

bright_red = (255,0,0)
bright_green= (0,255,0)

green = (0,200,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Doging! Car')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

car_width=73

pause = False

def block_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged "+str(count),True,black)
    gameDisplay.blit(text,(0,0))

def car(x,y):
    gameDisplay.blit(carImg,(x,y))
    
def blocks(blockx,blocky,blockw,blockh,color):
    pygame.draw.rect(gameDisplay,color,[blockx,blocky,blockw,blockh])


def crash():
    message_display('You Crashed Game Over')

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()
    
    #print(mouse)
    if x+w > mouse[0] > x and y+h >mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action!=None:
            action()
##            if action =='play':
##                game_loop()
##            if action == "quit":
##                pygame.quit()
            
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
    
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf,textRect = text_object(msg,smallText)
    textRect.center= ( (x + (w/2)) , (y+(h/2)) )
    gameDisplay.blit(textSurf,textRect)

def quit_game():
    pygame.quit()
    quit()

def unpaused():
    global pause
    pause = False


def paused():

    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_object("Paused", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        
        button("Continue",150,450,100,50,green,bright_green,unpaused)
        button("Quit",550,450,100,50,red,bright_red,quit_game)

        
        pygame.display.update()
        clock.tick(15)
        


def game_intro():

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_object("Dodging CAR", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        
        button("Go!!",150,450,100,50,green,bright_green,game_loop)
        button("End",550,450,100,50,red,bright_red,quit_game)

        
        pygame.display.update()
        clock.tick(15)
        


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
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
    global pause
    
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    block_startx = random.randrange(0,display_width)
    block_starty = -600
    block_speed = 7
    block_width = 100
    block_height  = 100
    dodge = 0
    block_color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
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
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        
                
        x += x_change

        gameDisplay.fill(white)


        blocks(block_startx , block_starty , block_width , block_height , block_color)
        block_starty+=block_speed
        car(x,y)

        block_dodged(dodge)
        if x> (display_width-car_width) or x<0:
            crash()
        if block_starty > display_height:
            block_starty = 0-block_height
            block_startx = random.randrange(0,display_width)
            dodge+=1
            block_color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            block_speed+=.3
            

        if y < block_starty+block_height:
            #print("Step 1")

            if x > block_startx and x < block_startx + block_width or x+car_width > block_startx and x + car_width < block_startx+block_width:
                #print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
