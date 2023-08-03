my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
}

print(my_dict["name"])
print(my_dict.get("age"))

my_dict["occupation"] = "Engineer"
print(my_dict)

my_dict.pop("age")
print(my_dict)

print("city" in my_dict)
print("country" in my_dict)

keys = my_dict.keys()
values = my_dict.values()
print(keys)
print(values)

for key in my_dict:
    print(key, ":", my_dict[key])

my_dict.clear()
print(my_dict)
