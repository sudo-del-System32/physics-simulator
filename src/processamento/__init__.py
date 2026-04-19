# --- Inputs ---
# importar aqui os inputs

# --- Formulas ---
# Fc = Fm

# Fc = m . acp
# acp = v**2/ R

# Fm = qVxB = qvbsin T (sempre 90)

# mAc = qv2b

# Ac = qv2b/m

# mv = qbR

# Output Fc, R e Ac

def formula_mov_circular(massa: float, velocidade: float, campoMagnetico: float, carga: float):
    """
    Retorna a força magnetica ou força centripeta, raio e acelaração centripeta de 
    UMA PARTÍCULA CARREGADA EM MOVIMENTO CIRCULAR.
    Recebe os inputs direto do menu de inputs.
    """
 
    Fm = carga*velocidade*campoMagnetico
    Raio = (massa*velocidade*velocidade)/Fm
    Ac = Fm/massa

    Fm = round(Fm, 2)
    Raio = round(Raio, 2)
    Ac = round(Ac, 2)
    
    return Fm, Raio, Ac
