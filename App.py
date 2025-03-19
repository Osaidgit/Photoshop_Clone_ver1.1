import pygame as pg
from ui.func import *
from core.file import *

class Main:
	def __init__(self):
		self.menu = Menu()
		self.file = File()
		self.page = Page()
		self.exit = Exit()
		self.shape = Shapes()
		
		
		# Shapes drawing states #
		self.shapes ={
		"box":False,
		"circle":False,
		"tri":False,
		"hexa":False,
		"ecs":False}
		
		# Dragging states #
		self.run = True	
		self.is_dragging = False
		self.drag_target = None
		self.draw_files = False	
	#_________________________
	def check_events(self):
		#__Method variables
		self.pos = pg.mouse.get_pos()
	
		for i in pg.event.get():
			if i.type == pg.QUIT:
				self.run = False
			#Handle button clicks
			if i.type == pg.MOUSEBUTTONDOWN:
				self.pos
				self.run = exit(self.pos,self.run)
				self.draw_files = fileExit(self.pos,self.draw_files)
				self.handle_button_clicks()
				self.handle_shape_selection()
			# Handle Dragging #
			if i.type == pg.MOUSEMOTION and self.is_dragging:
					self.handle_dragging()
									
			# Stop Dragging
			if i.type == pg.MOUSEBUTTONUP:
				self.is_dragging = False
				self.drag_target =None
	def handle_button_clicks(self):
		if self.menu.btn1.collidepoint(self.pos):
				self.shapes["box"] = True
			#For Butn2
		if self.menu.btn2.collidepoint(self.pos):
				print("btn2")
				self.shapes["circle"] = True
			# For btn3
		if self.menu.btn3.collidepoint(self.pos):
				print("btn3")
				self.shapes["tri"] = True
			#For btn4
		if self.menu.btn4.collidepoint(self.pos):
				print("btn4")
				self.shapes["hexa"] = True
		if self.menu.btn5.collidepoint(self.pos):
			print("btn5")
			self.shapes["ecs"]  = True
		if self.menu.btn8.collidepoint(self.pos):
			self.handle_files()
			print("btn8")
	def handle_files(self):
		 self.draw_files = True			
		
	def handle_shape_selection(self):
			if self.shape.circle.rect.collidepoint(self.pos):
				self.drag_target = self.shape.circle.rect
			if self.shape.box.box.collidepoint(self.pos):
				self.drag_target = self.shape.box.box
			if self.shape.tri.rect.collidepoint(self.pos):
				self.drag_target = self.shape.tri.rect
			if self.shape.ecs.rect.collidepoint(self.pos):
				self.drag_target = self.shape.ecs.rect
			if self.shape.hexa.rect.collidepoint(self.pos):
				self.drag_target =self.shape.hexa.rect
			self.is_dragging = bool(self.drag_target)
			
	def handle_dragging(self):
			if self.drag_target:
				self.drag_target.center  = self.pos
			
	def draw(self):
		win.fill(GREY)
		
		pg.draw.rect(win,red,win_rect,2)	
		self.page.draw()
		self.menu.draw()	
		Show_pos()
		self.exit.draw()
		self.file.draw_icon()
		# Draw shapes based on State #
		if self.shapes["hexa"]:
			self.shape.hexa.draw()
		if self.shapes["tri"]:
			self.shape.tri.draw()
		if self.shapes["circle"]:
				self.shape.circle.draw()
		if self.shapes["box"]:
				self.shape.box.draw()
		if self.shapes["ecs"]:
				self.shape.ecs.draw()
		# Draw file window based on State #
		if self.draw_files:
			self.file.draw_window()
						
	def update(self):
	#	print(clock.get_fps())	
		pg.display.update(),clock.tick(fps)
	