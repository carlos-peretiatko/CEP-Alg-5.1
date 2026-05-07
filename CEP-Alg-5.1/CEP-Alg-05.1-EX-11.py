def conta_digitos(n, d):
    contador = 0
    for digito in str(n):
        if int(digito) == d:
            contador += 1
    return contador

def eh_permutacao(a, b):
    for d in range(1, 10):
        if conta_digitos(a, d) != conta_digitos(b, d):
            return False
    return True

print(eh_permutacao(5412434, 4321445))