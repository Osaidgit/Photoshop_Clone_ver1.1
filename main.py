import unittest
import pygame as pg
from App import *
if __name__ == '__main__':
	app =Main()
	while run:
		app.draw()
		app.check_events()
		app.update()
	



