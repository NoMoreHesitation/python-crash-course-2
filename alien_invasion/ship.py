import pygame


class Ship:
	"""
	飞船类
	"""

	def __init__(self, ai_game):
		"""
		初始化飞机，按矩形进行编程
		:param ai_game: 屏幕
		"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		# 加载飞机图片
		self.image = pygame.image.load('image/ship.bmp')
		self.rect = self.image.get_rect()
		# 新飞船放到底部中央
		self.rect.midtop = self.screen_rect.midtop

	def blit(self):
		"""
		指定位置绘制飞机
		:return:
		"""
		self.screen.blit(self.image, self.rect)
