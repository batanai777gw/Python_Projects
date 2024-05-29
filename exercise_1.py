# Exercise 1: variables
# - We check in a patient named John Smith
# - He is 20 years old.
# - He is a new patient.
# declare variable to store these values

# Solution - Batanai Gwanyanya(Python Developer)

first_name = "John"
last_name = "Smith"
age = str(20) 
is_new = str(True)

# age = 20 -> TypeError: can only concatenate str (not "int") to str
# is_new = True -> Solution: convert int type to String

print("Patient Information:")
print("----------------------")
print("First Name: " + first_name)
print("Last Name: " + last_name)
print("Age: " + age)
print("New Patient: " + is_new)