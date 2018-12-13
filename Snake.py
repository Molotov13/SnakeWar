# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from pygame.transform import *
import sys
from os import *
import random
def mode_1():
        def MakeFood():
                L=list()
                for a in range(1,int(surH/gridW)-1):
                        for b in range(1,int(surW/gridW)-1):
                                if (a,b) not in SnakeBody:
                                        L.append((a,b))
                return random.choice(L)
        def game_over1():
                surface=pygame.image.load('over_menu1.png').convert_alpha()
                screen.blit(surface,(225,140))
                while True:
                    for event in pygame.event.get():
                        if event.type==QUIT:
                           exit()
                        elif event.type==MOUSEBUTTONDOWN:
                           pos=pygame.mouse.get_pos()
                           mouse_x = pos[0]
                           mouse_y = pos[1]
                           if 350<=mouse_x<=425 and 265<=mouse_y<=280:
                                   mode_1()
                           elif 350<=mouse_x<=425 and 301<=mouse_y<=316:
                                   main_menu()
                        elif event.type==MOUSEMOTION:
                           pos=pygame.mouse.get_pos()
                           mouse_x = pos[0]
                           mouse_y = pos[1]
                           if 350<=mouse_x<=425 and 265<=mouse_y<=280:
                                   surface=pygame.image.load('over_menu2.png').convert_alpha()
                           elif 350<=mouse_x<=425 and 301<=mouse_y<=316:
                                   surface=pygame.image.load('over_menu3.png').convert_alpha()
                           else:
                                   surface=pygame.image.load('over_menu1.png').convert_alpha()
                    screen.blit(surface,(225,140))
                    pygame.display.update()
        surH=800
        surW=480
        gridW=16
        screen=pygame.display.set_mode((surH,surW),0,32)
        SnakeBody=[(3,1,'Head','R'),(2,1,'Body','V'),(1,1,'Body','H')]
        SnakeHead=(3,1)
        ml    = False
        mr    = True    
        mu    = False
        md    = False
        FoodPosition=MakeFood()
        mainClock = pygame.time.Clock()
        background=pygame.Surface((surH,surW),0,32)
        FPS=5
        for a in range(0,surH,gridW):
            for b in range(0,surW,gridW):
                background.blit(scale(pygame.image.load('grass.png').convert_alpha(),(16,16)),(a,b))
                background.blit(scale(pygame.image.load('tree.png').convert_alpha(),(16,16)),(0,b))
                background.blit(scale(pygame.image.load('tree.png').convert_alpha(),(16,16)),(a,0))
                background.blit(scale(pygame.image.load('tree.png').convert_alpha(),(16,16)),(a,surW-gridW))
                background.blit(scale(pygame.image.load('tree.png').convert_alpha(),(16,16)),(surH-gridW,b))
        while True:
            time_passed = mainClock.tick(FPS)
            for event in pygame.event.get():
                if event.type==QUIT:
                    exit()
                elif event.type==KEYDOWN:
                    if event.key == K_LEFT and mr == False:
                        ml = True
                        mr = False
                        mu = False
                        md = False
                    if event.key == K_RIGHT and ml == False:
                        ml = False
                        mr = True
                        mu = False
                        md = False
                    if event.key == K_UP and md == False:
                        ml = False
                        mr = False
                        mu = True
                        md = False
                    if event.key == K_DOWN and mu == False:
                        ml = False
                        mr = False
                        mu = False
                        md = True
            #获取玩家键盘操作
            if mu==True:
                NextHead=(SnakeHead[0],SnakeHead[1]-1)
            elif md==True:
                NextHead=(SnakeHead[0],SnakeHead[1]+1)
            elif mr==True:
                NextHead=(SnakeHead[0]+1,SnakeHead[1])
            elif ml==True:
                NextHead=(SnakeHead[0]-1,SnakeHead[1])
            #分析下一帧蛇头位置
            if NextHead[0] in (0,surH/gridW-1) or NextHead[1] in (0,surW/gridW-1) or NextHead in [(i[0],i[1]) for i in SnakeBody]:
                game_over1()
                break       
            #判断游戏是否结束                                                                                                                                                                                                                                       
            elif NextHead==FoodPosition:
                SnakeBody=[(i[0],i[1],'Body',i[3]) for i in SnakeBody]
                SnakeHead=NextHead
                if FPS<15:
                        FPS+=0.1
                FoodPosition=MakeFood()
                pygame.mixer.Sound('transmissionStart.wav').play()
            else:
                del SnakeBody[-1:]
                SnakeBody=[(i[0],i[1],'Body',i[3]) for i in SnakeBody]
                SnakeHead=NextHead
            #判断是否吃到水果，并作出相对反应
            if md==True:
                SnakeBody=[(SnakeHead[0],SnakeHead[1],'Head','D')]+SnakeBody
                SnakeBody[1]=(SnakeBody[1][0],SnakeBody[1][1],'Body','V')
                if SnakeBody[2][3]!=SnakeBody[1][3]:
                    SnakeBody[1]=(SnakeBody[1][0],SnakeBody[1][1],'Body','DL')
            elif mu==True:
                SnakeBody=[(SnakeHead[0],SnakeHead[1],'Head','U')]+SnakeBody
                SnakeBody[1]=(SnakeBody[1][0],SnakeBody[1][1],'Body','V')
                if SnakeBody[2][3]!=SnakeBody[1][3]:
                    SnakeBody[1]=(SnakeBody[1][0],SnakeBody[1][1],'Body','DL')
            elif mr==True:
                SnakeBody=[(SnakeHead[0],SnakeHead[1],'Head','R')]+SnakeBody
                SnakeBody[1]=(SnakeBody[1][0],SnakeBody[1][1],'Body','H')
                if SnakeBody[2][3]!=SnakeBody[1][3]:
                    SnakeBody[1]=(SnakeBody[1][0],SnakeBody[1][1],'Body','DL')
            elif ml==True:
                SnakeBody=[(SnakeHead[0],SnakeHead[1],'Head','L')]+SnakeBody
                SnakeBody[1]=(SnakeBody[1][0],SnakeBody[1][1],'Body','H')
                if SnakeBody[2][3]!=SnakeBody[1][3]:
                    SnakeBody[1]=(SnakeBody[1][0],SnakeBody[1][1],'Body','DL')
            screen.blit(background,(0,0))
            screen.blit(scale(pygame.image.load('apple.png').convert_alpha(),(gridW,gridW)),(FoodPosition[0]*gridW,FoodPosition[1]*gridW))
            for  x in SnakeBody:
                if x[2]=='Head':
                        if x[3]=='R':
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),180),(x[0]*gridW,x[1]*gridW))
                        elif x[3]=='L':
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),0),(x[0]*gridW,x[1]*gridW))
                        elif x[3]=='U':
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),270),(x[0]*gridW,x[1]*gridW))
                        elif x[3]=='D':
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),90),(x[0]*gridW,x[1]*gridW))
                else:
                        screen.blit(scale(pygame.image.load('body.png').convert_alpha(),(gridW,gridW)),(x[0]*gridW,x[1]*gridW))
            pygame.display.update()
