from random import randint

def eh_primo(num):
    if num < 2:
        return False  

    primo = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            primo = False
            break
    return primo

def random_10():
    l = []
    for _ in range(10):
        l.append(randint(0,10))
    return l 

def multiply():
    lista_aleatoria = random_10()
    multiply = 1
    for num in range(len(lista_aleatoria)):
        if eh_primo(num):
            multiply *= num
    return multiply

def main():
   result = multiply()
   print(result)
main()