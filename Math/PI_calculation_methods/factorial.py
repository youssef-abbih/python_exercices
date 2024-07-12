def factorial(n: int, cte: int = 1) -> int:
    k: int = n * cte
    fact: int = 1
    if k <= 1:
        return 1
    while k != 0:
        fact *= k
        k -= 1
    return fact