def mode_2():
        def MakeFood():
                L=list()
                for a in range(1,int(surH/gridW)-1):
                        for b in range(1,int(surW/gridW)-1):
                                if (a,b) not in SnakeBody_1 and (a,b) not in SnakeBody_2:
                                        L.append((a,b))
                return random.choice(L)
        def game_over(player):
                surface=pygame.image.load('over_menu1.png').convert_alpha()
                screen.blit(surface,(225,140))
                while True:
                    for event in pygame.event.get():
                        if event.type==QUIT:
                           exit()
                        elif event.type==MOUSEBUTTONDOWN:
                           pos=pygame.mouse.get_pos()
                           mouse_x = pos[0]
                           mouse_y = pos[1]
                           if 350<=mouse_x<=425 and 265<=mouse_y<=280:
                                   mode_2()
                           elif 350<=mouse_x<=425 and 301<=mouse_y<=316:
                                   main_menu()
                        elif event.type==MOUSEMOTION:
                                   pos=pygame.mouse.get_pos()
                                   mouse_x = pos[0]
                                   mouse_y = pos[1]
                                   if 350<=mouse_x<=425 and 265<=mouse_y<=280:
                                           surface=pygame.image.load('over_menu2.png').convert_alpha()
                                   elif 350<=mouse_x<=425 and 301<=mouse_y<=316:
                                           surface=pygame.image.load('over_menu3.png').convert_alpha()
                                   else:
                                           surface=pygame.image.load('over_menu1.png').convert_alpha()
                    screen.blit(surface,(225,140))
                    pygame.display.update()
        surH=800
        surW=480
        gridW=16
        screen=pygame.display.set_mode((surH,surW),0,32)
        SnakeBody_1=[(3,3,'Head','R'),(2,3,'Body'),(1,3,'Body')]
        SnakeHead_1=(3,3)
        SnakeBody_2=[(47,26,'Head','L'),(48,26,'Body'),(49,26,'Body')]
        SnakeHead_2=(47,26)
        ml_1    = False
        mr_1    = True    
        mu_1    = False
        md_1    = False
        ml_2    = True
        mr_2    = False   
        mu_2    = False
        md_2    = False
        FoodPosition=MakeFood()
        mainClock = pygame.time.Clock()
        background=pygame.Surface((surH,surW),0,32)
        FPS=5
        for a in range(0,surH,gridW):
            for b in range(0,surW,gridW):
                background.blit(scale(pygame.image.load('grass.png').convert_alpha(),(16,16)),(a,b))
                background.blit(scale(pygame.image.load('tree.png').convert_alpha(),(16,16)),(0,b))
                background.blit(scale(pygame.image.load('tree.png').convert_alpha(),(16,16)),(a,0))
                background.blit(scale(pygame.image.load('tree.png').convert_alpha(),(16,16)),(a,surW-gridW))
                background.blit(scale(pygame.image.load('tree.png').convert_alpha(),(16,16)),(surH-gridW,b))
        while True:
            time_passed = mainClock.tick(FPS)
            for event in pygame.event.get():
                if event.type==QUIT:
                    exit()
                elif event.type==KEYDOWN:
                    if event.key == 97 and mr_1 == False:
                        ml_1 = True
                        mr_1 = False
                        mu_1 = False
                        md_1 = False
                    if event.key == 100 and ml_1 == False:
                        ml_1 = False
                        mr_1 = True
                        mu_1 = False
                        md_1 = False
                    if event.key == 119 and md_1 == False:
                        ml_1 = False
                        mr_1 = False
                        mu_1 = True
                        md_1 = False
                    if event.key == 115 and mu_1 == False:
                        ml_1 = False
                        mr_1 = False
                        mu_1 = False
                        md_1 = True
                    if event.key == K_LEFT and mr_2 == False:
                        ml_2 = True
                        mr_2 = False
                        mu_2 = False
                        md_2 = False
                    if event.key == K_RIGHT and ml_2 == False:
                        ml_2 = False
                        mr_2 = True
                        mu_2 = False
                        md_2 = False
                    if event.key == K_UP and md_2 == False:
                        ml_2 = False
                        mr_2 = False
                        mu_2 = True
                        md_2 = False
                    if event.key == K_DOWN and mu_2 == False:
                        ml_2 = False
                        mr_2 = False
                        mu_2 = False
                        md_2 = True
            if mu_1==True:
                NextHead_1=(SnakeHead_1[0],SnakeHead_1[1]-1)
            elif md_1==True:
                NextHead_1=(SnakeHead_1[0],SnakeHead_1[1]+1)
            elif mr_1==True:
                NextHead_1=(SnakeHead_1[0]+1,SnakeHead_1[1])
            elif ml_1==True:
                NextHead_1=(SnakeHead_1[0]-1,SnakeHead_1[1])
            if NextHead_1[0] in (0,surH/gridW-1) or NextHead_1[1] in (0,surW/gridW-1) or NextHead_1 in [(i[0],i[1]) for i in SnakeBody_1] or  NextHead_1 in [(i[0],i[1]) for i in SnakeBody_2]:
                game_over('玩家2')
                break
            elif NextHead_1==FoodPosition:
                SnakeHead_1=NextHead_1
                FoodPosition=MakeFood()
                pygame.mixer.Sound('transmissionStart.wav').play()
            else:
                del SnakeBody_1[-1:]
                SnakeHead_1=NextHead_1
            SnakeBody_1=[(i[0],i[1],'Body') for i in SnakeBody_1]
            SnakeBody_1=[(SnakeHead_1[0],SnakeHead_1[1],'Head')]+SnakeBody_1
            
            if mu_2==True:
                NextHead_2=(SnakeHead_2[0],SnakeHead_2[1]-1)
            elif md_2==True:
                NextHead_2=(SnakeHead_2[0],SnakeHead_2[1]+1)
            elif mr_2==True:
                NextHead_2=(SnakeHead_2[0]+1,SnakeHead_2[1])
            elif ml_2==True:
                NextHead_2=(SnakeHead_2[0]-1,SnakeHead_2[1])
            if NextHead_2[0] in (0,surH/gridW-1) or NextHead_2[1] in (0,surW/gridW-1) or  NextHead_2 in [(i[0],i[1]) for i in SnakeBody_1] or  NextHead_2 in [(i[0],i[1]) for i in SnakeBody_2]:
                game_over('玩家1')
                break
            elif NextHead_2==FoodPosition:
                Head_2=NextHead_2
                FoodPosition=MakeFood()
                pygame.mixer.Sound('transmissionStart.wav').play()
            else:
                del SnakeBody_2[-1:]
                SnakeHead_2=NextHead_2
            SnakeBody_2=[(i[0],i[1],'Body') for i in SnakeBody_2]
            SnakeBody_2=[(SnakeHead_2[0],SnakeHead_2[1],'Head')]+SnakeBody_2

            screen.blit(background,(0,0))
            screen.blit(scale(pygame.image.load('apple.png').convert_alpha(),(gridW,gridW)),(FoodPosition[0]*gridW,FoodPosition[1]*gridW))
            for  x in SnakeBody_1:
                if x[2]=='Head':
                        if mr_1==True:
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),180),(x[0]*gridW,x[1]*gridW))
                        elif ml_1==True:
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),0),(x[0]*gridW,x[1]*gridW))
                        elif mu_1==True:
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),270),(x[0]*gridW,x[1]*gridW))
                        elif md_1==True:
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),90),(x[0]*gridW,x[1]*gridW))
                else:
                        screen.blit(scale(pygame.image.load('body.png').convert_alpha(),(gridW,gridW)),(x[0]*gridW,x[1]*gridW))
            for  x in SnakeBody_2:
                if x[2]=='Head':
                        if mr_2==True:
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),180),(x[0]*gridW,x[1]*gridW))
                        elif ml_2==True:
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),0),(x[0]*gridW,x[1]*gridW))
                        elif mu_2==True:
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),270),(x[0]*gridW,x[1]*gridW))
                        elif md_2==True:
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),90),(x[0]*gridW,x[1]*gridW))
                else:
                    screen.blit(scale(pygame.image.load('body.png').convert_alpha(),(gridW,gridW)),(x[0]*gridW,x[1]*gridW))
            pygame.display.update()
