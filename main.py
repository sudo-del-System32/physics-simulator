import pygame

pygame.init() 

from src import processamento
from src.entradas.startMenu import start
from src.simulacao.particula2 import simulacao
from src.graficos import graficos

def main():
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
            next = graficos(
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
