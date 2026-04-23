from src.entradas import (
    pygame, 
    sys,
    font, 
    objects, 
    screen,

    width,
    fps,
    fpsClock
)

from src.entradas.button import Button


def myFunction():
    print(f"Dados finais: {campo}, {velocidade}, {carga}, {massa}")

def create_label(
        name:str,
        text:str, 
        rect: pygame.Rect, 
        activatedColor: bool
    ):

    label = font.render(name, True, (255, 255, 255))
    screen.blit(label, (rect.x, rect.y - 25))
    
    color = colorActive if activatedColor else colorNotActive
    pygame.draw.rect(screen, color, rect, 2, border_radius=10)
    
    textSurface = font.render(text, True, (255, 255, 255))
    screen.blit(textSurface, (rect.x + 5, rect.y + 5))
    
    rect.w = max(320, textSurface.get_width() + 10)


# Color for when input active and Button customization

colorActive = pygame.color.Color((62, 130, 142))
colorNotActive = pygame.color.Color('gray')

Button(width/2 - 60, 400, 120, 35, text="Salvar", onClick=myFunction)


def start():
    
    # Data for customization of inputs boxes

    nameCampo: str = "Campo Magnético (T):"
    textCampo: str = ""
    inputCampo = pygame.Rect(200, 160, 140, 32)
    campoActive = False

    nameVelocidade: str = "Velocidade (m/s):"
    textVelocidade: str = ""
    inputVelocidade = pygame.Rect(200, 220, 140, 32)
    velocidadeActive = False

    nameCarga: str = "Carga (C):"
    textCarga: str = ""
    inputCarga = pygame.Rect(200, 280, 140, 32)
    cargaActive = False

    nameMassa: str = "Massa (kg):"
    textMassa: str = ""
    inputMassa = pygame.Rect(200, 340, 140, 32)
    massaActive = False



    # functions
    
    while True:
    
        screen.fill((18, 38, 58))
        textErro = font.render("Simulador: Movimento Circular Uniforme de Uma Partícula Carregada", True, (255, 255, 255))
        screen.blit(textErro, (10, 10))
        
        for event in pygame.event.get():
        
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

        create_label(nameCampo, textCampo, inputCampo, campoActive)

        create_label(nameVelocidade, textVelocidade, inputVelocidade, velocidadeActive)

        create_label(nameCarga, textCarga, inputCarga, cargaActive)
        
        create_label(nameMassa, textMassa, inputMassa, massaActive)
        
        try:
            global campo
            campo = float(textCampo)
            global velocidade 
            velocidade = float(textVelocidade)
            global carga 
            carga = float(textCarga)
            global massa
            massa = float(textMassa)

            for object in objects:
                object.process()

        except ValueError: 
            textErro = font.render("Insira os valores:", True, (255, 255, 255))
            screen.blit(textErro, (70, 70))

            
            
        pygame.display.flip()
        fpsClock.tick(fps)
        