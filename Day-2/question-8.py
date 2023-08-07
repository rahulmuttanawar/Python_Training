from functools import reduce

def sum_reduce(numbers):
    return reduce(lambda x, y: x + y, numbers)

numbers = [1, 2, 3, 4, 5]
total_sum = sum_reduce(numbers)
print("Sum of the list:", total_sum)
