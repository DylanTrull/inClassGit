def divs(n):
	i = 1
	while i <= n:
		if(n % i == 0):
			print(i)
		i += 1


num = input("Enter a Number ")
num = int(num)
divs(num)