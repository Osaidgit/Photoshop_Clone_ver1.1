import pygame as pg
import sys
sys.path.append("storage/emulated/0/PYTHON/Photoshop_clone")
from settings import * #win_rect,#width,height,black

#_____ FOR FILES ______#
#   For File Icon  #
file_x,file_y = win_rect.center
file_w = width //2
file_h = height //4

file_icon_rect = pg.Rect(5,365,30,30)
file_img = pg.image.load("sprites/plus.png").convert_alpha()
resize_file = pg.transform.scale(file_img,(30,30))
#   For File Window  #
file_window = pg.Rect(file_x,file_y,file_w,file_h)

# For File path
path_bar = pg.Rect(file_x+25,file_y+50,file_w - 50,file_h // 4)

exit_w = file_w // 16
exit_h = file_h // 12
# For file window Exit button
file_exit = pg.Rect(file_window.right-exit_w,file_window.top,exit_w,exit_h)

#For file Font
file_font = pg.font.SysFont(None,15)
file_text = file_font.render("X",True,black)
# For Open file button
open_w = file_w //4
open_h = file_h // 8
opn_h = open_h // 2
open_rect = pg.Rect(file_window.left+open_w, file_window.centery+open_h,open_w, open_h)
#For Open text
open_text = file_font.render("open",True,white)
open_text_rect = open_text.get_rect(center = open_rect.center)
# For Directory
direct_font = pg.font.SysFont(None,path_bar.x//2)
direct_text = file_font.render(str(os.getcwd()),True,black)

class File:
	def __init__(self):
		self.icon_rect = file_icon_rect
		self.window_rect = file_window
		self.path_bar = path_bar
		self.exit = file_exit
		self.text = file_text
		self.open_rect = open_rect
		self.open_text_surf = open_text_rect
		self.direct_text =direct_text
	def draw_icon(self):
		win.blit(resize_file,self.icon_rect.center)
	def draw_window(self):
		pg.draw.rect(win,Gainsobro,self.window_rect,border_radius = 5)
		pg.draw.rect(win,black,self.window_rect,2,border_radius = 5)
		#For Draw PathBar
		pg.draw.rect(win,h_white,self.path_bar)
		pg.draw.rect(win,black,self.path_bar,2)
		
		#For Draw Directory
		win.blit(self.direct_text,(self.path_bar.left,self.path_bar.centery))
		
		#For Exit Button
		pg.draw.rect(win,GREY,self.exit,border_radius = 5)
		pg.draw.rect(win,black,self.exit,3,border_radius = 5)
		
		win.blit(self.text,self.exit.center)
		#For Open Button
		pg.draw.rect(win,DARKBLUE,self.open_rect,border_radius = 15)
		pg.draw.rect(win,black,self.open_rect,2,border_radius = 15)
		
		win.blit(open_text,self.open_text_surf)
		pass
#____ UTILITY ___##
def fileExit(pos,draw):
		if File().exit.collidepoint(pos):
			draw = False
			print("fileexit")
		return draw
