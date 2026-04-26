import matplotlib.pyplot as plt
from src import processamento
import pygame

nextSceane2 = pygame.USEREVENT + 6
priorSceane2 = pygame.USEREVENT + 7

def next():
    pygame.event.post(pygame.event.Event(nextSceane2))

def prior():
    pygame.event.post(pygame.event.Event(priorSceane2))

def graficos(massa, velocidade, campo, carga, forca, raio, aceleracao):
    # campos e valores
    categorias = ['massa', 'velocidade', 'campo magnetico', 'carga', 'força magnetica', 'raio', 'AC']
    valores = [massa, velocidade, campo, carga, forca, raio, aceleracao]
    cores = ['#f99201', "#b80538", "#6905a3", "#0CC1C4", "#ce09b1", "#aeff17bf", '#ff0022']

    # customização
    fig, ax = plt.subplots()
    fig.patch.set_facecolor("#12263a")
    ax.set_facecolor('#12263a')
    ax.tick_params(colors='white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['top'].set_color('#1e1e1e')   
    ax.spines['right'].set_color('#1e1e1e') 
    bars = ax.bar(categorias, valores, color=cores)  
    ax.bar_label(bars, padding=3, color='white')  
    ax.set_ylim(0, max(valores) + 10)            

    fig.set_dpi(100) # Multiply this by the inches to get the number of pixels in the screen.
    fig.set_size_inches(15, 6.25, forward=True)

    # apresentação
    plt.savefig('CaduGay.png')