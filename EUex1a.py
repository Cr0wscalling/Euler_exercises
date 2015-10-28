# Find the sum of all the multiples of 3 or 5 below 1000 using Python
# setting variables and assigning values to the variables
number = 0 # WL-variable for natural numbers
#number = int(number) 
mup3n5 = 0 # = 0 # variable for multiples of 3 & 5 for natural numbers < 1000 *probably don't need this with built in fxn

while number < 999: #WL
	number = number + 1 #WL

	if number % 3 == 0 or number % 5 == 0: # boolean argument
		mup3n5 = mup3n5 + number #summation of multiples
	else:
		continue # skips lines without multiples
print mup3n5 # out put of loop