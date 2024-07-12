def print_mat(A: list[list]):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f"matrice[{i}][{j}]: {A[i][j]}")

def addition_matrice(A: list[list], B: list[list]) -> list[list]:
    
    return [[ A[i][j] + B[i][j] 
            for j in range(len(A[i]))
            ]for i in range(len(A))]

def substraction_matrice(A: list[list], B: list[list]) -> list[list]:
    
    return [[ A[i][j] - B[i][j] 
            for j in range(len(A[i]))
            ]for i in range(len(A))]

def multiplication_matrice_range(A: list[list], B: list|list) -> list[list]:

    matrice = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                matrice[i][j] += A[i][k] * B[k][j]
    return matrice

def multiplication_matrice_zip(A: list[list], B: list[list]) -> list[list]:

    B_t = list(zip(*B))

    return [[sum(a * b for a, b in zip(A[i], B_t[j])) for j in range(len(B_t))]for i in range(len(A))]

def multiplication_generique(A: list[list], B: list[list]) -> list[list]:
    if len(A) == 1 and len(A[0]) == 1:
        return [[A[0][0] * B[0][0]]]
    
    A11, A12, A21, A22 = diviser_matrice(A)
    B11, B12, B21, B22 = diviser_matrice(B)
    
    C11 = addition_matrice(
        multiplication_generique(A11, B11),
        multiplication_generique(A12, B21)
    )
    C12 = addition_matrice(
        multiplication_generique(A11, B12),
        multiplication_generique(A12, B22)
    )
    C21 = addition_matrice(
        multiplication_generique(A21, B11),
        multiplication_generique(A22, B21)
    )
    C22 = addition_matrice(
        multiplication_generique(A21, B12),
        multiplication_generique(A22, B22)
    )
    
    return combiner_matrice(C11, C12, C21, C22)

def diviser_matrice(A: list[list]) -> tuple[list]:
    mid_r = len(A) // 2
    mid_c = len(A[0]) // 2

    A11 = [row[:mid_c] for row in A[:mid_r]]
    A12 = [row[mid_c:] for row in A[:mid_r]]
    A21 = [row[:mid_c] for row in A[mid_r:]]
    A22 = [row[mid_c:] for row in A[mid_r:]]

    return A11, A12, A21, A22

def combiner_matrice(C11: list[list], C12: list[list], C21: list[list], C22: list[list]) -> : list[list]:

    return [C11[i] + C12[i] for i in range(len(C11))] + [C21[i] + C22[i] for i in range(len(C21))]

def strassens_algorithm(A: list[list], B: list|list) -> list[list]:
    if len(A) == 1 and len(A[0]) == 1:
        return [[A[0][0] * B[0][0]]]    
    
    A11, A12, A21, A22 = diviser_matrice(A)
    B11, B12, B21, B22 = diviser_matrice(B)

    P1 = strassens_algorithm(A11, substraction_matrice(B12,B22))
    P2 = strassens_algorithm(addition_matrice(A11,A12), B22)
    P3 = strassens_algorithm(addition_matrice(A21, A22), B11)
    P4 = strassens_algorithm(A22, substraction_matrice(B21,B11))
    P5 = strassens_algorithm(addition_matrice(A11, A22), addition_matrice(B11, B22))
    P6 = strassens_algorithm(substraction_matrice(A12, A22), addition_matrice(B21, B22))
    P7 = strassens_algorithm(substraction_matrice(A11, A21), addition_matrice(B11, B12))

    C11 = addition_matrice(substraction_matrice(addition_matrice(P5, P4), P2), P6)
    C12 = addition_matrice(P1, P2)
    C21 = addition_matrice(P3, P4)
    C22 = substraction_matrice(substraction_matrice(addition_matrice(P5, P1), P3), P7)

    return combiner_matrice(C11, C12, C21, C22)

def main():
    A = [[1,2], [3,4]]
    B = [[5,6], [7,8]]

    print(multiplication_generique(A, B))

if __name__ == '__main__':
    main()