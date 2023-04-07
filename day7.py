# sets
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}

age = [22, 19, 24, 25, 26, 24, 25, 24]


# Exercises: Level 1
# Find the length of the set it_companies
# Add 'Twitter' to it_companies
# Insert multiple IT companies at once to the set it_companies
# Remove one of the companies from the set it_companies
# What is the difference between remove and discard
lengthOfSet = len(it_companies)
it_companies_lt = list(it_companies)
it_companies_lt.insert(0, 'Twitter')
print(it_companies_lt)

it_companies.update(['Meta', 'Pintrest', 'Reddit'])
print(it_companies)
# Remove will create an error if you're trying to remove something that isn't there, discard() will not throw an error.
it_companies.remove('Meta')

# Exercises: Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# Join A and B
# Find A intersection B

A.union(B)
print(A)

isIntersection = A.intersection(B)

print(isIntersection)
# Is A subset of B
print(A.issubset(B))
print(B.issuperset(A))
# Are A and B disjoint sets
# Join A with B and B with A
# What is the symmetric difference between A and B
# Delete the sets completely


# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# Explain the difference between the following data types: string, list, tuple and set
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
