# Substituição em Vetor I

numbers = []
for i in range(10):
    user_number = int(input())
    if user_number <= 0:
        user_number = 0
    numbers.append(user_number)

for index, number in enumerate(numbers):
    print(f'X[{index}] = {number}')
