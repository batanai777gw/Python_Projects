# we learned 3 types of data in python

#int - 10
#String - "Batanai"
#Boolean - True

birth_year = input("Enter your birth year: ")
#Error was casued because input value are strings p py
#"1982" Pycan't sub string from int data type 1982 [different]
# Converting string to integer - in Py - built in function function to conver our variable
# so solve this problem[type cnverstion] age = 2024 - birth_year, we us the Fn below
age = 2024 - int(birth_year) # return correct output
print(age)

# another build in Fn is float() 
#   -> used to convert a value to a floating point number
#       -> a flating point num is a num with a decimal point[in python & other _lang]
# 10 is an integer, and 10.1 is a  float
# Type Convertions we have int(), float(), bool(), & str()
# These are the the build in Fn 4 converting the type of our variables