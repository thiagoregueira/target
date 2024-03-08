def is_fibonacci(number):
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    if b == number:
        return True
    else:
        return False

number = int(input("Informe o número: "))


if is_fibonacci(number):
    print(f"{number} pertence à sequência de Fibonacci.")
else:
    print(f"{number} não pertence à sequência de Fibonacci.")