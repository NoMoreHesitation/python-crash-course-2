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

# 写入文件，w表示写入,数字要转换
file_name = 'test_output.txt'
with open(file_name, 'w') as file_output:
	file_output.write('I love programming.\n')
	file_output.write(str(2)+'\n')
# 附加模式，在原来文件基础上添加
with open(file_name, 'a') as file_add:
	file_add.write('I love playing computer games!')
