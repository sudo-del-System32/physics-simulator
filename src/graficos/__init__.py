import matplotlib.pyplot as plt

# graficos iniciais dos resultaods da equação com os input
valores = [13, 43, 23.4, 12]
variaveis = ['massa', 'velocidade', 'campo magnetico', 'carga']
bars = plt.bar(variaveis, valores, color=["#9a840a", '#054f99', '#0d4502', '#790111'])
plt.bar_label(bars, padding=3)
plt.ylim(0, max(valores) + 5) 
plt.show()



# graficos posteriores de força
valores = [ 54, 34, 18]
variaveis = ['força magnetica', 'raio', 'AC']
bars = plt.bar(variaveis, valores, color=[ '#054f99', "#188802", '#F91900'])
plt.bar_label(bars, padding=3)
plt.ylim(0, max(valores) + 5) 
plt.show()