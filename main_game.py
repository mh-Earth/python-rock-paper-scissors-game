import pygame
import random

pygame.init()
display=pygame.display.set_mode((800,800))
pygame.display.set_caption('Rock Paper Scissore')

rock=pygame.image.load('rock.png')
rock=pygame.transform.scale(rock,(100,100))
paper=pygame.image.load('paper.png')
paper=pygame.transform.scale(paper,(100,100))
scissore=pygame.image.load('scissosr.png')
scissore=pygame.transform.scale(scissore,(100,100))
# ___________________________text functions_____________________________________
def text_screen(text, color, x, y,fontsize=30):
    font = pygame.font.Font("comic.ttf", fontsize)
    screen_text = font.render(text, True, color)
    display.blit(screen_text, [x,y])
# ______________________________________________________________________________
r=0
p=0
s=0
Cr=0
Cp=0
Cs=0

red=(255,0,0)
green=(0,255,0)
cyan=(0,255,255)

# ____________________________gamewin logic_____________________________________
def gamewin():
    if r==1 and Cr==1:
        text_screen("Tie",cyan ,350,700,fontsize=55)
    elif r==1 and Cp==1:
        text_screen("Computer Win",red ,200,700,fontsize=55)

    elif r==1 and Cs==1:
        text_screen("Human wins" ,green,250,700,fontsize=55)

    elif p==1 and Cp==1:
        text_screen("Tie",cyan ,350,700,fontsize=55)
    elif p==1 and Cr==1:
        text_screen("Human wins" ,green,250,700,fontsize=55)

    elif p==1 and Cs==1:
        text_screen("Computer Win",red ,200,700,fontsize=55)
        
    elif s==1 and Cs==1:
        text_screen("Tie",cyan ,350,700,fontsize=55)
    elif s==1 and Cr==1:
        text_screen("Computer Win",red ,200,700,fontsize=55)

    elif s==1 and Cp==1:
        text_screen("Human wins" ,green,250,700,fontsize=55)



human_player=True
computer=False
running=True

rocks=False
papers=False
scissores=False

Crocks=False
Cpapers=False
Cscissores=False
 
C_RPS=[rock,rock,paper,paper,scissore,scissore]

clock=pygame.time.Clock()
while running:
    display.fill((0,0,0))
    text_screen("A=Rock",((248,124,217)),70,530)
    text_screen("S=Papre",((254,237,99)),70,570)
    text_screen("D=Scissore",((76,199,240)),70,610)

    text_screen("Human",cyan,120,80,60)
    text_screen("Computer",cyan,480,80,60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                quit()
            if event.key==pygame.K_a:
                play=random.choice(C_RPS) 
                r=1
                p=0
                s=0
                papers=False
                scissores=False
                rocks=True
                computer=True
            elif event.key==pygame.K_s:
                play=random.choice(C_RPS) 
                p=1
                r=0
                s=0
                rocks=False
                scissores=False
                papers=True
                computer=True
            elif event.key==pygame.K_d:
                play=random.choice(C_RPS) 
                s=1
                r=0
                p=0
                rocks=False
                papers=False
                scissores=True
                computer=True
    # _______________________human controls________________________________            
    if human_player:
        if rocks:
            display.blit(rock,(150,300))
        if papers:
            display.blit(paper,(150,300))
        if scissores:
            display.blit(scissore,(150,300))
    # __________________________computer___________________________________
    if computer:
        display.blit(play,(550,300))
        if play==rock:
            Cr=1
            Cp=0
            Cs=0
        elif play==paper:
            Cp=1
            Cs=0
            Cr=0
        elif play==scissore:
            Cs=1
            Cr=0
            Cp=0
    gamewin()
    pygame.draw.line(display, cyan, (400,500),(400,680), 10)
    pygame.draw.line(display, cyan, (0,680), (800,680), 10)
    clock.tick(20)
    pygame.display.update()