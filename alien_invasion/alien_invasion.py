import sys
import pygame
from settings import Settings


class AlienInvasion:
	"""
	管理游戏资源和行为
	"""

	def __init__(self):
		"""
		初始化游戏并创建游戏资源
		"""
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		# RGB色光三原色
		self.bcakground_color = self.settings.background_color
		pygame.display.set_caption('Alien Invasion')

	def run_game(self):
		"""
		游戏的主循环
		:return:
		"""
		while True:
			# 监视键盘鼠标
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			# 每次绘制新屏幕，擦去旧屏幕
			self.screen.fill(self.bcakground_color)
			pygame.display.flip()


if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()
