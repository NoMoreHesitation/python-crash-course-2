import unittest

from city_country import get_city_and_country


# 测试test_city_country方法是否正确,需要先建类
class CityTestCase(unittest.TestCase):
	# 测试方法定义
	def test_get_city_and_country(self):
		city_name = get_city_and_country('shiyan', 'china')
		self.assertEqual(city_name, 'Shiyan, China')


if __name__ == '__main__':
	unittest.main()
