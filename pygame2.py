import pygame   
import tkinter
from tkinter import *  
import time 

window = pygame.display.set_mode((480,320)) #해상도

window.blit(pygame.image.load('boynew.PNG'),(90,450))

# 색깔
BLACK = 0, 0, 0          
WHITE = 255, 255, 255  
YELLOW = 255, 255, 130
PINK = 255, 185, 185

window = pygame.display.set_mode((480,320)) #해상도
SCREEN_WIDTH = 450         # 화면 너비(가로)
SCREEN_HEIGHT = 600        # 화면 높이(세로)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

rect = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))  
pygame.draw.rect(screen, YELLOW, rect) # 화면 색

img3 = pygame.image.load('home.PNG')
img_scale3 = pygame.transform.scale(img3, (100, 100)) # 이미지 크기 변환
pygame.image.save(img_scale3, 'homenew.PNG') # 이미지 저장

img4 = pygame.image.load('cafe.PNG')
img_scale4 = pygame.transform.scale(img4, (100, 100)) # 이미지 크기 변환
pygame.image.save(img_scale4, 'cafenew.PNG') # 이미지 저장

img5 = pygame.image.load('library.PNG')
img_scale5 = pygame.transform.scale(img5, (100, 100)) # 이미지 크기 변환
pygame.image.save(img_scale5, 'librarynew.PNG') # 이미지 저장

img6 = pygame.image.load('school.PNG')
img_scale6 = pygame.transform.scale(img6, (100, 100)) # 이미지 크기 변환
pygame.image.save(img_scale6, 'schoolnew.PNG') # 이미지 저장

pygame.init()              # 파이게임을 사용하기 전에 초기화한다.

sf = pygame.font.SysFont("malgungothic", 40) # 폰트, 크기
text = sf.render("Day 1", True, PINK) # 게임 제목
screen.blit(text, (75,100)) 

window.blit(pygame.image.load('boynew.PNG'),(90,450))

window.blit(pygame.image.load('homenew.PNG'),(10,150))

window.blit(pygame.image.load('cafenew.PNG'),(10,300))

window.blit(pygame.image.load('librarynew.PNG'),(340,150))

window.blit(pygame.image.load('schoolnew.PNG'),(340,300))

pygame.display.update()  

player = pygame.image.load("boynew.PNG")
player = pygame.transform.scale(player, (40, 102))
