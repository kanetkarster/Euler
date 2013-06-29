large_number = 600851475143
largest_prime_factor = -1
i = 2;
while(i <= large_number):
	print large_number
	if(large_number%i == 0):
		large_number /= i
		largest_prime_factor = i
	else:
		i += 1

print largest_prime_factor