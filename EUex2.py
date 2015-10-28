# Find the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million.

i = 0 
j = 1
k = 0
fib_term = 0
even_fib_term = 0
# loop to build the Fibonacci numbers
while fib_term < 4000000: # WL definate loop
	k = i + j
	i = j
	j = k
 	fib_term = k # fib_term
 	#print fib_term
 	
	if fib_term % 2 == 0:
		even_fib_term = even_fib_term + fib_term
	else:
		continue
print even_fib_term
