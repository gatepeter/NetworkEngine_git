#####################################################################
#                  PROJECT NAME:  REMOVE TEAMVIEW, VNC.             #
#                  AUTHOR: IT  TOSY TEAM                            #
#####################################################################
import socket, sys, os, pygame
from PIL import Image
import pygame
import io
from io import StringIO
import threading
import base64
#from pygame.locals import *
import autopy
import time
#import utils
HOST = '192.168.1.139'
PORT = 50007
done = False
key = 1
class MouseClass:
    def getMouseValues(self,done):
        clock = pygame.time.Clock()
        timer = 0
        #dt = 0
        (ch, LB, CB, RB,p,x,y) = ('None', 0,0,0,0,0,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #print(event.key)
                    pygame.quit()
                    sys.exit()
                    done = True
                else:
                    #print(pygame.key.name(event.key))
                    #pass
                    ch = str(pygame.key.name(event.key))
            elif event.type == pygame.MOUSEMOTION:
                #print('pg.MOUSEMOTION:', pygame.MOUSEMOTION)
                if event.buttons[0]==1:  # Left mouse button pressed.
                    p = 1
                    #print('event.buttons[0]: ',event.buttons[0])
                    x += event.rel[0]
                    y += event.rel[1]
                    print('x:', x)
                    print('y:', y)
            elif event.type == pygame.MOUSEBUTTONDOWN:

                #print('in mousebuttondown')
                #print('mouse: %d' % event.button)
                if event.button == 1:
                    if timer ==0:
                        timer = 0.001
                        LB = 1
                    elif timer < 0.2:
                        LB = 11
                        timer = 0

                elif event.button == 2:
                    CB = 1
                elif event.button == 3:
                    RB = 1
        (X,Y) = pygame.mouse.get_pos()
        #ch = pygame.key.name(event.key)
        #print(X,Y)
        #print(ch,X, Y, LB, CB, RB)
        return (ch,X, Y, LB, CB, RB,p,x,y)

def loadpicture():
    #done = False
    older_1 = 'None'
    data = ''
    while done == False:
        try:
            data = ''
            data = s.recv(99999999)
            #print('datadata:  nn',data)
            if data != older_1:
                output1 = io.BytesIO(base64.b64decode(data))
                pepeImg = pygame.image.load(output1)
                # for e in pygame.event.get():
                # 	if e.type == pygame.QUIT:
                # 		pass
                screen.blit(pepeImg, (0, 0))
                pygame.display.flip()
                #time.sleep(0.15)
                print('load picture')
            older_1 = data
        except: continue
threads = []
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    abc = input("ID: ")
    serverId = int(abc)
    encryptedId = serverId^key
    s.sendall(str(encryptedId).encode())
    data = s.recv(1024)
    size = eval(data)
    pygame.init()
    clock = pygame.time.Clock()

    timer = 0
    #icon = pygame.image.load('tosy.jpg')
    #pygame.display.set_icon(icon)
    #pygame.display.set_caption('TOSY REMOTE')
    screen = pygame.display.set_mode(size)
    color = [255, 0, 0]
    #red = [255, 0, 0]
    screen.fill(color)
    mouse = MouseClass()
    exitFlag = False
    t = threading.Thread(target=loadpicture)
    #t.daemon = True
    threads.append(t)
    t.start()
    done = False
    olddata = "None"
    data = ""
    while 1:
        try:
            data = ''
            data = str(mouse.getMouseValues(done))
            #data = str(data)
            #print(data)
            if data != olddata:
                s.sendall(data.encode())
                print(data)
            #s.sendall(data.encode())
            time.sleep(0.25)
            olddata = data
            # data = s.recv(99999999)
            # #print('datadata:  nn',data)
            # output1 = io.BytesIO(base64.b64decode(data))
            # pepeImg = pygame.image.load(output1)
            # for e in pygame.event.get():
            # 	if e.type == pygame.QUIT:
            # 		pass
            # screen.blit(pepeImg, (0, 0))
            # pygame.display.flip()
        except: continue
    s.close()