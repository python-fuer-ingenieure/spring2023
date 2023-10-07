import matplotlib.pyplot as plt
import numpy as np

alpha = np.linspace(0, 6.28, 100)
y = np.sin(alpha)

mm = 1./25.4 # Umrechnung mm -> zoll
fig = plt.figure(figsize=(250*mm, 180*mm)) # Abmessungen explizit vorgeben

plt.plot(alpha, y, label=r'$\sin(\alpha)$')
plt.xlabel(r'$\alpha$ in rad')
plt.ylabel('$y$')
plt.title('Sinusfunktion')
plt.legend() # Legende einblenden
plt.grid() # Gitterlinien einblenden

plt.savefig('test.pdf') # Dateiformat wird aus Endung erkannt
plt.show() # Anzeige des Bildes
