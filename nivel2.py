import math

def distancia_entre_pontos(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def lados(ponto_A, ponto_B, ponto_C):
    lado_a = distancia_entre_pontos(ponto_B, ponto_C)
    lado_b = distancia_entre_pontos(ponto_A, ponto_C)    
    lado_c = distancia_entre_pontos(ponto_A, ponto_B)
    return lado_a, lado_b, lado_c

def angulos(a, b, c):
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
    angulo_C_radianos = math.acos(cos_C)
    angulo_C_graus = math.degrees(angulo_C_radianos)
    
    cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
    angulo_B_radianos = math.acos(cos_B)
    angulo_B_graus = math.degrees(angulo_B_radianos)

    angulo_A_graus = 180 - angulo_B_graus - angulo_C_graus
    return angulo_A_graus, angulo_B_graus, angulo_C_graus

def perimetro(lado_a, lado_b, lado_c):  
    return lado_a + lado_b + lado_c

def calcular_area_por_determinante(x1, y1, x2, y2, x3, y3):
    determinante = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    area = 0.5 * abs(determinante)
    return area

def eh_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a != b and a != c and b != c:
            return "escaleno"
        elif a == b and b == c:
            return "equilátero"
        else:
            return "isósceles"
    else:
        return "não é um triângulo"

def eh_triangulo2(a, b, c):
    lados_ordenados = sorted([a, b, c])
    a, b, c = lados_ordenados

    if a**2 + b**2 == c**2:
        return "retângulo"
    elif a**2 + b**2 < c**2:
        return "obtuso"
    else:
        return "agudo"

def main():
    ponto_A = (2, 2)
    ponto_B = (5, 2)
    ponto_C = (3.5, 2 + 3 * (3 ** 0.5))

    a, b, c = lados(ponto_A, ponto_B, ponto_C)
    print(f"O lado A é {a:.2f}, o lado B é {b:.2f} e o lado C é {c:.2f}")

    angulo_A, angulo_B, angulo_C = angulos(a, b, c)
    print(f"Os ângulos do triângulo são {angulo_A:.2f}, {angulo_B:.2f}, {angulo_C:.2f}")

    perimetro_tri = perimetro(a, b, c)
    print(f"O perímetro do triângulo é {perimetro_tri:.2f}")

    area_tri = calcular_area_por_determinante(ponto_A[0], ponto_A[1], ponto_B[0], ponto_B[1], ponto_C[0], ponto_C[1])
    print(f"A área é de {area_tri:.2f}")

    tipo_triangulo = eh_triangulo(a, b, c)
    print(f"Tipo de triângulo: {tipo_triangulo}")

    tipo_triangulo2 = eh_triangulo2(a, b, c)
    print(f"Tipo de triângulo 2: {tipo_triangulo2}")

if __name__ == "__main__":
    main()
