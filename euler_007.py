num = int(raw_input("find prime number: "))
primes = [2, 3]
k = 5
while(len(primes) < (num)):
	is_prime = True
	for prime in primes:
		if(prime > (k ** .5)):
			break
		if(k%prime == 0):
			is_prime = False
			break
	if(is_prime):
		primes.append(k)
	k += 2
#print primes
print primes[num - 1]