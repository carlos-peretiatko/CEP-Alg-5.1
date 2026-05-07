def conta_digitos(n, d):
    contador = 0
    for digito in str(n):
        if int(digito) == d:
            contador += 1
    return contador

print(conta_digitos(122333, 3))