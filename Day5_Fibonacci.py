def fibonacci(n):
    fibo = [1, 1]

    if n <= 1:
        return fibo[:n+1]

    while len(fibo) <= n:
        next_num = fibo[-1] + fibo[-2]
        fibo.append(next_num)

    return fibo
print("Nhập số phần tử trong dãy Fibonacci: ")
n = int(input())
fibo = fibonacci(n)
print("Dãy Fibonacci là:")
print(fibo)