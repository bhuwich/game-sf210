from traceback import print_tb
import pygame
import math
import time
pygame.init()

display = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
FPS = 100

#BG
bg = pygame.image.load('background.png')
bg = pygame.transform.scale(bg,(1000,600))
#Create Cat
cat = pygame.image.load('Cat.png')
cat = pygame.transform.scale(cat,(150,150))
cat = pygame.transform.flip(cat, flip_x=180,flip_y=0)
cat1 = pygame.image.load('Cat1.png')
cat1 = pygame.transform.scale(cat1,(150,150))
cat1 = pygame.transform.flip(cat1, flip_x=180,flip_y=0)
cat2 = pygame.image.load('Cat2.png')
cat2 = pygame.transform.scale(cat2,(150,150))
cat2 = pygame.transform.flip(cat2, flip_x=180,flip_y=0)
cat3 = pygame.image.load('Cat3.png')
cat3 = pygame.transform.scale(cat3,(150,150))
cat3 = pygame.transform.flip(cat3, flip_x=180,flip_y=0)
cat4 = pygame.image.load('Cat4.png')
cat4 = pygame.transform.scale(cat4,(150,150))
cat4 = pygame.transform.flip(cat4, flip_x=180,flip_y=0)
cat_win = pygame.image.load('Cat Win.png')
cat_win = pygame.transform.scale(cat_win,(330,330))

#Create Dog
dog = pygame.image.load('dog.png')
dog = pygame.transform.scale(dog,(150,150))
dog1 = pygame.image.load('dog1.png')
dog1 = pygame.transform.scale(dog1,(150,150))
dog2 = pygame.image.load('dog2.png')
dog2 = pygame.transform.scale(dog2,(150,150))
dog3 = pygame.image.load('dog3.png')
dog3 = pygame.transform.scale(dog3,(150,150))
dog4 = pygame.image.load('dogdeath.png')
dog4 = pygame.transform.scale(dog4,(150,150))
dog_win = pygame.image.load('Dog Win.png')
dog_win = pygame.transform.scale(dog_win,(350,350))

#fish
fish = pygame.image.load('Bone.png')
fish = pygame.transform.scale(fish,(100,100))
fish = pygame.transform.flip(fish, flip_x=180,flip_y=0)
#bone
bone = pygame.image.load('bone1.png')
bone = pygame.transform.scale(bone,(100,100))
#heart dog 5
heart1 = pygame.image.load('heart.png')
heart1 = pygame.transform.scale(heart1,(50,50))





class Cat():
    def __init__(self):
       self.flag = False
       self.y = 580
       self.x = 50
       self.Vx = 3
       self.Vy = 11
       self.s = 20
       self.i = 0
       self.checks = 0
       self.accerlation = 19.6/FPS
    def conves(self,timecount): 
 
        self.Vx += timecount*2
        self.Vy += timecount*2


    def draw(self):
        if self.flag == False:
            display.blit(fish,(self.x,self.y))
        
    def move(self,timecount):
        move = True
        self.Vy -= self.accerlation
        self.y -= self.Vy
        self.x += self.Vx
        if self.x == 500 and self.y== 300:          
            self.flag = True
        if (self.x >= 1000 or self.y >= 600) and self.checks == 1:

            self.flag = False
            self.y = 580
            self.x = 50
            self.Vx = timecount*2 + 3
            self.Vy = timecount*2 + 11
            self.s = 20
            self.i = 0
            self.checks = 0
            print(self.Vx,self.Vy)
        if self.x >= 1000 or self.y >= 600:           
            move = False
            return move
        return move
    def hit(self,dog_hitbox,wall):
        fishBone_rect = pygame.Rect(self.x,self.y,60,60)
        if fishBone_rect.colliderect(dog_hitbox):
            display.blit(dog3,(850,430))
            self.flag = True
            return True
        if fishBone_rect.colliderect(wall):
            self.flag = True
            
        return False

    def check(self):
        self.checks = 1

