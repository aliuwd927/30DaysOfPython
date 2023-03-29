#Declare an empty list
lstFunction = list()
lstDeclaration = []

print(type(lstFunction))
print(type(lstDeclaration))

#Declare a list with more than 5 items

listOf5 = ['item1', 'item2', 'item3', 'item4', 'item5']

#Find the legnth of your list

print(len(listOf5))

#Get the first item, the middle and last item of the list

print(listOf5[0])
print(listOf5[2])
print(listOf5[-1])

lastIndex = len(listOf5)-1
print(listOf5[lastIndex])

#Declare a list called mixed_data_types, put (name,age,height,marital status,address)

mixed_data_type = ['John',33,"5'7",'single', "123 Fake Street"]

#Declare a list variable named it_companies and assign inital value Facebook, Google, Microsoft, Apple, IBM, Oracle, and Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(mixed_data_type)
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])


#print the list after modifying one of the companies

it_companies[0] = 'Reddit'

print(it_companies)
it_companies.append('Facebook')
print(it_companies)

it_companies.insert(3,'Meta')
print(it_companies)

it_companies[3] = it_companies[3].upper()
print(it_companies)


it_companies_hash = '#; '.join(it_companies)
print(it_companies_hash)

print('IBM' in it_companies)

it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)

first_three = it_companies[0:3]
print(first_three)
last_three = it_companies[6:9]
print(last_three)
middle_three = it_companies[3:6]
print(middle_three)

del it_companies[0]
del it_companies[-1]
del it_companies[3:6]

print(it_companies)

it_companies.clear()
print(it_companies)
del it_companies


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end

full_stack.append('Python')
full_stack.append('SQL')
print(full_stack)

#Excercise 2
