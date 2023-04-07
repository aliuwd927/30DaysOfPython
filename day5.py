# Declare an empty list
lstFunction = list()
lstDeclaration = []

print(type(lstFunction))
print(type(lstDeclaration))

# Declare a list with more than 5 items

listOf5 = ['item1', 'item2', 'item3', 'item4', 'item5']

# Find the legnth of your list

print(len(listOf5))

# Get the first item, the middle and last item of the list

print(listOf5[0])
print(listOf5[2])
print(listOf5[-1])

lastIndex = len(listOf5)-1
print(listOf5[lastIndex])

# Declare a list called mixed_data_types, put (name,age,height,marital status,address)

mixed_data_type = ['John', 33, "5'7", 'single', "123 Fake Street"]

# Declare a list variable named it_companies and assign inital value Facebook, Google, Microsoft, Apple, IBM, Oracle, and Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon']

print(mixed_data_type)
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])


# print the list after modifying one of the companies

it_companies[0] = 'Reddit'

print(it_companies)
it_companies.append('Facebook')
print(it_companies)

it_companies.insert(3, 'Meta')
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
back_end = ['Node', 'Express', 'MongoDB']

full_stack = front_end + back_end

full_stack.append('Python')
full_stack.append('SQL')
print(full_stack)

# Excercise 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and fine the min and max age
ages.sort()
print(ages)

# Add the min age and the max age again to the list
ages.insert(0, 19)
ages.insert(-1, 26)

print(ages)

# Find the median age (one middle item or two middle items divided by two)

lengthOfAge = len(ages)
#[19, 19, 19, 20, 22., 24, 24, 24., 25, 25, 26, 26]
print(lengthOfAge)

median = ages[6] + ages[7]

print(median / 2)

# Find the average age (sum of all items divided by their number )
sumOfAge = sum(ages)

print(sumOfAge)

# Find the range of the ages (max minus min)

rangeOfAge = ages[-1] - ages[0]
print(rangeOfAge)

# Compare the value of (min - average) and (max - average), use abs() method

avgOfAge = sumOfAge / lengthOfAge + 1

minAvgAge = ages[0] - avgOfAge
maxAvgage = ages[-1] - avgOfAge

print(minAvgAge)
print(maxAvgage)

# Divide the countries list into two equal lists if it is even
# if not one more country for the first half.

countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombi',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]

lengthOfCountries = len(countries)+1


if lengthOfCountries % 2 == 0:
    print("True")
else:
    print("False")

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'].
# Unpack the first three countries and the rest as scandic countries.
copyOfCountry = ['China', 'Russia', 'USA',
                 'Finland', 'Sweden', 'Norway', 'Denmark']
unpackFirstThree = slice(0, 3)
print(copyOfCountry[unpackFirstThree])
lengthOfCopy = len(copyOfCountry())
scandicCountries = slice(4, lengthOfCopy)
print(scandicCountries)
