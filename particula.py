import pygame
import sys
import math

# Constantes Físicas
E_CHARGE = 1.60217663e-19
PROTON_MASS = 1.67262192e-27
ELECTRON_MASS = 9.1093837e-31

def main():
    print("=== Simulador em Escala Real (Próton vs Elétron) ===")
    print("Dica: Velocidade = 1000 | Campo = 1.0\n")
    
    # 1. Coleta de Inputs
    try:
        v_0 = float(input("Velocidade inicial (m/s) [ex: 1000]: "))
        B = float(input("Módulo do Campo Magnético (B em Tesla) [ex: 1.0]: "))
        sinal_q = int(input("Partícula (Digite 1 para Próton, ou -1 para Elétron): "))
    except ValueError:
        print("Erro: Insira apenas números válidos.")
        sys.exit()

    if sinal_q not in (1, -1):
        print("Erro: O sinal deve ser 1 ou -1.")
        sys.exit()
        
    if B == 0:
        print("Erro: O campo magnético não pode ser zero.")
        sys.exit()

    # 2. Definindo a massa e carga com base na escolha
    m = PROTON_MASS if sinal_q == 1 else ELECTRON_MASS
    q = sinal_q * E_CHARGE
    nome_particula = "Próton" if sinal_q == 1 else "Elétron"

    # 3. Calculando os valores físicos reais
    raio_metros = (m * abs(v_0)) / (abs(q) * abs(B))
    
    # 4. Sistema de Câmera (Zoom automático)
    # Fixamos o raio visual na tela para 200 pixels
    raio_visual_px = 200.0
    px_por_metro = raio_visual_px / raio_metros
    metros_por_quadrado = 50.0 / px_por_metro

    # Setup do Pygame
    pygame.init()
    WIDTH, HEIGHT = 800, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"Simulador Escala Real: {nome_particula}")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 16)
    font_large = pygame.font.SysFont("Arial", 20, bold=True)

    # Cores
    BG_COLOR = (15, 15, 20)
    GRID_COLOR = (40, 40, 50)
    AXIS_COLOR = (100, 100, 120)
    TRAIL_COLOR = (200, 200, 200)
    TEXT_COLOR = (220, 220, 220)
    
    if sinal_q > 0:
        PARTICLE_COLOR = (255, 50, 50) # Vermelho para positivo
    else:
        PARTICLE_COLOR = (50, 150, 255) # Azul para negativo

    # Posição central da tela em pixels
    cx, cy = WIDTH // 2, HEIGHT // 2
    
    # Direção da força inicial
    direcao_forca = -1 if (q * B) > 0 else 1
    
    # Posição e velocidade inicial no mundo físico (METROS)
    phys_x = 0.0
    phys_y = -(direcao_forca * raio_metros)
    vx = v_0
    vy = 0.0

    # Tempo dinâmico: avança um pequeno ângulo por frame para não explodir
    omega = -(q * B) / m
    d_theta = 0.02 
    dt = abs(d_theta / omega) 
    tempo_real = 0.0

    trail = []
    max_trail_length = 2000

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- FÍSICA (Calculada em metros) ---
        vx_old = vx
        vy_old = vy
        
        # Rotação da velocidade
        vx = vx_old * math.cos(omega * dt) - vy_old * math.sin(omega * dt)
        vy = vx_old * math.sin(omega * dt) + vy_old * math.cos(omega * dt)
        
        # Atualização da posição física
        phys_x += ((vx + vx_old) / 2.0) * dt
        phys_y += ((vy + vy_old) / 2.0) * dt
        tempo_real += dt

        # Convertendo de metros para pixels na tela
        screen_x = cx + (phys_x * px_por_metro)
        screen_y = cy + (phys_y * px_por_metro)

        trail.append((int(screen_x), int(screen_y)))
        if len(trail) > max_trail_length:
            trail.pop(0)

        # --- DESENHO ---
        screen.fill(BG_COLOR)

        # Desenhando a malha (Grid)
        step = 50
        for i in range(0, WIDTH + 1, step):
            color = AXIS_COLOR if i == cx else GRID_COLOR
            thickness = 2 if i == cx else 1
            pygame.draw.line(screen, color, (i, 0), (i, HEIGHT), thickness)
            
        for i in range(0, HEIGHT + 1, step):
            color = AXIS_COLOR if i == cy else GRID_COLOR
            thickness = 2 if i == cy else 1
            pygame.draw.line(screen, color, (0, i), (WIDTH, i), thickness)

        # Desenhando o rastro
        if len(trail) > 1:
            pygame.draw.lines(screen, TRAIL_COLOR, False, trail, 2)

        # Desenhando a partícula
        pygame.draw.circle(screen, PARTICLE_COLOR, (int(screen_x), int(screen_y)), 6)

        # Atualizando textos do HUD
        hud_texts = [
            f"Velocidade: {v_0:g} m/s",
            f"Partícula: {nome_particula} (Massa: {m:g} kg)",
            f"Carga: {'+' if sinal_q > 0 else ''}{E_CHARGE:g} C",
            f"Campo B: {B:g} T",
            f"Raio: {raio_metros:g} m",
            f"1 Quadrado (Grid) = {metros_por_quadrado:g} m",
            f"Tempo Real Decorrido: {tempo_real:g} s"
        ]

        for i, text in enumerate(hud_texts):
            img = font.render(text, True, TEXT_COLOR)
            screen.blit(img, (10, 10 + (i * 25)))

        # Legenda do Vetor B
        legenda_x = WIDTH - 200
        legenda_y = 20
        titulo_b = font_large.render("Vetor Campo (B)", True, TEXT_COLOR)
        screen.blit(titulo_b, (legenda_x, legenda_y))
        
        simbolo_centro = (legenda_x + 70, legenda_y + 45)
        pygame.draw.circle(screen, TEXT_COLOR, simbolo_centro, 15, 2)
        
        if B > 0:
            pygame.draw.circle(screen, TEXT_COLOR, simbolo_centro, 4)
            estado_B = font.render("Saindo da Tela", True, TEXT_COLOR)
        else:
            pygame.draw.line(screen, TEXT_COLOR, (simbolo_centro[0]-7, simbolo_centro[1]-7), (simbolo_centro[0]+7, simbolo_centro[1]+7), 2)
            pygame.draw.line(screen, TEXT_COLOR, (simbolo_centro[0]+7, simbolo_centro[1]-7), (simbolo_centro[0]-7, simbolo_centro[1]+7), 2)
            estado_B = font.render("Entrando na Tela", True, TEXT_COLOR)
            
        screen.blit(estado_B, (legenda_x + 10, legenda_y + 70))

        pygame.display.flip()
        clock.tick(120)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()