def Prime_factorization(number):
    factors = []
    divided = 2

    while number < 1:
        while number % divided == 0:
            factors.append(divided)
            number //= divided
        divided =+ 1
    return factors

input_Num = int(input("Enter a number: "))
result = Prime_factorization(input_Num)
print(f"Prime factors:{result}")