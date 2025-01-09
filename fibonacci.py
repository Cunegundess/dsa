# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

d: dict[int] = {}

def fibonacci(n: int) -> int:
    if n == 1 or n == 2:
        return 1

    if n == 3:
        return 2

    if n > 3:
        if n - 1 not in d:
            d[n - 1] = fibonacci(n - 1)

        if n - 2 not in d:
            d[n - 2] = fibonacci(n - 2)

        return d[n - 1] + d[n - 2]



print(fibonacci(10))