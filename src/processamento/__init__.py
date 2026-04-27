# --- Inputs ---
# importar aqui os inputs
global campo, velocidade, carga, massa
campo: float
velocidade: float 
carga: float 
massa: float
global forca, raio, aceleracao, negativo
forca: float
raio: float
aceleracao: float
negativo: bool


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
    negativo = False

    if massa <= 0:
        raise ValueError("Massa precisa ser um valor positivo.")
    if velocidade <= 0:
        raise ValueError("Velocdade precisa ser um valor positivo.")
    if campoMagnetico == 0:
        raise ValueError("CampoMagnetico não pode ser nulo.")
    if carga == 0:
        raise ValueError("Carga não pode ser nulo.")
    if carga < 0:
        carga = abs(carga)
        negativo = True

    Fm = abs(carga)*velocidade*abs(campoMagnetico)
    Raio = (massa*velocidade*velocidade)/Fm
    Ac = Fm/massa

    Fm = round(Fm, 2)
    Raio = round(Raio, 2)
    Ac = round(Ac, 2)
    
    return Fm, Raio, Ac, negativo
