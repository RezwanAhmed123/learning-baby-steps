import random
from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


victories = {
    Action.Scissors: [Action.Paper],
    Action.Paper: [Action.Rock],
    Action.Rock: [Action.Scissors]
}


def get_system_action():
    action = Action(random.randint(0, 2))
    return action


def get_human_action():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action


def determine_winner(human_action, computer_action):
    defeats = victories[computer_action]
    if human_action == computer_action:
        print(f"You picked: {human_action.name} while computer picked: {computer_action.name} . Its a tie!")
    elif computer_action in defeats:
        print(f"You picked: {human_action.name} while computer picked: {computer_action.name} . You win!")
    else:
        print(f"You picked: {human_action.name} while computer picked: {computer_action.name} . You lose!")


try_again = "y"
while try_again == "y":
    try:
        system = get_system_action()
        human = get_human_action()
        determine_winner(human, system)
    except ValueError:
        print(f"Invalid selection! Pick an integer between 0 and {len(Action)-1}")
        continue

    try_again = input("Do you want to try again? (y/n): ").lower()
    if try_again != "y":
        break
