my_set = {1, 2, 3, 4, 5}

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)

my_set.discard(4)
print(my_set)

removed_element = my_set.pop()
print(removed_element)
print(my_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)

intersection_set = set1.intersection(set2)
print(intersection_set)

difference_set = set1.difference(set2)
print(difference_set)

symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)

subset_check = set1.issubset(union_set)
print(subset_check)

superset_check = union_set.issuperset(set1)
print(superset_check)
