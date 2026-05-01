import pygame, sys
from src import objects
from src.graficos import graficos, priorSceane2, nextSceane2, next, prior
from src.entradas import width, height
from src.entradas.button import Button

def integrated(massa, velocidade, campo, carga, forca, raio, aceleracao):
    graficos(abs(massa), abs(velocidade), abs(campo), abs(carga), abs(forca), abs(raio), abs(aceleracao))

    # --- Setting image an Background ---
    bg = pygame.image.load("resultados.png")
    w = 1500
    h = 625
    pygame.display.set_caption("Simulador - Grafico")
    screen = pygame.display.set_mode((w, h))
    font = pygame.font.SysFont('Verdana', 18)
    Button(font, screen, w-105, h-55, 100, 50, onClick=next, text="Prox")
    Button(font, screen, 0, h-55, 100, 50, onClick=prior, text="Anter")




    # --- Window response ---
    while True:

        for event in pygame.event.get():

            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == priorSceane2:
                objects.clear()
                return 2

            if event.type == nextSceane2:
                objects.clear()
                return 1

        # --- Updating screen and Setting order of 'toppings'---
        screen.blit(bg, (0, 0))
        for object in objects:
            object.process()
        pygame.display.flip()
