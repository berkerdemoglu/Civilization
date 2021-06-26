from abc import abstractmethod, ABC

import pygame as pg

from .color import ColorTuple


class BaseRenderable(ABC):
	"""
	An abstract class that any object can inherit 
	from if they can/should be rendered to the screen.
	"""

	@abstractmethod
	def render(self, surface: pg.Surface) -> None:
		"""Render the object to the screen."""
		raise NotImplemented


class ImageRenderable(BaseRenderable):

	def __init__(self, image: pg.Surface):
		self.image = image
		self.rect = image.get_rect()

	def render(self, surface):
		surface.blit(self.image, self.rect)


class RectRenderable(BaseRenderable):

	def __init__(self, color: ColorTuple):
		self.color = color

	@abstractmethod
	def get_rect(self, surface: pg.Surface) -> pg.Rect:
		raise NotImplemented

	def render(self, surface):
		pg.draw.rect(surface, self.color, self.get_rect(surface))
