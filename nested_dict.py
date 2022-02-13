# 列表嵌套字典
persons = []
for persons_number in range(20):
	dict_person = {'name': 'shaoSir', 'age': 25, 'gender': '18'}
	persons.append(dict_person)

for person in persons[:5]:
	print(person)

# 字典嵌套列表
shao_sir = {'name': 'shaoSir', 'languages': ['Ruby', 'python', 'C']}
print(shao_sir['languages'])

# 字典里嵌套字典
friends = {
	'shao': {'name': 'shaoSir', 'location': 'Wuhan'},
	'yuchen': {'name': 'yuchen', 'location': 'Nanjing'},
	'furui': {'name': 'chef', 'location': 'Shenyang'}
}
for name, info in friends.items():
	print(f'Hi, user_name {name}')
	print(f'\t you are living in {info["location"]}')
