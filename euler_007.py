import time
from math import sqrt
time.clock()
num = 10001
primes = [2, 3]
k = 5
while(len(primes) < (num)):
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
#print primes
print time.clock()
print primes[num - 1]