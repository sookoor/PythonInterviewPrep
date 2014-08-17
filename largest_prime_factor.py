def get_largest_prime_factor(n):
    d = 2
    factors = []
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d;
        d += 1
        if d * d > n:
            if n > 1:
                factors.append(n)
                break

    return max(factors)

if __name__ == "__main__":
    assert get_largest_prime_factor(13195) == 29
    print get_largest_prime_factor(600851475143)
