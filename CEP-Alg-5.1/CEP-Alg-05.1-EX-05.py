def potencia(x, y):
    resultado = 1
    for i in range(int(y)):
        resultado *= x
    return resultado

print(potencia(5, 2))