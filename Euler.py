def p1():
	total = 0
	for i in range(1000):
		if(i % 3 ==0 or i % 5 ==0):
			total += i˝
			
	
	print total
	
p1()


def p2():
	list = [1,2]
	done = False
	
	# While we are not above 4 million
	while(not done):
		
		# If the addition is less than 4 million, append it
		if(list[-1] + list[-2] <= 4000000):
			list.append(list[-1] + list[-2])
		# Else we are done finding the sequence
		else:
			done = True
	
	# Filter out those that are evently divisible by 2 and sum them
	print sum(filter(lambda x: (x % 2==0), list))
	
p2()


def p3():
	