def power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 1:
        p = power(a, abs(b) // 2)
        prod = p * p * a
        if b > 0:
            return prod
        else:
            return 1 / prod
    else:
        p = power(a, abs(b) // 2)
        prod = p * p
        if b > 0:
            return prod
        else:
            return 1 / prod

if __name__ == "__main__":
    print(power(2, 10))
    print(power(2, 11))
    print(power(2, 0))
    print(pow(2, -2))
