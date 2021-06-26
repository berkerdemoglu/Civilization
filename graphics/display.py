from abc import abstractmethod, ABC

import pygame as pg

from .color import ColorTuple, BLACK
from .utils import time_ns, time_ms


class DisplaySettings:

	def __init__(self, width: int, height: int, title: str, fps: int):
		if not self._sanitize_display_settings(width, height, title, fps):
			raise ValueError

		self.width = width
		self.height = height
		self.title = title
		self.fps = fps

	def _sanitize_display_settings(self, width, height, title, fps) -> bool:
		if type(width) != int:
			return False
		if type(height) != int:
			return False
		if type(title) != str:
			return False
		if type(fps) != int:
			return False

		return True


class Display(ABC):

	def __init__(self, settings: DisplaySettings):
		self.settings = settings
		self.is_running: bool = False

		pg.init()

		screen_dimensions = self.settings.width, self.settings.height
		self.surface = pg.display.set_mode(screen_dimensions)
		pg.display.set_caption(self.settings.title)

	def start(self) -> None:
		if self.is_running: return
		self.is_running = True

		update_nano_frequency = 1000000000 / self.settings.fps
		delta = 0

		now_nano: int
		last_nano = time_ns()

		# FPS related
		drawn_frames = 0
		now_milli = time_ms()

		while self.is_running:
			now_nano = time_ns()
			delta += (now_nano - last_nano) / update_nano_frequency
			last_nano = now_nano

			while delta >= 1:
				self.poll_events()

				self.update()
				delta -= 1

				self.render()
				pg.display.flip()
				drawn_frames += 1

			if time_ms() - now_milli > 1000:
				now_milli += 1000
				pg.display.set_caption(f'{self.settings.title} - {drawn_frames} FPS')
				drawn_frames = 0

	@abstractmethod
	def poll_events(self) -> None:
		"""Check events regarding the window."""
		raise NotImplemented

	@abstractmethod
	def render(self) -> None:
		"""Draw/render objects to the screen."""
		self.surface.fill(BLACK)

	@abstractmethod
	def update(self) -> None:
		"""Update the game state."""
		raise NotImplemented
