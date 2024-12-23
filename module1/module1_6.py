my_dict = { "Alex" : 1985, "Max" : 1987, "Nikita" : 2000, "Sasha" : 1995}
print(my_dict)
print(my_dict["Alex"])
print(my_dict.get("kamila", "None"))
my_dict.update({"Serg" : 1997,
                "Oleg" : 1982})
print(my_dict)
my_dict.pop("Alex")
print(my_dict)
# 3 task
my_set = {1, 2, 3, 4, 4, 8, 8, 8, 66, "Kolan", "Ivan", "Kolan", True}
print(my_set)
my_set.add(7)
my_set.add(33)
print(my_set)
my_set.discard(1)
print(my_set)
