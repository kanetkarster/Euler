max = 20
def reduce(val):
	for i in range(2, max):
		print val
		boo = True
		for j in range(2, max):
			if((val / i)%j != 0):
				boo = False
		if(boo):
			val /= i
	return val
def multiply(val):
	for i in range(2, max):
		if(val%i != 0):
			return multiply(val*i)
	return reduce(val)
print multiply(1)
#232792560
