# O maior

numbers = input().split()
first_number = int(numbers[0])
second_number = int(numbers[1])
third_number = int(numbers[2])

maior = first_number

if second_number > maior:
    maior = second_number
if third_number > maior:
    maior = third_number
print(f'{maior} eh o maior')
