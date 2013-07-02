from math import sqrt
num = 2000000
primes = [2, 3]
k = 5
while( primes[len(primes) - 1] < num):
	is_prime = True
	for prime in primes:
		if(prime > (sqrt(k))):
			break
		if(k%prime == 0):
			is_prime = False
			break
	if(is_prime):
		primes.append(k)
	k += 2
primes.pop()
print sum(primes)