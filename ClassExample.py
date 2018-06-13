class Car:
	def __init__(self,x):	#constructor	
		self.x=x
	
	def turn_left(self, x=20):
		self.x = x
		print("I'm from turn left")
	
	def turn_right(self,x=10):
		self.x = x
		print("I'm from turn right")
	
	def accelerate(self,x=50):
		self.x=x
		print("I'm from accelerate")

	def slow_down(self,x=100):
		self.x=x
		print("I'm from slow down")

	def open_a_window(self,x=60):
		self.x=x
		print("I'm from open a window")

Car(77).turn_left()
print(Car(77).x)

Car(10).turn_right()
print(Car(10).x)

Car(50).accelerate()
print(Car(50).x)
