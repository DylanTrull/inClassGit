import random
import string

def randomPassword(n):
	randLetter = string.ascii_letters

	password = ''.join(random.choice(randLetter) for i in range(n))
	print(password)

randomPassword(10)
