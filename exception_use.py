# try-except-else 正常情况try-else，异常情况try-except
# 静默失败用pass语句
def divide_operation():
	"""
	简单的除法运算
	:return:
	"""
	try:
		number1 = int(input('please enter first number:'))
		number2 = int(input('please enter second number:'))
		a = number1 / number2
	except ZeroDivisionError:
		print('you cannot divide by 0')
	except ValueError:
		print('please enter number instead of character')
	else:
		print(a)


divide_operation()
