from classes.poligono import Poligono
from classes.circulo import Circulo
from classes.quadrado import Quadrado

def main():
    c1 = Circulo(5)
    print(f"Com base no raio de {c1.raio}, o valor da area e: {c1.area():.1f}cm^2.")
    print(f"Com base no raio de {c1.raio}, o valor do perimetro e: {c1.perimetro():.1f}cm.")

    q1 = Quadrado(10)
    print(f"Com base no comprimento dos lados de {q1.compri_lado} cm, o valor da area e: {q1.area():.1f}cm.")
    print(f"Com base no comprimento dos lados de {q1.compri_lado} cm, o valor do perimetro e: {q1.perimetro():.1f}cm.")

if __name__ == "__main__":
    main()