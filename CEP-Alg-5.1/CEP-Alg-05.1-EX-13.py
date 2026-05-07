def encaixa(a, b):
    return str(a).endswith(str(b))

def segmento(a, b):
    if len(str(a)) < len(str(b)):
        return str(a) in str(b)
    else:
        return str(b) in str(a)

print(segmento(567890, 678))