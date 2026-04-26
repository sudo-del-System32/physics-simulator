from src import objects
import pygame

class Button():
    def __init__(
            self, 
            font: pygame.font.Font, screen: pygame.surface.Surface,
            x: float, 
            y: float,  
            width: float, 
            height: float, 
            onClick, 
            text: str = "Ok", 
            onePress=False
        ):

        self.font = font
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.onClick = onClick
        self.onePress = True
        self.clicked = False

        self.fillColors = {
            'normal' : "#ffffff",
            'hover': '#dddddd',
            'pressed': '#aaaaaa',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height)) 
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height) # tinha um , border_radius=10 mas eu tirei e nao mudou nada 

        self.buttonText = self.font.render(text, True, (20, 20, 20))
        objects.append(self)

    def process(self):
        mousePosition = pygame.mouse.get_pos()
        cor_atual = self.fillColors['normal']

        if self.buttonRect.collidepoint(mousePosition):
            cor_atual = self.fillColors['hover']
            # self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
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

        self.screen.blit(self.buttonSurface, self.buttonRect)                    
