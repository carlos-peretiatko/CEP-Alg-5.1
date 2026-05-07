import random

def sorteia_dado():
    return random.randint(1, 6)

contagem = [0, 0, 0, 0, 0, 0]

for i in range(1000000):
    resultado = sorteia_dado()
    contagem[resultado - 1] += 1

for i in range(6):
    print(f"Número {i+1}: {contagem[i]} vezes")