# Sort Simples

n1, n2, n3 = map(int, input().split())

list = [n1, n2, n3]
ascending_order = sorted(list)
for numbers in ascending_order:
     print(numbers)
print(f'\n{n1}\n{n2}\n{n3}')
