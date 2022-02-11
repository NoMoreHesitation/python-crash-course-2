# 生成名字列表，并输出相关问候语
names = ["ziyang", "fengyun", "yuchen", 'zhaoxin']
for i in names:
	message = f'Hi,{i}'
	print(message)

# 添加，插入，删除元素
names.append('furui')
names.insert(0, 'yoyo')
del names[0]
print(names)

# pop删除，返回删除的值，为了删除后继续用他
names_pop = names.pop()
print(names_pop)
print(names)

# 不确定位置，知道要删除什么值
names.remove('ziyang')
print(names)

# 根据字母排序，排完序永久改变顺序,这里都是小写可以这么排
names.sort(reverse=True)
print(names)

# sorted保留原来的顺序
print(sorted(names))
print(names)

# reverse调转列表
names.reverse()
print(names)
