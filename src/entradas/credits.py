# from src import objects
from src import objects

from src.entradas import (
    pygame, 
    sys,
    font, 
    width, height,

    fps,
    fpsClock,
    startProgram,
    START_PROGRAM
)

from src.entradas.button import Button

def myFunction():
    pygame.event.post(START_PROGRAM)



def credits_menu():
    
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()

    Button(font, screen, width/2 -60, height-100, 120, 35, text="Continuar", onClick=myFunction)

    stop = False

    while not stop:
    
        screen.fill((18, 38, 58))
        textErro = font.render("Simulador: Movimento Circular Uniforme de Uma Partícula Carregada", True, (255, 255, 255))
        screen.blit(textErro, (100, 10))
        textErro = font.render("Creditos:", True, (255, 255, 255))
        screen.blit(textErro, (40, 100))
        h, l = 70, 150
        textErro = font.render("Daniel Bertini", True, (255, 255, 255))
        screen.blit(textErro, (h, l))
        textErro = font.render("Francisco Gabriel", True, (255, 255, 255))
        screen.blit(textErro, (h, l:=l+25))
        textErro = font.render("Carlos Eduardo Almeida", True, (255, 255, 255))
        screen.blit(textErro, (h, l:=l+25))
        textErro = font.render("Leticia Vitoria", True, (255, 255, 255))
        screen.blit(textErro, (h, l:=l+25))
        textErro = font.render("Renan", True, (255, 255, 255))
        screen.blit(textErro, (h, l:=l+25))
        textErro = font.render("João Paulo", True, (255, 255, 255))
        screen.blit(textErro, (h, l:=l+25))
        
        for event in pygame.event.get():
            
            if event.type == startProgram:
                stop = True
                objects.clear()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for object in objects:
                object.process()


            
            
        pygame.display.flip()
        fpsClock.tick(fps)
    
    return 2