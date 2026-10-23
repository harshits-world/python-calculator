def calculate(a, operator, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a + b
    elif operator == "/":
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError("Invalid operator")


if __name__ == "__main__":
    print("Python Calculator")
    a = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    try:
        print("Result:", calculate(a, operator, b))
    except ValueError as error:
        print("Error:", error)
