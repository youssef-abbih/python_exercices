from math import sqrt
from factorial import factorial

def leibniz_formula(n: int) -> float:
    pi: float = 0
    for i in range(n):
        pi += 4/( (-1) ** i * (2 * i + 1))
    return pi

def wallis_product(n: int) -> float:
    pi: float = 1.0
    for i in range(1, n):
        pi *= (4 * i ** 2)/((4 * i ** 2) -1)
    return 2 * pi

def ramanujan_formula(n: int) -> float:
    pi: float = 0
    __CONST: float = 2 * sqrt(2) / 9801
    
    for i in range(n):
        pi += factorial(i, 4) * (1103 + 26390 * i) / ((factorial(i) ** 4) * 396 ** (4 * i))
    return 1 / (pi * __CONST)

def madhava_formula(n: int) -> float:
    pi: float = 0
    __CONST = sqrt(12)
    
    for i in range(n):
        pi += (3 ** -i) / (2 * i + 1)
    
    return __CONST * pi

def main() -> None:
    pi1 = leibniz_formula(1000000)
    pi2 = wallis_product(1000000)
    pi3 = ramanujan_formula(1000)
    pi4 = madhava_formula(100000)

    print(pi1)
    print(pi2)
    print(pi3)
    print(pi4)


if __name__ == '__main__':
    main()
