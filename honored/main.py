import pygame
import random
import math


pygame.init()

screen=pygame.display.set_mode((1280,720))

#map
level= pygame.image.load('city.png')
#Honored
pygame.display.set_caption("Honored")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
#bohater
boh_img=pygame.image.load('boh.png')
bohX: int=500
bohY=500
bohX_change = 0
#sword
sword_img = pygame.image.load('sword.png')
swordX = 0
swordY = 500
swordX_change = 1
swordY_change = 1
sword_state = "hit"

#NPC
npc_img = []
npcX = []
npcY = []
npcX_change = []
npcY_change = []
numer_npc = 6

for i in range(numer_npc):
        npc_img.append(pygame.image.load('npc.png'))
        npcX.append(random.randint(0,100))
        npcY.append(random.randint(100,300))
        npcX_change.append(2)
        npcY_change.append(40)

#tabela
life=100
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

end=pygame.font.Font('freesansbold.ttf',64)

def boh(x,y):
        screen.blit(boh_img, (x, y))

def show_life(x,y):
    life = font.render("HP",True,(255,0,0))
    screen.blit(life,(x,y))

def npc (x,y,i):
        screen.blit(npc_img[i], (x, y))

def sword (x,y):
    global sword_state
    sword_state = "hito"
    screen.blit(sword_img, (x + 1, y + 1))
def collisions (npcX,npcY,swordX,swordY):
        dystans = math.sqrt(math.pow(npcX-swordX, 2) + (math.pow(npcY-swordY, 2)))
        if dystans < 1:

            return True
        else:
            return False

#okno
run=True
while run:
    screen.fill((0,0,0))
    screen.blit(level,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    #ster
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    bohX_change = -10
                if event.key == pygame.K_d:
                    bohX_change = 10
                if event.key == pygame.K_w:
                    bohY_change = 10
                if event.key == pygame.K_s:
                    bohY_change = 0
                if event.key == pygame.K_SPACE:


        boh(bohX,bohY)
        bohX += bohX_change
    if bohX <= 0:
        bohX = 0
    elif bohX >= 736:
        bohX = 736

    for i in range (numer_npc):

        npcX[i] += npcX_change[i]
        if  npcX[i] <= 0:
            npcX_change[i] = 4
            npcY[i] += npcY_change[i]
        elif npcX_change[i] >= 736:
            npcX_change[i]= -4
            npcY[i] += npcY_change[i]


        incollisions = collisions(npcX[i],npcY[i],swordX,swordY)
        if incollisions:
            swordY=0
            sword_state = "hito"
            npcX[i] = random.randint(0,500)
            npcY[i] = random.randint(0,500)

            npc(npcX[i],npcY[i], i)


        if swordY<=0:
            swordY = 0
            sword_state = "hito"

        if  sword_state is "ok":
             sword(swordX,swordY)
             swordY -= swordY_change

    boh(bohX,bohY)
    pygame.display.update()