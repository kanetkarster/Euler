max_val = int(raw_input("Enter the maximum number: ")) + 1
print  sum(range(1,max_val)) ** 2 - sum( [x*x for x in range(1, max_val)])
