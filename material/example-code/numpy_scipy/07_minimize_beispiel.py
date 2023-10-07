import numpy as np
from scipy import optimize

def fnc2(x):
    return (x + 2.3*np.cos(x) - 1)**2 # quadratischer Gleichungsfehler

res = optimize.minimize(fnc2, 0) # Optimierung mit Startschätzung 0
# Probe:
print(res.x, res.x + 2.3*np.cos(res.x)) # -> [-0.7236326] [1.00000004]

# mit Grenzen und veränderter Startschätzung -> andere Lösung
res = optimize.minimize(fnc2, 0.5, bounds=[(0, 3)])
# Probe:
print(res.x, res.x + 2.3*np.cos(res.x)) # -> [2.03999505] [1.00000003]
