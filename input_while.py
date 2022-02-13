prompt = 'Tell me something:'
prompt += '\n Enter "quit" to end the program.'
message = ''
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message)
