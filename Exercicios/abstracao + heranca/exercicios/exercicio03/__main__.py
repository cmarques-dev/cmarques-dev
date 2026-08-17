from classes.moto import Moto
from classes.drone import Drone
from classes.caminhao import Caminhao

def main():
    dist = 8

    entrega = Drone(dist)
    print(f"Frete de {type(entrega).__name__} para {dist}km e de: {entrega.cal_frete()}")

if __name__ == "__main__":
    main()