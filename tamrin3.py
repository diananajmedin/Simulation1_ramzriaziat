import math


def is_perfect_square(num):

    last_two_digits = ["00", "01", "04", "09", "16", "21", "24", "25",
                       "29", "36", "41", "44", "49", "56", "61", "64",
                       "69", "76", "81", "84", "89", "96"]


    if str(num)[-2:] in last_two_digits:
        root = math.sqrt(num)
        integer_part = int(root)


        if root - integer_part == 0:
            return True
        else:
            return False
    else:
        return False


number = int(input("enter your number: "))


root = math.sqrt(number)
print(F"{int(root) - 1} < {root} < {int(root) + 1}")


current_value = int(root) + 1
found = False
attempts = 0


while not found:
    difference = pow(current_value, 2) - number
    found = is_perfect_square(difference)

    if not found:
        current_value += 1

    attempts += 1


print(F"{number} = ({current_value})² - ({int(math.sqrt(difference))})² = {pow(current_value, 2)} - {difference}")
print("attempts: ", attempts)