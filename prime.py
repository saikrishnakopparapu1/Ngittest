def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print("Prime numbers up to 50:")
for num in range(2, 51):
    if is_prime(num):
        print(num, end=" ")


def get_odds(lst):
    """Return a list of odd integers from `lst` preserving order."""
    return [x for x in lst if isinstance(x, int) and x % 2 != 0]


# Demo: show odd numbers from a sample list
if __name__ == "__main__":
    sample = list(range(1, 21))
    print("\nOdd numbers in sample:", get_odds(sample))


def get_prime_palindromes(lst):
    """Return a list of integers from `lst` that are both prime and palindromic.

    Rules:
    - Only integers > 0 are considered.
    - Preserves the original order.
    """
    result = []
    for x in lst:
        if not isinstance(x, int):
            continue
        if x <= 0:
            continue
        if is_prime(x) and str(x) == str(x)[::-1]:
            result.append(x)
    return result


# Demo: show prime palindromes from a sample range
if __name__ == "__main__":
    sample2 = list(range(1, 200))
    print("Prime palindromes in 1..199:", get_prime_palindromes(sample2))

