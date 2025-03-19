import pygame as pg
import sys
sys.path.append("/storage/emulated/0/PYTHON/Photoshop_clone/helpers")
from settings import *

#____________________________
x,w,h = 10,50,50
menu = pg.Rect(x,20,50,1000)
rect1 = pg.Rect(100,1200,600,200)
btn1= pg.Rect(x,20, w,h)
btn2 = pg.Rect(x,70,w,h)
btn3= pg.Rect(x,120, w,h)
btn4= pg.Rect(x,170,w,h)
btn5= pg.Rect(x,220, w,h)
btn6= pg.Rect(x,270,w,h)
btn7= pg.Rect(x,320, w,h)
btn8 = pg.Rect(x,370,w,h)
shape = pg.image.load("sprites/shapes.png")
class Menu:
	def __init__(self):
		self.rect0 = menu
		self.rect1 = rect1
		self.btn1 = btn1
		self.btn2 = btn2
		self.btn3 = btn3
		self.btn4 = btn4
		self.btn5 = btn5
		self.btn6= btn6
		self.btn7= btn7
		self.btn8 =btn8
	def draw(self):
		pg.draw.rect(win,black,self.rect0,3)
		pg.draw.rect(win,black,self.rect1,3)
		#________________________
		pg.draw.rect(win,black,self.btn1,1)
		pg.draw.rect(win,black,self.btn2,1)
		pg.draw.rect(win,black,self.btn3,1)
		pg.draw.rect(win,black,self.btn4,1)
		pg.draw.rect(win,black,self.btn5,1)
		pg.draw.rect(win,black,self.btn6,1)
		pg.draw.rect(win,black,self.btn7,1)
		pg.draw.rect(win,black,self.btn8,1)
#_____________________________
p_rect = pg.Rect(width //4,100,500,1000)
p_rect1 = pg.Rect(width //4-10,90,500,1000)
class Page:
	def __init__(self):
		self.rect = p_rect
	def draw(self):
		pg.draw.rect(win,grey,p_rect)
		pg.draw.rect(win,white,p_rect1)
#_______ FOR EXIT ________#
exit_img = pg.image.load("sprites/exit2.png")
exitw,exith = 40,40

resize_exit = pg.transform.scale(exit_img,(40,40))
e_rect = pg.Rect(win_rect.right-exitw,win_rect.top,exitw,exith)
class Exit:
	def __init__(self):
		self.rect = e_rect		
	def draw(self):
		win.blit(resize_exit,(self.rect.topleft))
		pg.draw.rect(win,black,self.rect,2)
# _____ UTILITY ________#
def exit(pos,run):
	if Exit().rect.collidepoint(pos):
		run = False
		pg.quit()
		quit()
	return run
				

#____ FOR SHAPES _______#
class Shapes:
	def __init__(self):
		self.circle = Circle()
		self.hexa= Hexagon()
		self.tri = Triangle()
		self.penta = Pentagon()
		self.ecs = Ellipse()
		self.box = Box()
# ___ FOR COLORS ________ #
# ______ LAYERS ________#

