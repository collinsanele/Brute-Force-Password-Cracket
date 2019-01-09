import itertools
import string

def pwd_crack(pwd):
	chars = string.ascii_lowercase + string.digits
	count =0
	for pwd_length in range(1, 11):
		for guess in itertools.product(chars, repeat=pwd_length):
			guess = ''.join(guess)
			count += 1
			if guess == pwd:
				return f'password is {guess} and was found after {count} times'
			#print(guess, count)
			
			
			
print(pwd_crack('home'))















