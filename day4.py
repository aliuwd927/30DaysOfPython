'''
string1 = 'Thirty '
string2 = 'Days '
string3 = 'Of '
string4 = 'Python '


print(string1 + string2 + string3 + string4)
'''


company = 'Coding For All'
# print(company)
# print(len(company))
# print(company.upper())
# print(company.lower())
# print(company.capitalize())
# print(company.title())
# print(company.swapcase().title().capitalize())
first_word = company[0:6]
# print(first_word)
# print(company.find(first_word))
# print(company.rfind(first_word))
# print(company.index('in'))
# print(company.startswith(first_word))
#print(company.replace('Coding', 'Python'))
company = company.replace("Coding", "Python")
# print(company)
company = company.replace("All", "Everyone")
#company = company.split(' ')
# print(type(company))  # This is a list, NOT a tuple

# Python For Everyone
faamigo = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
# print(faamigo.split(','))

# print(company[0])
# print(company[-1])
# print(company[10])
print(company[0] + company[7] + company[11])


sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.index('because'))

print(sentence.rfind('because'))
print(sentence[31:54])

sub_string = 'Python'
sub_string_two = 'python'

print(company.index(sub_string))
# print(company.index(sub_string_two))

trailing_space = ' Coding For All '
print(trailing_space)
print(len(trailing_space))
trailing_space = trailing_space[1:-1]
print(trailing_space)

variable_one = '30DaysOfPython'
variable_two = 'thirty_days_of_python'

print(variable_one.isidentifier())
print(variable_two.isidentifier())

join_this = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

print(' '.join(join_this))

use_new_line = 'I am enjoying this challenge.\nI just wonder what is next.'

print(use_new_line)

use_tab = 'Name\t\tAge\tCountry\tCity'
use_tab_Data = 'Asabeneh\t250\tFinland\tHelsinki'

print(use_tab)
print(use_tab_Data)

radius = 10
area = 3.14 * radius ** 2
sentence = 'The area of a circle with radius %s is %s meters square.' % (
    radius, area)

print(sentence)

sentence_two = 'The area of a circle with radius {} is {} meters square'.format(
    radius, area)

print(sentence_two)


operand_one = 8
operand_two = 6

print('{} + {} = {}'.format(operand_one, operand_two, operand_one + operand_two))
print('{} - {} = {}'.format(operand_one, operand_two, operand_one - operand_two))
print('{} * {} = {}'.format(operand_one, operand_two, operand_one * operand_two))
print('{} / {} = {}'.format(operand_one, operand_two, operand_one / operand_two))
print('{} % {} = {}'.format(operand_one, operand_two, operand_one % operand_two))
print('{} // {} = {}'.format(operand_one, operand_two, operand_one // operand_two))
print('{} ** {} = {}'.format(operand_one, operand_two, operand_one ** operand_two))
