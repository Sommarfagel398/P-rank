def multiply_matrices(A, B):
    if len(A[0]) != len(B):
        return None

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)
    return result

rows_A, cols_A = map(int, input("Enter rows and columns of matrix A: ").split())
A = [list(map(int, input(f"Row {i+1} of A: ").split())) for i in range(rows_A)]

rows_B, cols_B = map(int, input("Enter rows and columns of matrix B: ").split())
B = [list(map(int, input(f"Row {i+1} of B: ").split())) for i in range(rows_B)]

result = multiply_matrices(A, B)
if result is None:
    print("Incompatible Matrix")
else:
    print("Resultant Matrix:")
    for row in result:
        print(row)
