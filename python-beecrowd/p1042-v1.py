# Sort Simples

n1, n2, n3 = map(int, input().split())

list = [n1, n2, n3]
cres = sorted(list)
for numbers in cres:
     print(numbers)
print(f'\n{n1}\n{n2}\n{n3}')
