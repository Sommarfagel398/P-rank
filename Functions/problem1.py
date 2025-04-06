def checker(password):
    length = len(input_password)
    if length < 8:
        return "Password must contain up to 8", length

    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case = upper_case.lower()
    special = "!@#$%^&*"
    digits = "1234567890"

    has_upper = False
    has_lower = False
    has_special = False
    has_digit = False

    for char in password:
        if char in upper_case:
            has_upper = True
        elif char in lower_case:
            has_lower = True
        elif char in special:
            has_special = True
        elif char in digits:
            has_digit = True

    if not (has_upper and has_lower and has_special and has_digit):
        return "Password is weak"

    return "Password is strong"


input_password = input("Enter a password: ")
print(checker(input_password))







