# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    odd_numbers = []
    for item in some_list:
        if item % 2 != 0:
            odd_numbers.append(item)
    return odd_numbers

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    even_numbers = []
    for item in some_list:
        if item % 2 == 0:
            even_numbers.append(item)
    return even_numbers

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    long_strings = []

    for word in word_list:
        if len(word) >= 4:
            long_strings.append(word)

    return long_strings

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):

    smallest = some_list[0]

    for i in range(1,len(some_list)):
        if smallest > some_list[i]:
            smallest = some_list[i]

    return smallest

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    largest = some_list[0]

    for i in range(1,len(some_list)):
        if largest < some_list[i]:
            largest = some_list[i]

    return largest

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):

    halves = []

    for item in some_list:
        halves.append( item/2.0 )

    return halves

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    lengths = []

    for item in word_list:
        lengths.append(len(item))

    return lengths

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    the_sum = 0

    for item in numbers:
        the_sum += item

    return the_sum

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    multiply = 1

    for item in numbers:
        multiply *= item

    print multiply

    return multiply

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    joined = ""

    for item in string_list:
        joined += item

    return joined

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    the_sum = 0

    for item in numbers:
        the_sum += item

    the_avg = the_sum / float(len(numbers))

    return the_avg
