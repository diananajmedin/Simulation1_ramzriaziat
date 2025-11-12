import math
import random

counter = 0
max_count = 100

while counter < max_count:
    print("-------------------------------------------------------")
    print(F"{counter + 1}.")

    number = random.randint(100, 500)
    print(F"n is: {number}")

    max_divisor = int(math.isqrt(number)) + 1

    divisibility = []
    divisors_list = []

    for divisor in range(2, max_divisor):
        divisors_list.append(divisor)
        if number % divisor == 0:
            divisibility.append(True)
        else:
            divisibility.append(False)

    tedad_morakab = 0
    morakab = False
    mazarebaval = []

    for flag in divisibility:
        tedad_morakab += flag

    if tedad_morakab == 0:
        print("prime")
    else:
        print("composite")
        morakab = True

    if morakab:
        for idx in range(len(divisibility)):
            if divisibility[idx]:
                mazarebaval.append(divisors_list[idx])

    final_result = []
    for factor in sorted(mazarebaval):
        is_prime_factor = True
        for existing in final_result:
            if factor % existing == 0 and factor != existing:
                is_prime_factor = False
                break
        if is_prime_factor:
            final_result.append(factor)

    print(F"prime factors are: {final_result}")

    counter += 1