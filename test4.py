for i in range(5):
	try:
		print(i / 1)
	except ZeroDivisionError as e:
		print(e, "--> Division by 0 is not allowed")
	finally:
		print("I am getting printed")