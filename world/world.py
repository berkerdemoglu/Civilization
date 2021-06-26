from typing import List

import pygame as pg

from .tile import Tile, TileType
from graphics.renderable import BaseRenderable


class World(BaseRenderable):

	def __init__(self):
		self.tiles: List[Tile] = list()
		self.generate_world()

	def generate_world(self):
		self.tiles.append(Tile(TileType.GRASSLAND, (10, 10)))

	def render(self, surface: pg.Surface) -> None:
		for tile in self.tiles:
			tile.render(surface)
