print("Day2: 30 Days of python programming")
firstname = 'John'
lastname = 'Doe'
fullname = firstname + lastname
country = 'USA'
city = 'San Francisco'
age = 33
year = 2023
is_married = False
is_true = False
is_light_on = False
num_one, num_two, num_three = 1, 2, 3

print(type(firstname))
print(type(lastname))
print(type(fullname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(num_one))
print(type(num_two))
print(type(num_three))
print("num_one Variable: ", num_one)
print("num_two Variable: ", num_two)

print('Length of firstname: ', len(firstname))
print('Length of lastname: ', len(lastname))

num_one = 5
num_two = 4

print("Updated num_one Variable: ", num_one)
print("Update num_two Variable: ", num_two)

variable_sum = num_one + num_two
variable_diff = num_one - num_two
variable_mul = num_one * num_two
variable_div = num_one / num_two
variable_mod = num_one % num_two
variable_exp = num_one ** num_two
variable_floordiv = num_one // num_two

# Radius of Circle = 30 meters
radius = 30
area_of_circle = 3.14 * (radius**2)
circumfrence = 2 * (3.14*(radius))

print(area_of_circle)
print(circumfrence)

radius_from_user = input("Enter The Radius ")
input_from_user = float(radius_from_user)
print(input_from_user)
area = 3.14 * pow(input_from_user, 2)
circ = 2 * (3.14 * (input_from_user))

print(area)
print(circ)
help('keywords')