class Dog():
    def __init__(self):
       self.flag = False
       self.y = 580
       self.x = 950
       self.Vx = -3
       self.Vy = 11
       self.s = 20
       self.i = 0
       self.checks = 0
       self.accerlation = 19.6/FPS
    def conves(self,timecount): 
          
        self.Vx -= timecount*2
        self.Vy += timecount*2


    def draw(self):
        if self.flag == False:
            display.blit(bone,(self.x,self.y))
        
    def move(self,timecount):
        move = True
        self.Vy -= self.accerlation
        self.y -= self.Vy
        self.x += self.Vx
        if self.x == 500 and self.y== 300:
            print("ball hit!")           
            self.flag = True
        if (self.x <= 0 or self.y >= 600) and self.checks == 1:
            self.flag = False
            self.y = 580
            self.x = 950
            self.Vx = -3 - timecount*2
            self.Vy = timecount*2 + 11
            self.s = 20
            self.i = 0
            self.checks = 0
        
        if self.x <= 0 or self.y >= 600:           
            move = False
            return move
        return move
    def hit(self,cat_hitbox,wall):
        
        Bone_rect = pygame.Rect(self.x,self.y,60,60)
        if Bone_rect.colliderect(cat_hitbox):
            display.blit(cat3,(10,420))
            self.flag = True
            return True
        if Bone_rect.colliderect(wall):
            self.flag = True
        return False

    def check(self):
        self.checks = 1
    
    
def game():
    bone = Dog()
    fish = Cat()
    check = True
    fishs = False
    bones = False
    dog_heart = 5
    cat_heart = 5
    count_hitdog = 0
    count_hitcat = 0

    
    while True:
        display.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                timeStart = time.time()
                if(cat_hitbox.collidepoint(pygame.mouse.get_pos())):
                    check = False
                if(dog_hitbox.collidepoint(pygame.mouse.get_pos())):
                    check = False
               
            if event.type == pygame.MOUSEBUTTONUP:
                if(cat_hitbox.collidepoint(pygame.mouse.get_pos()) and check == False):
                    timeend = time.time()
                    timecount = timeend - timeStart

                    print(pygame.mouse.get_pos())
                    fish.conves(int(timecount))
                    check = True
                    fishs = True 
                if(dog_hitbox.collidepoint(pygame.mouse.get_pos()) and check == False):
                    timeend = time.time()
                    timecount = timeend - timeStart

                    print(pygame.mouse.get_pos())
                    bone.conves(int(timecount))
                    check = True
                    bones = True 

        cat_hitbox = pygame.draw.rect(display,(255,0,0),pygame.Rect(30,450,100,100))
        dog_hitbox = pygame.draw.rect(display,(255,0,0),pygame.Rect(870,450,100,100))
        wall = pygame.draw.rect(display,(255,0,0),pygame.Rect(450,300,100,400))
        display.blit(bg,(0,0))
        #Dog Win
        if cat_heart <= 0:
            display.blit(cat4,(10,420))
            display.blit(dog_win,(330,0))
        else:
            display.blit(cat,(10,420))

        #Cat Win
        if dog_heart <= 0:
            display.blit(dog4,(850,430))
            display.blit(cat_win,(330,0))
        else:
            display.blit(dog,(850,430))

        #Show Heart
        for i in range(dog_heart):
            display.blit(heart1,(900-50*i,20))
        for i in range(cat_heart):
            display.blit(heart1,(50*i,20))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if(cat_hitbox.collidepoint(pygame.mouse.get_pos())):
                count_hitcat = 0
                display.blit(cat1,(10,420))
            if(dog_hitbox.collidepoint(pygame.mouse.get_pos())):
                count_hitdog = 0
                display.blit(dog1,(850,430))
        if event.type == pygame.MOUSEBUTTONUP:
            if(cat_hitbox.collidepoint(pygame.mouse.get_pos())):
                display.blit(cat2,(10,420))

            if(dog_hitbox.collidepoint(pygame.mouse.get_pos())):
                display.blit(dog2,(850,430))

        if fishs :
            move = fish.move(timecount)
            fish.draw()
            if move == False and event.type == pygame.MOUSEBUTTONDOWN:
                if(cat_hitbox.collidepoint(pygame.mouse.get_pos())):
                    fish.check()
                    fishs = False
                    fish.conves(int(timecount))
            
        if bones :
            move = bone.move(timecount)
            bone.draw()
            if move == False and event.type == pygame.MOUSEBUTTONDOWN:
                if(dog_hitbox.collidepoint(pygame.mouse.get_pos())):
                    bone.check()
                    bones = False
                    bone.conves(int(timecount))
            
        if fish.hit(dog_hitbox,wall):
            if(count_hitdog == 0):
                dog_heart -= 1
            count_hitdog = 1
            
        if bone.hit(cat_hitbox,wall):
            if(count_hitcat == 0):
                cat_heart -= 1
            count_hitcat = 1
               
        pygame.display.update()
        
        clock.tick(60)

game()
pygame.quit()