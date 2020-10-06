import random

Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   

try:
	n=int(input("Enter the no. of digits required in pin in number "))
	pin=''
	for i in range(n):
		pin=pin+random.choice(Digits)

	print(pin)
	 
except ValueError:
	print("PLease enter a number only")

except:
	print('There has been some error')



