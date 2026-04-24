import matplotlib.pyplot as plt

# campos e valores
categorias = ['massa', 'velocidade', 'campo magnetico', 'carga', 'força magnetica', 'raio', 'AC']
valores = [13, 43, 23.4, 12, 54, 34, 18]
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

# apresentação
plt.show()

