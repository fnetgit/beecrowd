# Tomadas

t1, t2, t3, t4 = map(int, input().split()) # tomadas em cada régua
total_sockets = (t1 + t2 + t3 + t4) - 3 # somar todas as tomadas e subtrair (sempre vai diminuir 3)
print(total_sockets)
