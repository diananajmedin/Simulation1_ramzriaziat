
def gcd_extended(m, n):
    u = [1, 0]
    v = [0, 1]
    quotients = []

    print("Step\tm\t\tn\t\tR\t\tu\t\tv")
    print("--------------------------------------------")

    step = -1
    orig_m, orig_n = m, n
    current_gcd = None

    while m != 0:
        step += 1

        if n == 0:
            remainder = 0
            quotients.append("-")
        else:
            remainder = m % n
            quotients.append(m // n)

        if step > 1:
            u.append(u[step-2] - u[step-1]*quotients[step-2])
            v.append(v[step-2] - v[step-1]*quotients[step-2])

        print(f"{step}\t\t{m}\t\t{n}\t\t{remainder}\t\t{u[step]}\t\t{v[step]}")

        current_gcd = m
        m, n = n, remainder

        if m == 0:
            print("-----------------------------------------------")
            print(f"GCD = {current_gcd}")
            print(f"GCD = {u[step]}*{orig_m} + {v[step]}*{orig_n} = {current_gcd}")
            final_u = u[step]
            final_v = v[step]

    return current_gcd, final_u, final_v



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"\nCalculating GCD for: {num1} and {num2}\n")

gcd_result, u_coeff, v_coeff = gcd_extended(num1, num2)


print(f"\n\nGCD({num1}, {num2}) = {gcd_result}")
print(f"{gcd_result} = {num1}*({u_coeff}) + {num2}*({v_coeff})")

print("End of program")
