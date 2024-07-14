from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    is_calculating = True

    num1 = float(input("What's the first number?: "))

    while is_calculating:
        operation_symbol = input(f"Pick an operation from: {', '.join(operations.keys())} ")
        num2 = float(input("What's the next number?: "))

        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        num1 = answer

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ").lower() == 'n':
            is_calculating = False
            calculator()


calculator()
