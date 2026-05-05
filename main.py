import pygame

pygame.init() 

from src import processamento
from src.entradas.credits import credits_menu
from src.entradas.startMenu import start
from src.simulacao.particula2 import simulacao
from src.graficos.graphics import integrated

def main():
    credits_menu()

    next = 1
    while True:
        if next == 1:
            next = start()
        
        if next == 2:
            next = simulacao(
                processamento.velocidade, 
                processamento.campo,
                processamento.carga, 
                processamento.massa, 
                processamento.forca, 
                processamento.raio, 
                processamento.aceleracao,
                processamento.negativo
            )

        if next == 3:
            next = integrated(
                processamento.massa, 
                processamento.velocidade, 
                processamento.campo, 
                processamento.carga, 
                processamento.forca, 
                processamento.raio, 
                processamento.aceleracao
            )


if __name__ == "__main__":
    main()
