#!/usr/bin/env python3
# Time to get some practice! Write your code in the list_comprehension.py file in the lib folder. Run pytest -x to check your work. Your goal is to practice creating lists using list comprehensions.

# Using a list comprehension, write a function return_evens() that returns a list of all of the even elements of a sequence of integers.

# return_evens([0, 1, 3, 5, 7, 8, 9])
# # [0, 8]
# Using a list comprehension, write a function make_exclamation() that takes a list of sentence strings and returns a list of sentence strings with exclamation marks at the end.

# make_exclamation(["Hello", "I'm doing great", "Python is fun"])
# # ["Hello!", "I'm doing great!", "Python is fun!"]
# When all of your tests are passing, submit your work using git.

def return_evens(num_list):
    even_integers = [n for n in num_list if n % 2 == 0]
    return even_integers

def make_exclamation(sentence_list):
    exclamation_strings = [string + '!' for string in sentence_list ]
    return exclamation_strings