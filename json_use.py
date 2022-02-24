import json

filename = 'user_name.json'
try:
	with open(filename) as f:
		username = json.load(f)
except FileNotFoundError:
	username = input('tell me your name:')
	with open(filename, 'w') as f:
		json.dump(username, f)
		print(f'We will remember you when you come back,{username}')
else:
	print(f'Welcome back,{username}!')
