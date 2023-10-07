import matplotlib.pyplot as plt
import numpy as np

xx = np.linspace(-2, 2, 100)

mm = 1./25.4 # Umrechnung mm -> zoll
scale = 0.5 # Für proportionale Skalierung
fs = np.array([250*mm, 180*mm])*scale

# kleiner rechter Rand
plt.rcParams['figure.subplot.right'] = .98

# subplots: 1 Zeile, 2 Spalten
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=fs);

ax1.plot(xx, xx**2)
ax1.set_title("Subplot 1: $y=x^2$")

ax2.plot(xx, xx**3, lw=3)
ax2.set_title("Subplot 2: $y=x^3$")

ax1.plot(xx, xx*0+3, ":k") # gepunktete schwarze Linie bei y=3

plt.savefig('subplots.pdf') # Dateiformat wird aus Endung erkannt
plt.show() # Anzeige des Bildes
