def fibonacci(n):
    fib = [0 for x in range(n + 2)]
    for i in range(0, n + 2):
        if i == 0:
            fib[i] = 0
        elif i == 1:
            fib[i] = 1
        else:
            fib[i] = fib[i - 1] + fib[i - 2]

        if fib[i] == n:
            return f'O número {n} está em Fibonacci{fib}'
        elif fib[i] > n:
            return f'O número {n} não está em {fib}'


input = int(input("Informe um número: "))
result = fibonacci(input)

print(result)
