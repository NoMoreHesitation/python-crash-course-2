# 利用range创建列表,左闭右开
numbers = list(range(1, 10))
print(numbers)

# min,max,sum方法
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 列表解析
square_numbers = [value ** 2 for value in range(1, 11, 2)]
print(square_numbers)

# 切片，左闭右开
print(square_numbers[0::2])

# 复制列表
square_same_numbers = square_numbers[:]
print(square_same_numbers)
