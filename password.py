import random
import string


def randomPassword(n):
	randLetter = string.ascii_letters + string.digits

	password = ''.join(random.choice(randLetter) for i in range(n))
	print(password)

num = input("Password Length ")
num = int(num)
randomPassword(num)
