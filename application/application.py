from sys import exit as sysexit
import pygame as pg

from graphics import Display
from .constants import DISPLAY_SETTINGS
from world import World


class Application(Display):

	def __init__(self):
		super().__init__(DISPLAY_SETTINGS)

		self.world = World()

	def poll_events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sysexit(1)

	def render(self):
		super().render()

		self.world.render(self.surface)

	def update(self):
		pass