def mode_3():
        def MakeFood():
                L=list()
                for a in range(1,int(surH/gridW)-1):
                        for b in range(1,int(surW/gridW)-1):
                                if (a,b) not in Body_1 and (a,b) not in Body_2:
                                        L.append((a,b))
                return random.choice(L)
        def game_over(player):
                surface=pygame.image.load('over_menu1.png').convert_alpha()
                screen.blit(surface,(225,140))
                while True:
                    for event in pygame.event.get():
                        if event.type==QUIT:
                           exit()
                        elif event.type==MOUSEBUTTONDOWN:
                           pos=pygame.mouse.get_pos()
                           mouse_x = pos[0]
                           mouse_y = pos[1]
                           if 350<=mouse_x<=425 and 265<=mouse_y<=280:
                                   mode_3()
                           elif 350<=mouse_x<=425 and 301<=mouse_y<=316:
                                   main_menu()
                        elif event.type==MOUSEMOTION:
                           pos=pygame.mouse.get_pos()
                           mouse_x = pos[0]
                           mouse_y = pos[1]
                           if 350<=mouse_x<=425 and 265<=mouse_y<=280:
                                   surface=pygame.image.load('over_menu2.png').convert_alpha()
                           elif 350<=mouse_x<=425 and 301<=mouse_y<=316:
                                   surface=pygame.image.load('over_menu3.png').convert_alpha()
                           else:
                                   surface=pygame.image.load('over_menu1.png').convert_alpha()
                    screen.blit(surface,(225,140))
                    pygame.display.update()
        surH=800
        surW=480
        gridW=16
        screen=pygame.display.set_mode((surH,surW),0,32)
        Body_1=[(3,3),(2,3),(1,3)]
        Head_1=(3,3)
        Body_2=[(47,26),(48,26),(49,26)]
        Head_2=(47,26)
        ml_1    = False
        mr_1    = True    
        mu_1    = False
        md_1    = False
        ml_2    = True
        mr_2    = False   
        mu_2    = False
        md_2    = False
        FoodPosition=MakeFood()
        mainClock = pygame.time.Clock()
        background=pygame.Surface((surH,surW),0,32)
        FPS=5
        for a in range(0,surH,gridW):
            for b in range(0,surW,gridW):
                background.blit(scale(pygame.image.load('grass.png').convert_alpha(),(16,16)),(a,b))
                background.blit(scale(pygame.image.load('tree.png').convert_alpha(),(16,16)),(0,b))
                background.blit(scale(pygame.image.load('tree.png').convert_alpha(),(16,16)),(a,0))
                background.blit(scale(pygame.image.load('tree.png').convert_alpha(),(16,16)),(a,surW-gridW))
                background.blit(scale(pygame.image.load('tree.png').convert_alpha(),(16,16)),(surH-gridW,b))
        while True:
            time_passed = mainClock.tick(FPS)
            for event in pygame.event.get():
                if event.type==QUIT:
                    exit()
                elif event.type==KEYDOWN:
                    if event.key == K_LEFT and mr_2 == False:
                        ml_1 = False
                        mr_1 = True
                        mu_1 = False
                        md_1 = False
                        ml_2 = True
                        mr_2 = False
                        mu_2 = False
                        md_2 = False
                    if event.key == K_RIGHT and ml_2 == False:
                        ml_1 = True
                        mr_1 = False
                        mu_1 = False
                        md_1 = False
                        ml_2 = False
                        mr_2 = True
                        mu_2 = False
                        md_2 = False
                    if event.key == K_UP and md_2 == False:
                        mr_1 = False
                        mu_1 = False
                        md_1 = True
                        ml_1 = False
                        ml_2 = False
                        mr_2 = False
                        mu_2 = True
                        md_2 = False
                    if event.key == K_DOWN and mu_2 == False:
                        mr_1 = False
                        mu_1 = True
                        md_1 = False
                        ml_1 = False
                        ml_2 = False
                        mr_2 = False
                        mu_2 = False
                        md_2 = True
            if mu_1==True:
                NextHead_1=(Head_1[0],Head_1[1]-1)
            elif md_1==True:
                NextHead_1=(Head_1[0],Head_1[1]+1)
            elif mr_1==True:
                NextHead_1=(Head_1[0]+1,Head_1[1])
            elif ml_1==True:
                NextHead_1=(Head_1[0]-1,Head_1[1])
            if mu_2==True:
                NextHead_2=(Head_2[0],Head_2[1]-1)
            elif md_2==True:
                NextHead_2=(Head_2[0],Head_2[1]+1)
            elif mr_2==True:
                NextHead_2=(Head_2[0]+1,Head_2[1])
            elif ml_2==True:
                NextHead_2=(Head_2[0]-1,Head_2[1])
            if NextHead_1[0] in (0,surH/gridW-1) or NextHead_1[1] in (0,surW/gridW-1) or NextHead_1 in Body_1 or NextHead_1 in Body_2:
                game_over('玩家2')
                break
            elif NextHead_2==FoodPosition or NextHead_1==FoodPosition:
                Head_1=NextHead_1
                Head_2=NextHead_2
                pygame.mixer.Sound('transmissionStart.wav').play()
                FoodPosition=MakeFood()
            else:
                del Body_1[-1:]
                Head_1=NextHead_1
                del Body_2[-1:]
                Head_2=NextHead_2
            if NextHead_2[0] in (0,surH/gridW-1) or NextHead_2[1] in (0,surW/gridW-1) or NextHead_2 in Body_1 or NextHead_2 in Body_2:
                game_over('玩家1')
                break
            Body_1=[(i[0],i[1],'Body') for i in Body_1]
            Body_1=[(Head_1[0],Head_1[1],'Head')]+Body_1
            Body_2=[(i[0],i[1],'Body') for i in Body_2]
            Body_2=[(Head_2[0],Head_2[1],'Head')]+Body_2
            screen.blit(background,(0,0))
            screen.blit(scale(pygame.image.load('apple.png').convert_alpha(),(gridW,gridW)),(FoodPosition[0]*gridW,FoodPosition[1]*gridW))
            for  x in Body_1:
                if x[2]=='Head':
                        if mr_1==True:
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),180),(x[0]*gridW,x[1]*gridW))
                        elif ml_1==True:
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),0),(x[0]*gridW,x[1]*gridW))
                        elif mu_1==True:
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),270),(x[0]*gridW,x[1]*gridW))
                        elif md_1==True:
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),90),(x[0]*gridW,x[1]*gridW))
                else:
                        screen.blit(scale(pygame.image.load('body.png').convert_alpha(),(gridW,gridW)),(x[0]*gridW,x[1]*gridW))
            for  x in Body_2:
                if x[2]=='Head':
                        if mr_2==True:
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),180),(x[0]*gridW,x[1]*gridW))
                        elif ml_2==True:
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),0),(x[0]*gridW,x[1]*gridW))
                        elif mu_2==True:
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),270),(x[0]*gridW,x[1]*gridW))
                        elif md_2==True:
                                screen.blit(rotate(scale(pygame.image.load('head.png').convert_alpha(),(gridW,gridW)),90),(x[0]*gridW,x[1]*gridW))
                else:
                    screen.blit(scale(pygame.image.load('body.png').convert_alpha(),(gridW,gridW)),(x[0]*gridW,x[1]*gridW))
            pygame.display.update()
