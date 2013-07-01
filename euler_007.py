num = int(raw_input("find prime number: "))
k = 3
primes = [2]

while(len(primes) < (num)):
	is_prime = True
	for prime in primes:
		if((k%prime == 0) and (prime <= (k ** .5))):
			is_prime = False
			break
	if(is_prime):
		primes.append(k)
	k += 1
#print primes
print primes[num - 1]
