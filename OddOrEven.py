def number_inspector(input_number, divisor):
    modulo = input_number % divisor
    if modulo == 0:
        print(f"The number {input_number} is a multiple of {divisor}.")
    else:
        print(f"The number {input_number} is not a multiple of {divisor}.")


numbers_to_check = int(input("How many numbers do you want to check? "))
client_divisor = int(input("Please input the divider: "))

list_of_numbers_checked = []

for item in range(numbers_to_check):
    client_input = int(input("Please input a number to be divided: "))
    number_inspector(client_input, client_divisor)
    list_of_numbers_checked += [client_input]
print(f"You have checked {numbers_to_check} numbers for divisibility by {client_divisor}."
      f"The numbers are {list_of_numbers_checked}.")