from random import randint

def eh_primo(num):
    if num < 2: # Não existe número primo menor que 2
        return False  

    for i in range(2, num // 2 + 1): # Verifica se o num é divisível por algum outro número
        if num % i == 0:
            return False
    return True # Se não for, ele é primo

def multiply():
    lista_aleatoria = [randint(0, 10) for _ in range(10)]
    resultado_multiplicacao = 1
    
    for num in lista_aleatoria:
        if eh_primo(num):
            resultado_multiplicacao *= num
    
    return resultado_multiplicacao

