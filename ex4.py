def somar (numero1, numero2):
    print(numero1 + numero2)

def subtrair(n1, n2):
    return n1 - n2

def imprime_parametros(**kwargs):
    for key, value in kwargs.items():
        print("%s = %s" %(key, value))
