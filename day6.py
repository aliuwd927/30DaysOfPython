# Create an empty tuple
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# Join brothers and sisters tuples and assign it to siblings
# How many siblings do you have?
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# Unpack siblings and parents from family_members

empty_tuple = tuple()

listOfBrothers = ("Jim", "John", "James")
listOfSisters = ("Jane", "Jill", "Janet")

listOfSiblings = listOfBrothers + listOfSisters  # This is a tuple
print(listOfSiblings)
print(type(listOfSiblings))
lengthOfSiblings = len(listOfSiblings)

listOfFamily = list(listOfSiblings)

listOfFamily.insert(0, 'Jimmy')
listOfFamily.insert(1, "Joan")
print(listOfFamily)
print(type(listOfFamily))

listOfParents = listOfFamily[0:2]
print(listOfParents)


# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
# Change the about food_stuff_tp tuple to a food_stuff_lt list
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# Slice out the first three items and the last three items from food_staff_lt list
# Delete the food_staff_tp tuple completely
# Check if an item exists in tuple:

fruits = ('Apples', 'Oranges', 'Cherry')
vegetables = ('Cabbage', 'Broccolis', 'tomato')
animal_products = ('Milk', 'Eggs', 'Butter')

food_stuff_tp = fruits + vegetables + animal_products

#('Apples', 'Oranges', 'Cherry', 'Cabbage', 'Broccolis', 'tomato', 'Milk', 'Eggs', 'Butter')
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)

middle_lt = list(food_stuff_tp[4:5])
print(middle_lt)

first_three = food_stuff_lt[0:4]
last_three = food_stuff_lt[6:9]

print(last_three)

del food_stuff_tp


# Check if 'Estonia' is a nordic country

# Check if 'Iceland' is a nordic country
# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

checkEstonia = ('Estonia' in nordic_countries)
checkIceland = ('Iceland' in nordic_countries)
print(checkEstonia)
print(checkIceland)
