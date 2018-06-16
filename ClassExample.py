class Car:
	def __init__(self):	#constructor	
		self.x = 70
		print("I'm from constructor")
	
	def turn_left(self, x=20):
		self.x = x
		print("I'm from turn left")
	
	

var = Car()
print(var.x)

(var.turn_left())
print(var.x)

