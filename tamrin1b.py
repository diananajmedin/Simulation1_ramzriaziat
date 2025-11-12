import math
import random
from matplotlib import pyplot as plt


def gcd_extended(m, n):
    u = [1, 0]
    v = [0, 1]
    quotients = []

    step = -1
    orig_m, orig_n = m, n
    current_gcd = None
    final_u = final_v = None

    while m != 0:
        step += 1

        if n == 0:
            remainder = 0
            quotients.append("-")
        else:
            remainder = m % n
            quotients.append(m // n)

        if step > 1:
            u.append(u[step - 2] - u[step - 1] * quotients[step - 2])
            v.append(v[step - 2] - v[step - 1] * quotients[step - 2])

        current_gcd = m
        m, n = n, remainder

        if m == 0:
            final_u = u[step]
            final_v = v[step]

    return current_gcd, final_u, final_v, step + 1


num_pairs = 100

list_a = []
list_b = []

for i in range(100):
    random_num_a = random.randint(100000, 10000000)
    list_a.append(random_num_a)
    random_num_b = random.randint(100000, 10000000)
    list_b.append(random_num_b)

list_a.sort()
list_b.sort()

turns = []
max_turns = []
for i in range(len(list_a)):
    x = list_a[i]
    y = list_b[i]

    gcd_val, u_val, v_val, steps = gcd_extended(x, y)
    turns.append(steps)

    max_val = 2 * math.log2(max(x, y)) + 1
    max_turns.append(max_val)

    print("Pair", i, ":", (x, y))
    print("GCD =", gcd_val, "=", x, "*(", u_val, ") +", y, "*(", v_val, ")")
    print("Steps taken =", steps, ", Max allowed ~", round(max_val, 2))
    print("---------------------------------------------")

x_axis = []

for i in range(len(list_a)):
    x_axis.append(min(list_a[i], list_b[i]))

plt.scatter(x_axis, turns, color="red", label="Actual Steps")
plt.plot(x_axis, max_turns, color="green", label="2log2(b)+1")
plt.xlabel("Max(a, b)")
plt.ylabel("Number of Steps")
plt.title("Euclidean Algorithm Steps vs Max Theoretical Steps")
plt.legend()
plt.show()
