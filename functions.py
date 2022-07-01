from traceback import print_tb
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
       self.Vx = 1
       self.Vy = 9
       self.s = 20
       self.i = 0
       self.checks = 0
       self.accerlation = 19.6/FPS
    def conves(self,timecount): 
        self.Vx = 1
        self.Vy = 9    
        self.Vx += timecount
        self.Vy += timecount


    def draw(self):
        if self.flag == False:
            pygame.draw.circle(display, (255,0,0), (self.x,self.y), 15)
        
        
    def move(self,timecount):
        move = True
        self.Vy -= self.accerlation
        self.y -= self.Vy
        self.x += self.Vx
        if self.x == 500 and self.y== 300:
            print("ball hit!")           
            self.flag = True
        if (self.x >= 1000 or self.y >= 600) and self.checks == 1:

            self.flag = False
            self.y = 580
            self.x = 50
            self.Vx = timecount + 1
            self.Vy = timecount + 9
            self.s = 20
            self.i = 0
            self.checks = 0
            print(self.Vx,self.Vy)
        if self.x >= 1000 or self.y >= 600:           
            move = False
            return move
        return move
            
    def check(self):
        self.checks = 1
    
    
            
        


def game():
    ball = Ball()
    check = True
    balls = False
    
    while True:
        display.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                timeStart = time.time()
                if(button.collidepoint(pygame.mouse.get_pos())):
                    check = False
               
            if event.type == pygame.MOUSEBUTTONUP:
                if(button.collidepoint(pygame.mouse.get_pos()) and check == False):
                    timeend = time.time()
                    timecount = timeend - timeStart
                    print("time = ", timeend - timeStart)
                    print(pygame.mouse.get_pos())
                    ball.conves(int(timecount))
                    check = True
                    balls = True
        if balls :
            move = ball.move(timecount)
            display.fill((255,255,255))
            ball.draw()
            if move == False and event.type == pygame.MOUSEBUTTONDOWN:
                 
                 if(button.collidepoint(pygame.mouse.get_pos())):
                    ball.check()
                    balls = False
                    ball.conves(int(timecount))


            
        button =pygame.draw.rect(display,(255,0,0),pygame.Rect(500,300,100,400))
        
        pygame.display.update()
        
        clock.tick(FPS)

game()
pygame.quit()