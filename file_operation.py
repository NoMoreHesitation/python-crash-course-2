# 注意编码，with在不在需要访问后关闭文件
# 一次读完整个文件
with open('test_input.txt', encoding='utf-8') as file_input:
	content = file_input.read()
	print(content.rstrip())

# 一次打印一行
with open('test_input.txt', encoding='utf-8') as file_input:
	for contents in file_input:
		print(contents.rstrip())

# 存入中间变量，后面再用
with open('test_input.txt', encoding='utf-8') as file_input:
	lines = file_input.readlines()
file_string = ''
for line in lines:
	file_string += line.strip()
print(file_string)
