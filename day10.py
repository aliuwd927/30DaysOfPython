# Iterate 0 to 10 using for loop, do the same using while loop.
# count = 0
# while count < 10:
#     print(count)
#     count = count + 1

# Iterate 10 to 0 using for loop, do the same using while loop.
# new_count = 10
# while new_count > 0:
#     print(count)
#     count = count - 1
#     if(count == 0):
#         break


# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
# triangle = 0
# while triangle < 10:
#     print("#" * triangle)
#     triangle = triangle + 1


# Use nested loops to create the following:

# Initialize the variable `rows` to 0, representing the current row count
rows = 0
# Initialize the variable `column` to None, which will later hold a string of "#" characters
column = None
# Start a loop that iterates 9 times (from 0 to 8, inclusive)
for i in range(9):
    # Check if `rows` equals 8 (final row)
    if(rows == 8):
        # If so, assign `column` a string of "#" repeated `rows` times
        column = "#" * rows
    else:
        # Otherwise, increment `rows` by 1
        rows = rows + 1
    # Start another loop that iterates 9 times (nested loop)
    for j in range(9):
        # Check if `column` is not None (i.e., if the final row condition was met)
        if(column != None):
            # If true, print the value of `column` (a string of "#" characters)
            print(column)
        else:
            # If `column` is None, skip the current iteration and do nothing
            continue

# Print the following pattern:
num_times_itself = 0

for i in range(11):
    print(num_times_itself * num_times_itself)
    num_times_itself = num_times_itself + 1

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

# Use for loop to iterate from 0 to 100 and print only even numbers

# Use for loop to iterate from 0 to 100 and print only odd numbers
    
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
    