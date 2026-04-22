import sys
import pygame

pygame.init()
fps = 60

fpsClock = pygame.time.Clock()
width, height = 740, 500
pygame.display.set_caption("Simulador - Valores")
font = pygame.font.SysFont('Verdana', 18)

screen = pygame.display.set_mode((width, height))

inputCampo = pygame.Rect(200, 160, 140, 32)
textCampo = ""
campoActive = False

inputVelocidade = pygame.Rect(200, 220, 140, 32)
textVelocidade = ""
velocidadeActive = False

inputCarga = pygame.Rect(200, 280, 140, 32)
textCarga = ""
cargaActive = False

inputMassa = pygame.Rect(200, 340, 140, 32)
textMassa = ""
massaActive = False

colorActive = pygame.color.Color((62, 130, 142))
colorNotActive = pygame.color.Color('gray')

objects = []

class Button():
    def __init__(self, x, y, width, height, text="Ok", onClick=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.onClick = onClick
        self.onePress = onePress
        self.clicked = False

        self.fillColors = {
            'normal' : "#ffffff",
            'hover': '#dddddd',
            'pressed': '#aaaaaa',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height)) 
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height, border_radius=10) 

        self.buttonText = font.render(text, True, (20, 20, 20))   
        objects.append(self)

    def process(self):
        mousePosition = pygame.mouse.get_pos()
        # self.buttonSurface.fill(self.fillColors['normal'])
        cor_atual = self.fillColors['normal']
        if self.buttonRect.collidepoint(mousePosition):
            cor_atual = self.fillColors['hover']
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                # self.buttonSurface.fill(self.fillColors['pressed'])
                cor_atual = self.fillColors['pressed']
                if not self.clicked:
                    self.onClick()
                    self.clicked = True if not self.onePress else False  
            else: 
                self.clicked = False    
        self.buttonSurface.fill((18, 38, 58))
        pygame.draw.rect(self.buttonSurface, cor_atual, (0, 0, self.width, self.height), border_radius=10)
        self.buttonSurface.blit(self.buttonText, [
            self.buttonRect.width / 2 - self.buttonText.get_rect().width/2,
            self.buttonRect.height / 2 - self.buttonText.get_rect().height/2,
        ])   

        screen.blit(self.buttonSurface, self.buttonRect)                    

def myFunction():
           print(f"Dados finais: {campo}, {velocidade}, {carga}, {massa}")

Button(width/2 - 60, 400, 120, 35, "Salvar", myFunction)
                        
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
                    
    label1 = font.render("Campo Magnético (T):", True, (255, 255, 255))
    screen.blit(label1, (inputCampo.x, inputCampo.y - 25))
    color = colorActive if campoActive else colorNotActive
    pygame.draw.rect(screen, color, inputCampo, 2, border_radius=10)
    textSurface = font.render(textCampo, True, (255, 255, 255))
    screen.blit(textSurface, (inputCampo.x + 5, inputCampo.y + 5))
    inputCampo.w = max(320, textSurface.get_width() + 10)
   
    label2 = font.render("Velocidade (m/s):", True, (255, 255, 255))
    screen.blit(label2, (inputVelocidade.x, inputVelocidade.y - 25))
    color2 = colorActive if velocidadeActive else colorNotActive
    pygame.draw.rect(screen, color2, inputVelocidade, 2, border_radius=10)
    textSurface2 = font.render(textVelocidade, True, (255, 255, 255))
    screen.blit(textSurface2, (inputVelocidade.x + 5, inputVelocidade.y + 5))
    inputVelocidade.w = max(320, textSurface2.get_width() + 10)

    label3 = font.render("Carga (C):", True, (255, 255, 255))
    screen.blit(label3, (inputCarga.x, inputCarga.y - 25))
    color3 = colorActive if cargaActive else colorNotActive
    pygame.draw.rect(screen, color3, inputCarga, 2, border_radius=10)
    textSurface3 = font.render(textCarga, True, (255, 255, 255))
    screen.blit(textSurface3, (inputCarga.x + 5, inputCarga.y + 5))
    inputCarga.w = max(320, textSurface3.get_width() + 10)

    label4 = font.render("Massa (kg):", True, (255, 255, 255))
    screen.blit(label4, (inputMassa.x, inputMassa.y - 25))
    color4 = colorActive if massaActive else colorNotActive
    pygame.draw.rect(screen, color4, inputMassa, 2, border_radius=10)
    textSurface4 = font.render(textMassa, True, (255, 255, 255))
    screen.blit(textSurface4, (inputMassa.x + 5, inputMassa.y + 5))
    inputMassa.w = max(320, textSurface4.get_width() + 10)

    try:

        campo = float(textCampo)
        velocidade = float(textVelocidade)
        carga = float(textCarga)
        massa = float(textMassa)

        for object in objects:
         object.process()

    except ValueError: 
        textErro = font.render("Insira os valores:", True, (255, 255, 255))
        screen.blit(textErro, (70, 70))

        
        
    pygame.display.flip()
    fpsClock.tick(fps)