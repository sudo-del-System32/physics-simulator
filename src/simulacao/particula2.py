import pygame
import sys
import math

# Constantes Físicas
e_charge = 1.60217663e-19
proton_mass = 1.67262192e-27
electron_mass = 9.1093837e-31

def desenhar_vetor(tela, cor, inicio_x, inicio_y, direcao_x, direcao_y, tamanho=60):
    """Função auxiliar para desenhar uma seta representando um vetor."""
    fim_x = inicio_x + direcao_x * tamanho
    fim_y = inicio_y + direcao_y * tamanho
    
    pygame.draw.line(tela, cor, (inicio_x, inicio_y), (fim_x, fim_y), 3)
    
    angulo = math.atan2(direcao_y, direcao_x)
    tamanho_ponta = 10
    ponto_esq = (fim_x - tamanho_ponta * math.cos(angulo - math.pi / 6), 
                 fim_y - tamanho_ponta * math.sin(angulo - math.pi / 6))
    ponto_dir = (fim_x - tamanho_ponta * math.cos(angulo + math.pi / 6), 
                 fim_y - tamanho_ponta * math.sin(angulo + math.pi / 6))
    
    pygame.draw.polygon(tela, cor, [(fim_x, fim_y), ponto_esq, ponto_dir])

def main():
    print("=== Simulador em Escala Real (Próton vs Elétron) ===")
    print("Dica: Velocidade = 1000 | Campo = 1.0\n")
    
    # 1. Coleta de Inputs
    try:
        v_0 = float(input("Velocidade inicial (m/s) [ex: 1000]: "))
        campo_b = float(input("Módulo do Campo Magnético (B em Tesla) [ex: 1.0]: "))
        sinal_q = int(input("Partícula (Digite 1 para Próton, ou -1 para Elétron): "))
    except ValueError:
        print("Erro: Insira apenas números válidos.")
        sys.exit()

    if sinal_q not in (1, -1):
        print("Erro: O sinal deve ser 1 ou -1.")
        sys.exit()
        
    if campo_b == 0:
        print("Erro: O campo magnético não pode ser zero.")
        sys.exit()
        
    if v_0 == 0:
        v_0 = 1.0

    # 2. Definindo a massa e carga com base na escolha
    massa = proton_mass if sinal_q == 1 else electron_mass
    carga = sinal_q * e_charge
    nome_particula = "Próton" if sinal_q == 1 else "Elétron"

    # 3. Calculando os valores físicos reais
    raio_metros = (massa * abs(v_0)) / (abs(carga) * abs(campo_b))
    
    # 4. Sistema de Câmera (Calculado apenas no início)
    raio_visual_px = 200.0
    px_por_metro = raio_visual_px / raio_metros
    metros_por_quadrado = 50.0 / px_por_metro

    # Setup do Pygame
    pygame.init()
    largura, altura = 800, 800
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Simulador Escala Real (CLIQUE AQUI ANTES DE USAR O TECLADO)")
    relogio = pygame.time.Clock()
    fonte = pygame.font.SysFont("Arial", 16)
    fonte_grande = pygame.font.SysFont("Arial", 20, bold=True)

    # Cores
    cor_fundo = (15, 15, 20)
    cor_grade = (40, 40, 50)
    cor_eixo = (100, 100, 120)
    cor_rastro = (200, 200, 200)
    cor_texto = (220, 220, 220)
    cor_velocidade = (50, 255, 50)
    cor_forca = (255, 100, 100)
    
    cor_particula = (255, 50, 50) if sinal_q > 0 else (50, 150, 255)

    centro_x, centro_y = largura // 2, altura // 2
    
    direcao_forca = -1 if (carga * campo_b) > 0 else 1
    
    fisico_x = 0.0
    fisico_y = -(direcao_forca * raio_metros)
    vel_x = v_0
    vel_y = 0.0

    velocidade_angular = -(carga * campo_b) / massa
    delta_angulo = 0.02 
    passo_tempo = abs(delta_angulo / velocidade_angular) 
    tempo_real = 0.0

    rastro = []
    tamanho_maximo_rastro = 2000

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                
            # Interatividade: Teclas únicas (apertar uma vez)
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    sinal_q *= -1 # Inverte a partícula
                    
                    massa = proton_mass if sinal_q == 1 else electron_mass
                    carga = sinal_q * e_charge
                    nome_particula = "Próton" if sinal_q == 1 else "Elétron"
                    cor_particula = (255, 50, 50) if sinal_q > 0 else (50, 150, 255)

                    raio_antigo = raio_metros
                    raio_metros = (massa * abs(v_0)) / (abs(carga) * abs(campo_b))
                    
                    fisico_x *= (raio_metros / raio_antigo)
                    fisico_y *= (raio_metros / raio_antigo)
                    
                    # Mantém o centro orbitando
                    vel_x *= -1
                    vel_y *= -1
                    
                    vel_mag_atual = math.hypot(vel_x, vel_y)
                    if vel_mag_atual != 0:
                        vel_x = (vel_x / vel_mag_atual) * abs(v_0)
                        vel_y = (vel_y / vel_mag_atual) * abs(v_0)

                    # --- CORREÇÃO DO ZOOM VISUAL ---
                    # Descobre qual o tamanho exato do círculo na tela antes de trocar a partícula
                    raio_visual_atual_px = raio_antigo * px_por_metro
                    
                    # Reajusta a câmera para o círculo continuar EXATAMENTE do mesmo tamanho visual
                    px_por_metro = raio_visual_atual_px / raio_metros
                    metros_por_quadrado = 50.0 / px_por_metro

                    velocidade_angular = -(carga * campo_b) / massa
                    passo_tempo = abs(delta_angulo / velocidade_angular) 
                    rastro.clear()

        # Interatividade: Teclas seguradas (para alterar velocidade continuamente)
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] or teclas[pygame.K_DOWN]:
            if teclas[pygame.K_UP]:
                v_0 *= 1.02 # Aumenta 2% a cada frame
            if teclas[pygame.K_DOWN]:
                v_0 /= 1.02 # Diminui 2% a cada frame

            raio_antigo = raio_metros
            raio_metros = (massa * abs(v_0)) / (abs(carga) * abs(campo_b))
            
            # Ajusta a posição sem mudar a escala da câmera, assim o círculo aumenta/diminui
            fisico_x *= (raio_metros / raio_antigo)
            fisico_y *= (raio_metros / raio_antigo)
            
            vel_mag_atual = math.hypot(vel_x, vel_y)
            if vel_mag_atual != 0:
                vel_x = (vel_x / vel_mag_atual) * abs(v_0)
                vel_y = (vel_y / vel_mag_atual) * abs(v_0)
                
            rastro.clear() # Limpa o rastro para não poluir a tela enquanto altera o raio

        # --- FÍSICA (Calculada em metros) ---
        vel_x_anterior = vel_x
        vel_y_anterior = vel_y
        
        vel_x = vel_x_anterior * math.cos(velocidade_angular * passo_tempo) - vel_y_anterior * math.sin(velocidade_angular * passo_tempo)
        vel_y = vel_x_anterior * math.sin(velocidade_angular * passo_tempo) + vel_y_anterior * math.cos(velocidade_angular * passo_tempo)
        
        fisico_x += ((vel_x + vel_x_anterior) / 2.0) * passo_tempo
        fisico_y += ((vel_y + vel_y_anterior) / 2.0) * passo_tempo
        tempo_real += passo_tempo

        # Convertendo de metros para pixels na tela
        tela_x = centro_x + (fisico_x * px_por_metro)
        tela_y = centro_y + (fisico_y * px_por_metro)

        rastro.append((int(tela_x), int(tela_y)))
        if len(rastro) > tamanho_maximo_rastro:
            rastro.pop(0)

        # --- DESENHO ---
        tela.fill(cor_fundo)

        passo_grade = 50
        for i in range(0, largura + 1, passo_grade):
            cor = cor_eixo if i == centro_x else cor_grade
            espessura = 2 if i == centro_x else 1
            pygame.draw.line(tela, cor, (i, 0), (i, altura), espessura)
            
        for i in range(0, altura + 1, passo_grade):
            cor = cor_eixo if i == centro_y else cor_grade
            espessura = 2 if i == centro_y else 1
            pygame.draw.line(tela, cor, (0, i), (largura, i), espessura)

        if len(rastro) > 1:
            pygame.draw.lines(tela, cor_rastro, False, rastro, 2)

        # Vetor Velocidade e Força
        direcao_vel_x = vel_x / abs(v_0)
        direcao_vel_y = vel_y / abs(v_0)
        desenhar_vetor(tela, cor_velocidade, tela_x, tela_y, direcao_vel_x, direcao_vel_y)

        direcao_forca_x = -fisico_x / raio_metros
        direcao_forca_y = -fisico_y / raio_metros
        desenhar_vetor(tela, cor_forca, tela_x, tela_y, direcao_forca_x, direcao_forca_y)

        pygame.draw.circle(tela, cor_particula, (int(tela_x), int(tela_y)), 6)

        # HUD
        textos_hud = [
            f"Velocidade: {v_0:g} m/s",
            f"Partícula: {nome_particula} (Massa: {massa:g} kg)",
            f"Carga: {'+' if sinal_q > 0 else ''}{e_charge:g} C",
            f"Campo B: {campo_b:g} T",
            f"Raio: {raio_metros:g} m",
            f"1 Quadrado (Grid) = {metros_por_quadrado:g} m",
            f"Tempo Real: {tempo_real:g} s",
            "",
            "Vetores:",
            " Verde = Velocidade",
            " Vermelho = Força Centrípeta",
            "",
            "--- CONTROLES ---",
            "[CLIQUE NA JANELA PARA ATIVAR]",
            "[ESPAÇO] Trocar Partícula",
            "[SEGURE SETAS] Mudar Velocidade"
        ]

        for i, texto in enumerate(textos_hud):
            imagem_texto = fonte.render(texto, True, cor_texto)
            tela.blit(imagem_texto, (10, 10 + (i * 25)))

        legenda_x = largura - 200
        legenda_y = 20
        titulo_b = fonte_grande.render("Vetor Campo (B)", True, cor_texto)
        tela.blit(titulo_b, (legenda_x, legenda_y))
        
        simbolo_centro = (legenda_x + 70, legenda_y + 45)
        pygame.draw.circle(tela, cor_texto, simbolo_centro, 15, 2)
        
        if campo_b > 0:
            pygame.draw.circle(tela, cor_texto, simbolo_centro, 4)
            estado_b = fonte.render("Saindo da Tela", True, cor_texto)
        else:
            pygame.draw.line(tela, cor_texto, (simbolo_centro[0]-7, simbolo_centro[1]-7), (simbolo_centro[0]+7, simbolo_centro[1]+7), 2)
            pygame.draw.line(tela, cor_texto, (simbolo_centro[0]+7, simbolo_centro[1]-7), (simbolo_centro[0]-7, simbolo_centro[1]+7), 2)
            estado_b = fonte.render("Entrando na Tela", True, cor_texto)
            
        tela.blit(estado_b, (legenda_x + 10, legenda_y + 70))

        pygame.display.flip()
        relogio.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()