import pygame
import math
import time
pygame.init()

display = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
FPS = 100



class Ball():
    def __init__(self):
       self.flag = False
       self.y = 580
       self.x = 50
       self.Vx = 6
       self.Vy = 15
       self.s = 20
       self.i = 0
       self.accerlation = 19.6/FPS

    def draw(self):
        if self.flag == False:
            pygame.draw.circle(display, (255,0,0), (self.x,self.y), 15)
        
        
    def move(self):
        self.Vy -= self.accerlation
        self.y -= self.Vy
        self.x += self.Vx
        if self.x == 500 and self.y== 300:
            print("ball hit!")           
            self.flag = True
    
            
        


def game():
    ball = Ball()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                timeStart = time.time()
               
            if event.type == pygame.MOUSEBUTTONUP:
                if(button.collidepoint(pygame.mouse.get_pos())):
                    timeend = time.time()
                    print("time = ", timeend - timeStart)
                    print(pygame.mouse.get_pos())
                print('eiei')
        ball.move()
        display.fill((255,255,255))
        ball.draw()
        button =pygame.draw.rect(display,(255,0,0),pygame.Rect(500,300,100,400))
        
        pygame.display.update()
        
        clock.tick(FPS)

game()
pygame.quit()