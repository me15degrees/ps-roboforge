from random import randint

def eh_primo(num):
    if num < 2:
        return False  

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def random_10():
    return [randint(0, 10) for _ in range(10)]

def multiply():
    lista_aleatoria = random_10()
    resultado_multiplicacao = 1
    for num in lista_aleatoria:
        if eh_primo(num):
            resultado_multiplicacao *= num
    return resultado_multiplicacao

def main():
    resultado = multiply()
    print(resultado)

if __name__ == "__main__":
    main()
