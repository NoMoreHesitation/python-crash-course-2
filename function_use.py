# 默认参数为‘China’,放最后
def describe_city(city, country='China'):
	"""
	打印关于城市国家对应信息
	:param city:
	:param country:
	:return:
	"""
	print(f'{city} is in {country}')


# 传递任意数量的实参,会自动建立一个元组，也放在最后
def favorite_languages(*languages):
	"""
	打印喜欢的语言
	:param languages:
	:return:
	"""
	for language in languages:
		print(f'I like {language}')


# 任意数量实参，但不知道是什么，比如输入键值对,自动为user_info建立字典
def build_profile(first_name, last_name, **user_info):
	"""
	打印相关信息，但不知道参数将会输入什么
	:param first_name:
	:param last_name:
	:param user_info:
	:return:
	"""
	user_info['first_name'] = first_name
	user_info['last_name'] = last_name
	return user_info


describe_city('Shiyan')
describe_city('Darmstadt', 'Germany')
favorite_languages('python', 'java', 'C')
user = build_profile('Sheep', 'Orange', location='Shiyan', language='chinese')
print(user['location'])
