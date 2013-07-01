lim = int(raw_input("Enter the sum of the pythagorean triplet: "))
for a in range(1, lim/3):
	for b in range(1, lim/2):
		c = lim - a - b
		if(a*a + b*b) == (c*c):
			print a * b * c