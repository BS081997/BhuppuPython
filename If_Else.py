def drive(car_speed):
	if car_speed>200:
		print("You are insane, man.!!!")
	elif car_speed>100:
		print("Too fast....")
	elif car_speed>70 and car_speed<80:
		print("The optimal speed for your car...")
	else:
		print("You are driving below the speed limit..Well done.")
drive(75)

def compare(a):
	
	if a<1:
		print("Big")
	elif a<5:
		print("Really big")
	elif a==10:
		print("Approaching enormity")
	elif a>10:
		print("Enormous.!")
compare(0)
compare(2)
compare(10)
compare(12)

