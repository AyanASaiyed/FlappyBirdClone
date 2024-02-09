import random
import pygame


pygame.init()

screen = pygame.display.set_mode((500,750))
background = pygame.image.load('background.jpg')

#Bird
bird = pygame.image.load('bird1.png')
birdX = 50
birdY = 300
birdDY = 0

#Bars
barWidth = 70
barHeight = random.randint(150,450)
barColor = (211,253,117)
barDX = -0.2
barX = 500

def displayBird(someX,someY):
    screen.blit(bird,(someX,someY))

def displayBar(height):
    pygame.draw.rect(screen,barColor,(barX,0,barWidth,height))
    bottomBarHeight = 635 - height - 150
    pygame.draw.rect(screen,barColor,(barX,height+150,barWidth,bottomBarHeight))

def checkCollision(barx,barheight,birdy,btmbarheight):
    if barx >= 50 and barx<=(50+64):
        if birdy <= barheight or birdy >= (btmbarheight-64):
            return True
    return False

score = 0
score_font = pygame.font.Font('freesansbold.ttf',32)

def showScore(score):
    disp = score_font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(disp,(10,10))

running = True

while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                birdDY = -0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                birdDY = 0.25  

    birdY += birdDY
    if birdY <= 0:
        birdY=0
    if birdY >= 571:
        birdY=571 

    barX+=barDX
    if barX <= -10:
        barX = 500
        barHeight = random.randint(200,400)
        score += 1
    displayBar(barHeight)

    collision = checkCollision(barX,barHeight,birdY,barHeight+150)
    if collision or birdY == 0 or birdY ==571:
        pygame.quit()

    displayBird(birdX,birdY)

    showScore(score)

    pygame.display.update()
    
pygame.quit()
