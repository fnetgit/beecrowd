# Média 3

num = input().split()
n1 = float(num[0])
n2 = float(num[1])
n3 = float(num[2])
n4 = float(num[3])

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
print(f'Media: {media:.1f}')
if media >= 7.0:
    print('Aluno aprovado.')
    exit()

elif media < 5.0:
    print('Aluno reprovado.')
    exit()

else:  
    print('Aluno em exame.')
    exame = float(input(''))
    final = (exame + media) / 2
    print(f'Nota do exame: {exame:.1f}')
if final >=5.0:
    print('Aluno aprovado.')
else:
    print('Aluno reprovado.')
print(f'Media final: {final:.1f}')
