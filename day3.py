import math

age = 30
height = 5.7

# when using complex number, make sure you use j
complex_num = 1 * (1 + 1j)

# Write a script that prompts the user to enter base and height of the triangle and
# calculate an area of this triangle (area = 0.5 x b x h).
#half_base = 0.5
#base = float(input("Enter Base: "))
#height = float(input("Enter Height: "))
#area = half_base*(base*height)

# print(area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle.
# Calculate the perimeter of the triangle (perimeter = a + b + c).

#side_a = float(input("Enter Size for Side A: "))
#side_b = float(input("Enter Size for Side B: "))
#side_c = float(input("Enter Size for Side C: "))
#perimeter = side_a + side_b + side_c

# print(perimeter)

# Get length and width of a rectangle using prompt.
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

#rectangle_length = float(input("Enter Length of Rectangle: "))
#rectangle_width = float(input('Enter Width of Rectangle: '))
#area_of_rectangle = rectangle_length * rectangle_width

# print(area_of_rectangle)

# Get radius of a circle using prompt.
# Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
#pi = 3.14
#get_radius = float(input('Enter Radius of Circle: '))
#area_of_circle = pi * pow(get_radius, 2)
#circumfrence_of_circle = 2 * (pi * get_radius)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2

# Slope Intercept
#y = 2j - 2

# Find the slope and Euclidean distance between point (2, 2) and point (6,10)
#x1 = 2
#x2 = 6
#y1 = 2
#y2 = 10

#slope = (y2 - y1)/(x2-x1)
#euclidean_distance = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

#print("Slope: ", slope)
#print("Eucliden: ", euclidean_distance)

# print(slope == euclidean_distance)  # Should return false


# Calculate the value of y (y = x^2 + 6x + 9).
# Try to use different x values and figure out at what x value y is going to be 0.

#x = int(input('Enter Number: '))

#is_zero = pow(x, 2) + (6*x) + 9

# print(is_zero == 0)  # -3 should equal true


# Find the length of 'python' and 'dragon' and make a falsy comparison statement.

#len_of_python = len('python')
#len_of_dragon = len('dragon')

# print(len_of_python == len_of_dragon)  # should return true


# Use and operator to check if 'on' is found in both 'python' and 'dragon'

#print('on' in 'python' and 'on' in 'dragon')


# I hope this course is not full of jargon.
# Use in operator to check if jargon is in the sentence.

#print('jargon' in 'I hope this course is not full of jargon.')


# There is no 'on' in both dragon and python

#print('on'not in 'python' and 'on' not in 'dragon')


# Find the length of the text python and convert the value to float and convert it to string

#len_of_python2 = str(float(len('python')))

# print(type(len_of_python2))
# print(len_of_python2)

# Even numbers are divisible by 2 and the remainder is zero.
# How do you check if a number is even or not using python?

#is_zero_input = int(input('Enter Number: '))
#is_zero = (is_zero_input % 2)

#print(is_zero == 0)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

#reg_division = 7 / 3
#floor_division = 7 // 3

# print(reg_division)
# print(floor_division == int(2.7))
# print(int(2.7))


# Check if type of '10' is equal to type of 10

# print(type('10') == type(10))

# Check if int('9.8') is equal to 10

# print(int(9.8))


# Write a script that prompts the user to enter hours and rate per hour.
# Calculate pay of the person?

#user_hours = float(input('Enter your hours: '))
#user_rate_per_hour = float(input('Enter your rate per hour: '))
#weekly_earnings = user_hours * user_rate_per_hour

# print(weekly_earnings)


# Write a script that prompts the user to enter number of years.
# Calculate the number of seconds a person can live. Assume a person can live hundred years

#user_years = int(input("Enter the number of years: "))
#one_year_in_seconds = 31536000
#years_lived = user_years * one_year_in_seconds

# print(years_lived)

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)
