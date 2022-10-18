"""
Program to practice automatic boring stuff FUNCTIONS chapter.
"""


def get_user_input():
    """Get the user input as an int."""
    while True:
        try:
            final = int(input("What is your number: "))
            break
        except ValueError:
            print("Please enter an integar!\n")
            continue
    return final


def return_to_1(count, final):
    """Keep running loop until the number is 1."""
    while final != 1:
        if final % 2 == 0:
            final = final // 2

        else:
            final = 3 * final + 1

        count += 1
    return count


def print_answer(count):
    """Print final answer based on whether the answer is singular or plural."""
    if count == 1:
        print(f"\nIt took {count} iteration to return 1.")

    else:
        print(f"\nIt took {count} iterations to return 1.")


count = 0
final = get_user_input()
print_answer(return_to_1(count, final))
