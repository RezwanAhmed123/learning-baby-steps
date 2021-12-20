a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_to_be_printed = []
for number in a:
    if number < 10:
        list_to_be_printed += [number]
print(list_to_be_printed)