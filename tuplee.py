# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# 1. count() method
count_of_3 = my_tuple.count(3)
print(count_of_3)

# 2. index() method
index_of_4 = my_tuple.index(4)
print(index_of_4)

# 3. len() method
length_of_tuple = len(my_tuple)
print(length_of_tuple)

# 4. slicing
slice_of_tuple = my_tuple[1:4]
print(slice_of_tuple)

# 5. concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)

# # 6. unpacking
# a, b, c = my_tuple
# print(a, b, c)

# 7. nested tuple
nested_tuple = (1, (2, 3), 4)
print(nested_tuple)

# 8. in operator
is_present = 4 in my_tuple
print(is_present)

# 9. max() method
max_value = max(my_tuple)
print(max_value)

# 10. min() method
min_value = min(my_tuple)
print(min_value)
