def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = []
for num in range(2, 101):
    if is_prime(num):
        prime_numbers.append(num)

print("Các số nguyên tố trong phạm vi từ 1 đến 100 là:")
print(prime_numbers)