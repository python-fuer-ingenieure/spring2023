import numpy as np
from scipy.integrate import solve_ivp

delta = .1
omega_2 = 2**2
def rhs(t, z):
    """ rhs heißt 'right hand side [function]' """
    # Argument t muss in Signatur vorhanden sein, kann aber ignoriert werden
    z1, z2  = z # Entpacken des Zustandsvektors in seine zwei Komponenten
    z1_dot = z2
    z2_dot = -(2*delta*z2 + omega_2*z1)
    return [z1_dot, z2_dot]

tt = np.arange(0, 100, .01) # unabhängige Variable (Zeit)
z0 = [10, 0]   # Anfangszustand für z1 und z2 (=y, und y_dot)
res = solve_ivp(rhs, (tt[0], tt[-1]), z0, t_eval=tt) # Aufruf des Integrators
zz = res.y # Zustandsverlaufs-Array (Zeilen: Zustandskomponenten; Spalten: Zeitschritte)

from matplotlib import pyplot as plt
plt.plot(tt, zz[0, :]) # Verlauf von z1 plotten
plt.show()
