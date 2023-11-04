def is_perfect_number(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors) == num

perfect_numbers = []
for num in range(2, 10001):
    if is_perfect_number(num):
        perfect_numbers.append(num)

print("Các số hoàn hảo trong phạm vi 10,000 là:")
print(perfect_numbers)