# 字典的创建，朴实无华
person = {'name': 'Bob', 'age': 25, 'city': 'Chengdu'}
print(person['age'])

# 不确定键值是否存在，用get
person_gender = person.get('gender', 'agender')
print(person_gender)

# 遍历字典
for key, value in person.items():
	print(f'Key:{key}')
	print(f'Value:{value}')
