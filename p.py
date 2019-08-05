import random

greet = ['hi','hello']
greet2 = ['how are you']
while True:
	ask = input(">>>")
	if ask in greet:
		ran = random.choice(greetR)
		print(ran)