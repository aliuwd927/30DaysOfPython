# Create an empty dictionary called dog
dog = {}

# Add name,color,breed,legs,age to dog dictionary
dog['name'] = 'Fido'
dog['color'] = 'Brown'
dog['breed'] = 'Terrier'
dog['legs'] = 4
dog['age'] = 15


# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {}
student['first_name'] = 'John'
student['last_name'] = 'Smith'
student['gender'] = 'Male'
student['age'] = '35'
student['marital_status'] ='Single'
student['skills'] = ['Problem Solving','Analytical','Creative']
student['country'] = 'United States'
student['city'] = 'Faker'
student['address'] = {
    'house_number': 123,
    'street_name': 'Fake Street',
    'city': student['city'],
    'zip_code':123456
}

# Get the length of the student dictionary
print(len(student['address']))

# Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))
print('skills' in student)

# Modify the skills values by adding one or two skills
student['skills'].append('Public Speaking')
student['skills'].append('Writing')
print(student['skills'])

# Get the dictionary keys as a list
print(student.keys())


# Get the dictionary values as a list
print(student.values())


# Change the dictionary to a list of tuples using items() method
dog_list_of_tuples = list(dog.items())
print(dog_list_of_tuples)
print(type(dog_list_of_tuples))
# Delete one of the items in the dictionary
del dog['legs']


# Delete one of the dictionaries
del dog

