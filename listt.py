my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)

my_list.extend([7, 8, 9])
print(my_list)

my_list.insert(0, 0)
print(my_list)

my_list.remove(3)
print(my_list)

popped_item = my_list.pop()
print(popped_item)
print(my_list)

my_list.clear()
print(my_list)

fruits = ['apple', 'banana', 'orange', 'apple']
print(fruits.index('banana'))
print(fruits.count('apple'))

numbers = [5, 2, 8, 1, 3]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

original_list = [1, 2, 3]
copied_list = original_list.copy()
print(copied_list)

print(len(original_list))
