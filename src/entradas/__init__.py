import sys
import pygame

fps = 60

fpsClock = pygame.time.Clock()
width, height = 740, 500
pygame.display.set_caption("Simulador - Valores")
font = pygame.font.SysFont('Verdana', 18)

screen = pygame.display.set_mode((width, height))

startSimulation = pygame.USEREVENT + 1
START_SIMULATION_EVENT = pygame.event.Event(startSimulation)
