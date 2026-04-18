import pygame
from re import match

PATTERN = r"^[0-9]+\.?[0-9]*$"

massa: float = 5
velocidade: float = 4
campoMagnetico: float = 0.5
carga: float = 12.52131


def main():
    while(1):
        x = input()
        if match(PATTERN, x):
            x = float(x)
            print(x)
        else:
            print("ERRO PRECISA SER UM NUMERO REAL!")


if __name__ == "__main__":
    main()
