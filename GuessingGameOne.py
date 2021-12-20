from random import randint

computer_number = randint(1, 9)
play_again = 3

while play_again > 0:
    try:
        user_number = int(input("Please input number between 1 and 9: "))
        if user_number == computer_number:
            print(f"{user_number} was the correct number you win!")
            break
        elif user_number > computer_number:
            print(f"{user_number} is too high, try lower!")
            play_again -= 1
            print(f"Number of tries remaining: {play_again}")
            continue
        elif user_number < computer_number:
            print(f"{user_number} is too low, try higher!")
            play_again -= 1
            print(f"Number of tries remaining: {play_again}")
            continue
    except ValueError:
        print("Invalid value! Please input an integer!")
        continue
