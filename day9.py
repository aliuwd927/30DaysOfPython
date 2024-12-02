person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
             }
    }

#  Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if(len(person) > 0):
    print(person['skills'][2])
else:
    print("None")


#  Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if(len(person)>0 and person['skills'][-1] == 'Python'):
    print(person['skills'][-1])
else:
    print("None")


#  If a person skills has only JavaScript and React, print('He is a front end developer')...
#   if the person skills has Node, Python, MongoDB, print('He is a backend developer')...
#   if the person skills has React, Node and MongoDB, Print('He is a fullstack developer')...
#       else print('unknown title') - for more accurate results more conditions can be nested!

if(person['skills'][0] == "JavaScript" and person['skills'][1] == "React"):
    print('He is a front end developer')
elif (person['skills'][2] == 'Node' and person['skills'][4] == 'Python' and person['skills'][3] == 'MongoDB'):
    print('He is a backend developer')
elif (person['skills'][1] == "React" and person['skills'][2] == 'Node' and person['skills'][3] == 'MongoDB'):
    print('He is a fullstack developer')
else:
    print('unknown title')




#  If the person is married and if he lives in Finland, print the information in the following format:

if(person['is_marred'] == True and person['country'] == "Finland"):
    print('{} {} lives in {}. He is married'.format(person['first_name'],person['last_name'],person['country']))
else:
    print("None")