# --- Inputs ---

from . import (
    massa, # Kg
    velocidade, # m/s
    campoMagnetico, # T
    carga # C
)

# --- Formulas ---
# Fc = Fm

# Fc = m . acp
# acp = v**2/ R

# Fm = qVxB = qvbsin T (sempre 90)

# mv = qbR

# Output Fc, R e Ac

def formula_mov_circular():
    """
    Retorna a força magnetica ou força centripeta e o raio de 
    UMA PARTÍCULA CARREGADA EM MOVIMENTO CIRCULAR.
    Recebe os inputs direto do menu de inputs.
    """
 
    Fm = carga*velocidade*campoMagnetico
    Raio = (massa*velocidade*velocidade)/Fm

    Fm = round(Fm, 2)
    Raio = round(Raio, 2)
    return Fm, Raio
