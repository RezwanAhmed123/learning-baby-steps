try_again = 'y'
while try_again == 'y':
    try:
        number_to_be_checked = int(input("Please input a number: "))
        divisors = [number for number in range(2, number_to_be_checked) if number_to_be_checked % number == 0]
        if len(divisors) == 0:
            print(f"The number {number_to_be_checked} is a prime number.")
        else:
            print(f"The number {number_to_be_checked} is not a prime number as it can be divided by {divisors}.")
    except ValueError:
        print("Input must be a valid whole number!")

    try_again = input("Do you want to check another number? (y/n): ").lower()
