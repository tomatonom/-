import pygame   
from tkinter import * 
from tkinter import messagebox 
import tkinter
import time 

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

img = pygame.image.load('boy.PNG')
img_scale = pygame.transform.scale(img, (75, 75)) # 이미지 크기 변환
pygame.image.save(img_scale, 'boynew.PNG') # 이미지 저장

img2 = pygame.image.load('girl.PNG')
img_scale2 = pygame.transform.scale(img2, (75, 75)) # 이미지 크기 변환
pygame.image.save(img_scale2, 'girlnew.PNG') # 이미지 저장

pygame.init()              # 파이게임을 사용하기 전에 초기화한다.

sf = pygame.font.SysFont("malgungothic", 40) # 폰트, 크기
text = sf.render("Cramming Grand Plan", True, PINK) # 게임 제목
screen.blit(text, (75,100)) 

window.blit(pygame.image.load('boynew.PNG'),(90,450))

window.blit(pygame.image.load('girlnew.PNG'),(300,450))

pygame.display.update() 

window=tkinter.Tk()
window.title("Your Character")
window.geometry("100x100+450+100")
window.resizable(False, False)

def check():
  str = 'no decide'
  if RadioVariety.get() ==1:
    str = "You are a boy!"
  if RadioVariety.get() ==2:
    str = 'You are a girl!'
  messagebox.showinfo("show", str)

RadioVariety=tkinter.IntVar()

radio1=tkinter.Radiobutton(window, text="Boy", value=1, variable=RadioVariety, command=check)

radio2=tkinter.Radiobutton(window, text="Girl", value=2, variable=RadioVariety, command=check)


click = Button(text="Ok", command=check)

radio1.pack()
radio2.pack()

time.sleep(5)
