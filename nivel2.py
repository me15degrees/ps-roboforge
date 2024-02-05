import math

def distancia_entre_pontos(p1, p2): # Fórmula derivada de pitágoras para calcular distância entre pontos
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def lados(ponto_A, ponto_B, ponto_C): # Os lados são calculados pela distância de 3 pontos, tomados 2 a 2
    lado_a = distancia_entre_pontos(ponto_B, ponto_C)
    lado_b = distancia_entre_pontos(ponto_A, ponto_C) 
    lado_c = distancia_entre_pontos(ponto_A, ponto_B)
    return lado_a, lado_b, lado_c

def angulos(a, b, c): # A fórmula da lei dos cossenos permite chegar em um valor de ângulo
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
    angulo_C_graus = math.degrees(math.acos(cos_C))
    
    cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
    angulo_B_graus = math.degrees(math.acos(cos_B))

    angulo_A_graus = 180 - angulo_B_graus - angulo_C_graus

    return angulo_A_graus, angulo_B_graus, angulo_C_graus

def perimetro(lado_a, lado_b, lado_c): # Soma o valor dos lados
    return lado_a + lado_b + lado_c

def calcular_area_por_determinante(x1, y1, x2, y2, x3, y3): # Passa as coordenadas e calcula 1/2 * |det|
    determinante = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    area = 0.5 * abs(determinante)
    return area

def verifica_triangulo(a,b,c): # Função que verifica se os lados satisfazem a desigualdade triangular
    if abs(b-c) < a and a < b + c:
        return True
    return False

def tipo_lado(a, b, c):
    if verifica_triangulo(a,b,c): # Verifica em qual categoria de triângulo se encaixa
        if a == b and b == c:
            return "equilátero"
        elif a == b or b == c or a == c:
            return "isóceles"
        else:
            return "escaleno"
    else:
        return "não é um triângulo"

def tipo_angulo(a, b, c): # Verifica em qual categoria de triângulo se encaixa
    lados_ordenados = sorted([a, b, c])
    a, b, c = lados_ordenados
    if verifica_triangulo(a,b,c):
        if a**2 + b**2 == c**2:
            return "retângulo"
        elif a**2 + b**2 < c**2:
            return "obtuso"
        else:
            return "agudo"

def main():
    # Aqui altera as coordenadas dos pontos 
    ponto_A = (0,0)
    ponto_B = (6,0)
    ponto_C = (3, (3**0.5)*6/2)

    a, b, c = lados(ponto_A, ponto_B, ponto_C)
    print(f"\nO lado A mede {a:.2f}, o lado B mede {b:.2f} e o lado C mede {c:.2f};")

    angulo_A, angulo_B, angulo_C = angulos(a, b, c)
    print(f"Os ângulos do triângulo são {angulo_A:.2f} graus, {angulo_B:.2f} graus e {angulo_C:.2f} graus;")

    perimetro_triangulo = perimetro(a, b, c)
    print(f"O perímetro do triângulo é {perimetro_triangulo:.2f};")

    area_triangulo = calcular_area_por_determinante(ponto_A[0], ponto_A[1], ponto_B[0], ponto_B[1], ponto_C[0], ponto_C[1])
    print(f"A área mede {area_triangulo:.2f};")

    tipo_triangulo = tipo_lado(a, b, c)
    tipo_triangulo2 = tipo_angulo(a, b, c)
    print(f"O triângulo é do tipo {tipo_triangulo} e {tipo_triangulo2}.")

if __name__ == "__main__":
    main()
