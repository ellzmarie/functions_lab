# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

# sum_to(6)  # returns 21
# sum_to(10) # returns 55

def sum_to(n):
    return sum(range(1, n+1))

print(sum_to(6))
print(sum_to(10))

print('---------')

# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

# largest([1, 2, 3, 4, 0])  # returns 4
# largest([10, 4, 2, 231, 91, 54])  # returns 231

def largest_number(number):

    large_number = 0

    for nums in number:
        if nums >= max(number):
            large_number = nums
    return large_number

print(largest_number([1, 2, 3, 4, 0]))
print(largest_number([10, 4, 2, 231, 91, 54]))

print('---------')

# 3. Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

# occurances('fleep floop', 'e')   # returns 2
# occurances('fleep floop', 'p')   # returns 2
# occurances('fleep floop', 'ee')  # returns 1
# occurances('fleep floop', 'fe')  # returns 0


def occurances(str1, str2):
  return str1.count(str2)

print(occurances('fleep floop', 'e'))
print(occurances('fleep floop', 'ee'))
print(occurances('fleep floop', 'fe'))

print('---------')

# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
# (HINT: Review your notes on *args).

# For example:
# product(-1, 4) # returns -4
# product(2, 5, 5) # returns 50
# product(4, 0.5, 5) # returns 10.0

def product(*args):
  result = 1
  for arg in args:
      result *= arg
  return result

print(product(-1, 4)) # returns -4
print(product(2, 5, 5)) # returns 50
print(product(4, 0.5, 5)) # returns 10.0