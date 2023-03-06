def verifica_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b == num:
        return True
    else:
        return False

num = int(input("Informe um número: "))
fibonacci = [0, 1]

while fibonacci[-1] < num:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

if num in fibonacci:
    print(f"O número {num} pertence à sequência de Fibonacci!")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci!")
