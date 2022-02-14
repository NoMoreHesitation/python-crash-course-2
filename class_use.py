# 父类子类必须在一个文件中
class Restaurant:
	def __init__(self, name, type):
		"""
		构造方法
		:param name: 餐馆名字
		:param type: 餐馆类型
		"""
		self.name = name
		self.type = type

	def describe_restaurant(self):
		"""
		输出相关信息
		:return:
		"""
		print(f"Restaurant's name is {self.name}.")
		print(f"Restaurant's type is {self.type}.")

	def open_restaurant(self):
		"""
		营业中
		:return:
		"""
		print('Restaurant is open')


class IceCreamStand(Restaurant):
	def __init__(self, name, type, flavors):
		super().__init__(name, type)
		self.flavors = flavors

	def describe_ice_cream(self):
		print(f'We have several icecream,such as:{self.flavors}')


my_restaurant = Restaurant('Bawanglou', 'chinese spicy')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_icecreamstand = IceCreamStand('summerkiller', 'icecreamstand', ['vanilla', 'banana', 'strawberry'])
my_icecreamstand.describe_restaurant()
my_icecreamstand.describe_ice_cream()
my_icecreamstand.open_restaurant()
