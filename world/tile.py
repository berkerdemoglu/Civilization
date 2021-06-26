from enum import Enum
from typing import Tuple

import pygame as pg

from graphics import RectRenderable, ColorTuple


class TileType(Enum):
	GRASSLAND = {
		'name': 'grassland',
		'color': ColorTuple(48, 179, 55),
		'food': 3
	}
	PLAINS = {
		'name': 'plains',
		'color': ColorTuple(126, 135, 81),
		'food': 2
	}


class Tile(RectRenderable):
	TILE_SIZE = 50

	def __init__(self, tile_type: TileType, pos: Tuple[int, int]):
		super().__init__(tile_type.value['color'])

		self.tile_type = tile_type
		self.tile_dict = self.tile_type.value

		self.pos = pos

	def get_rect(self, surface: pg.Surface) -> pg.Rect:
		return pg.Rect(*self.pos, Tile.TILE_SIZE, Tile.TILE_SIZE)
