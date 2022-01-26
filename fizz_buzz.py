def fizz_buzz():
	for i in range(1, 51):
		if i % 4 == 0 and i % 5 == 0:
			print(f'{i} is FizzBuzz')
		elif i % 4 == 0:
			print(f'{i} is Fizz')
		elif i % 5 == 0:
			print(f'{i} is Buzz')
		else:
			print(f'{i} is neither Fizz nor Buzz')
