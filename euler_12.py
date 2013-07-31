from math import sqrt, ceil
factors_needed = 500
number_of_factors = 2
triangular = 1
val = -1
while number_of_factors < factors_needed :
	number_of_factors = 2
	val = (triangular * (triangular + 1) / 2)
	for i in range(2, int(sqrt(val))):
		if val % i == 0:
			number_of_factors += 2
	triangular += 1
print val
