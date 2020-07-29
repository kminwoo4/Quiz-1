def isItPrime (x): 
	for i in range (2,int(x**0.5)+1): #why did you int(x**0.5)+1 
		if x%i == 0: 
			return False 
	return True 
	
print isItPrime (8)

def nthPrime(n): 
	if n == 1: 
		return 2 
	counter = 1  # why did you start the number 1 and counter 1.
	number = 1 
	while (counter < n) :
		number += 1
		if isItPrime (number): 
			counter += 1  
			
	return number 

print nthPrime (8)

def testfunc():
	print("testing thingy")
	assert(isItPrime(3)==True)
	assert(isItPrime(6)==False)
	assert(isItPrime(9)==False)
	assert(isItPrime(-7)==False)
	assert(isItPrime(17)==True)
	assert(isItPrime(0)==False)
	assert(isItPrime(1)==False)
	print ('passed')
print testfunc()

def testfunc():
	print("testing thingy")
	assert(nthPrime(4)==7)
	assert(nthPrime(5)==11)
	assert(nthPrime(1)==2)
	assert(nthPrime(2)==3)
	assert(nthPrime(10)==29)
	print ('passed')
print testfunc()

# nthPrime()




# def leastFrequentLetters (x): 
# 	x = x.lower().replace()
# 	counter = 0 
# 	letter = ''
# 	string = ''



