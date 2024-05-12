waiting_list = ["sen", "ben", "john"]

# lists are mutable, the methods will mutate the list.
# So the method itself doesn't return anything.
waiting_list.sort()

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)