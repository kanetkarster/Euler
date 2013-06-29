def is_palindrome(val):
	if(str(val) == str(val)[::-1]):	#reverses via Slicing
		return True
	return False

def is_product_palindrome(pal, digits):
	for i in range(2, 10 ** digits):
		if((pal%i == 0) and (len(str((pal/i))) == digits)):
			return True
	return False

def find_palindrome(digits):
	LARGEST_PRODUCT_PALINDROME = -1
	for pal in range(10 ** ((2 * digits) -1), 10 ** (2 * digits)):
		if(is_palindrome(pal)):
			if(is_product_palindrome(pal, digits)):
				LARGEST_PRODUCT_PALINDROME = pal
	return LARGEST_PRODUCT_PALINDROME
print find_palindrome( int(raw_input("Enter the palindrome's factor's digits: ")))
