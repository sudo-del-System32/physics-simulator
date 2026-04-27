from src import objects
from src.entradas import (
    pygame, 
    sys,
    font, 
    width, height,

    fps,
    fpsClock,
    startSimulation,
    START_SIMULATION_EVENT
)

from src.entradas.button import Button
from src.processamento import formula_mov_circular
from src import processamento

def myFunction():
    pygame.event.post(START_SIMULATION_EVENT)

def create_label(
        screen: pygame.surface.Surface,
        name:str,
        text:str, 
        rect: pygame.Rect, 
        activatedColor: bool
    ):
    # Color for when input active and Button customization

    colorActive = pygame.color.Color((62, 130, 142))
    colorNotActive = pygame.color.Color('gray')

    label = font.render(name, True, (255, 255, 255))
    screen.blit(label, (rect.x, rect.y - 25))
    
    color = colorActive if activatedColor else colorNotActive
    pygame.draw.rect(screen, color, rect, 2, border_radius=10)
    
    textSurface = font.render(text, True, (255, 255, 255))
    screen.blit(textSurface, (rect.x + 5, rect.y + 5))
    
    rect.w = max(320, textSurface.get_width() + 10)





def start():
    
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()

    Button(font, screen, width/2 - 60, 400, 120, 35, text="Salvar", onClick=myFunction)
    # Data for customization of inputs boxes

    nameCampo: str = "Campo Magnético (T):"
    try:
        textCampo: str = str(processamento.campo)
    except AttributeError:
        textCampo: str = "" 
    inputCampo = pygame.Rect(200, 160, 140, 32)
    campoActive = False

    nameVelocidade: str = "Velocidade (m/s):"
    try:
        textVelocidade: str = str(processamento.velocidade) 
    except AttributeError:
        textVelocidade: str = "" 
    inputVelocidade = pygame.Rect(200, 220, 140, 32)
    velocidadeActive = False

    nameCarga: str = "Carga (C):"
    try:
        textCarga: str = str(processamento.carga)
    except AttributeError:
        textCarga: str = "" 
    inputCarga = pygame.Rect(200, 280, 140, 32)
    cargaActive = False

    nameMassa: str = "Massa (kg):"
    try:
        textMassa: str = str(processamento.massa)
    except AttributeError:
        textMassa: str = "" 
    inputMassa = pygame.Rect(200, 340, 140, 32)
    massaActive = False

    stop = False


    # functions
    while not stop:
    
        screen.fill((18, 38, 58))
        textErro = font.render("Simulador: Movimento Circular Uniforme de Uma Partícula Carregada", True, (255, 255, 255))
        screen.blit(textErro, (10, 10))
        
        for event in pygame.event.get():
            
            if event.type == startSimulation:
                stop = True
                objects.clear()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                velocidadeActive = inputVelocidade.collidepoint(event.pos)
                campoActive = inputCampo.collidepoint(event.pos)
                cargaActive = inputCarga.collidepoint(event.pos)
                massaActive = inputMassa.collidepoint(event.pos)

            if event.type == pygame.KEYDOWN:
        
                if campoActive:
        
                    if event.key == pygame.K_BACKSPACE:
                        textCampo = textCampo[:-1]
                    else:
                        textCampo += event.unicode
        
                elif velocidadeActive:
        
                    if event.key == pygame.K_BACKSPACE:
                        textVelocidade = textVelocidade[:-1]
                    else:
                        textVelocidade += event.unicode
        
                elif cargaActive:
        
                    if event.key == pygame.K_BACKSPACE:
                        textCarga = textCarga[:-1]
                    else:
                        textCarga += event.unicode        
        
                elif massaActive:
        
                    if event.key == pygame.K_BACKSPACE:
                        textMassa = textMassa[:-1]
                    else:
                        textMassa += event.unicode

        create_label(screen, nameCampo, textCampo, inputCampo, campoActive)

        create_label(screen, nameVelocidade, textVelocidade, inputVelocidade, velocidadeActive)

        create_label(screen, nameCarga, textCarga, inputCarga, cargaActive)
        
        create_label(screen, nameMassa, textMassa, inputMassa, massaActive)
        
        try:

            processamento.campo = float(textCampo)
            processamento.velocidade = float(textVelocidade)
            processamento.carga = float(textCarga)
            processamento.massa = float(textMassa)

            processamento.forca, processamento.raio, processamento.aceleracao, processamento.negativo = formula_mov_circular(processamento.massa, processamento.velocidade, processamento.campo, processamento.carga)

            for object in objects:
                object.process()

        except ValueError: 
            textErro = font.render("Insira os valores:", True, (255, 255, 255))
            screen.blit(textErro, (70, 70))

            
            
        pygame.display.flip()
        fpsClock.tick(fps)
    
    return 2