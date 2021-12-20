number_for_inspection = int(input("Please type in a number: "))
list_of_divisors = []
for divisor in range(1, number_for_inspection):
    modulo_of_number = number_for_inspection % divisor
    if modulo_of_number == 0:
        list_of_divisors += [divisor]

print(f"the list of divisors for this number are {list_of_divisors}")