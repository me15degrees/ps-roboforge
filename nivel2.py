import math

def distancia_entre_pontos(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def lados(ponto_A, ponto_B, ponto_C):
    lado_a = distancia_entre_pontos(ponto_B, ponto_C)
    lado_b = distancia_entre_pontos(ponto_A, ponto_C)    
    lado_c = distancia_entre_pontos(ponto_A, ponto_B)
    return abs(lado_a), abs(lado_b), abs(lado_c)

def angulos(a, b, c):
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
    angulo_C_radianos = math.acos(cos_C)
    angulo_C_graus = math.degrees(angulo_C_radianos)
    
    cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
    angulo_B_radianos = math.acos(cos_B)
    angulo_B_graus = math.degrees(angulo_B_radianos)

    angulo_A_graus = 180 - angulo_B_graus - angulo_C_graus
    print(f"Os ângulos do triângulo são {angulo_A_graus:.2f}, {angulo_B_graus:.2f}, {angulo_C_graus:.2f}" )

def perimetro(lado_a, lado_b, lado_c):  
    perimetro = lado_a + lado_b + lado_c
    print(f"O perímetro do triângulo é {perimetro:.2f}")

def calcular_area_por_determinante(x1, y1, x2, y2, x3, y3):
    determinante = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    area = 0.5 * abs(determinante)
    print(f"A área é de {area:.2f}")

def eh_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a != b and a != c and b != c:
            print("O triângulo é escaleno")
        elif a == b and b == c:
            print("O triângulo é equilátero")
        else:
            print("O triângulo é isósceles")

def eh_triangulo2(a, b, c):
    if a + b > c and b + c > a and a + c > b:

        a_squared = a**2
        b_squared = b**2
        c_squared = c**2
        
        if a_squared + b_squared == c_squared or b_squared + c_squared == a_squared or a_squared + c_squared == b_squared:
            print("O triângulo é retângulo")
        elif a_squared + b_squared < c_squared or b_squared + c_squared < a_squared or a_squared + c_squared < b_squared:
            print("O triângulo é obtuso")
        else:
            print("O triângulo é agudo")

def main():
    ponto_A = (2, 2)
    ponto_B = (5, 2)
    ponto_C = (3.5, 2 + 3 * (3 ** 0.5))

    a, b, c = lados(ponto_A, ponto_B, ponto_C)
    print(f"O lado A é {a:.2f}, o lado B é {b:.2f} e o lado C é {c:.2f}")

    angulos(a, b, c)
    perimetro(a, b, c)
    calcular_area_por_determinante(ponto_A[0], ponto_A[1], ponto_B[0], ponto_B[1], ponto_C[0], ponto_C[1])
    eh_triangulo(a, b, c)
    eh_triangulo2(a, b, c)

main()
