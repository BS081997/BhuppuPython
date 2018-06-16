def tell_what_to_do(age):
	if person_is_old(age):
		print("You deserved to have a long vacation")
	else:
		print("Go to work")
def person_is_old(age):
	if (age<60):
		return True
	else:
		return False
tell_what_to_do(25)
tell_what_to_do(61)