def main_menu():
        pygame.init()
        pygame.mixer.music.load('music.mp3')
        pygame.mixer.music.play(loops=0, start=0.0)
        screen=pygame.display.set_mode((800,480),0,32)
        pygame.display.set_caption('贪吃蛇大战')
        cover=pygame.image.load('cover.png').convert_alpha()
        size=(150,60)
        c=(325,165)
        d=(325,235)
        e=(325,305)
        f=(325,375)
        ModePvC=scale(pygame.image.load('P1_1.png').convert_alpha(),size)
        ModePvP=scale(pygame.image.load('P2_1.png').convert_alpha(),size)
        ModePVE=scale(pygame.image.load('P3_1.png').convert_alpha(),size)
        Quit=scale(pygame.image.load('Quit_1.png').convert_alpha(),size)
        screen.blit(cover,(0,0))
        screen.blit(ModePvC,c)
        screen.blit(ModePvP,d)
        screen.blit(ModePVE,e)
        screen.blit(Quit,f)
        pygame.display.update()
        while True:
            screen.blit(cover,(0,0))
            for event in pygame.event.get():
                if event.type==QUIT:
                    exit()
                elif event.type==MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    mouse_x = pos[0]
                    mouse_y = pos[1]
                    if 325<=mouse_x<=475 and 165<=mouse_y<=225:
                        mode_1()
                    elif 325<=mouse_x<=475 and 235<=mouse_y<=295:
                        mode_2()
                    elif 325<=mouse_x<=475 and 305<=mouse_y<=365:
                        mode_3()
                    elif 325<=mouse_x<=475 and 375<=mouse_y<=435:
                        exit()
                elif event.type==MOUSEMOTION:
                    pos=pygame.mouse.get_pos()
                    mouse_x = pos[0]
                    mouse_y = pos[1]
                    if 325<=mouse_x<=475 and 165<=mouse_y<=225:
                        ModePvC=scale(pygame.image.load('P1_2.png').convert_alpha(),size)
                    else: 
                        ModePvC=scale(pygame.image.load('P1_1.png').convert_alpha(),size)
                    if 325<=mouse_x<=475 and 235<=mouse_y<=295:
                        ModePvP=scale(pygame.image.load('P2_2.png').convert_alpha(),size)
                    else: 
                        ModePvP=scale(pygame.image.load('P2_1.png').convert_alpha(),size)
                    if 325<=mouse_x<=475 and 305<=mouse_y<=365:
                        ModePVE=scale(pygame.image.load('P3_2.png').convert_alpha(),size)
                    else: 
                        ModePVE=scale(pygame.image.load('P3_1.png').convert_alpha(),size)
                    if 325<=mouse_x<=475 and 375<=mouse_y<=435:
                        Quit=scale(pygame.image.load('Quit_2.png').convert_alpha(),size)
                    else: 
                        Quit=scale(pygame.image.load('Quit_1.png').convert_alpha(),size)
            screen.blit(ModePvC,c)
            screen.blit(ModePvP,d)
            screen.blit(ModePVE,e)
            screen.blit(Quit,f)
            pygame.display.update()
main_menu()
