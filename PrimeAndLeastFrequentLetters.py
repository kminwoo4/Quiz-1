def isItPrime (x): 
	for i in range (2,int(x**0.5)+1): 
		if x%i == 0: 
			return False 
	return True 
	
print isItPrime (8)

def nthPrime(n): 
	if n == 1: 
		return 2 
	counter = 1 
	number = 1 
	while (counter < n) :
		number += 1
		if isItPrime (number): 
			counter += 1  
			
	return number 

print nthPrime (8)

# nthPrime()




# def leastFrequentLetters (x): 
# 	x = x.lower().replace()
# 	counter = 0 
# 	letter = ''
# 	string = ''



