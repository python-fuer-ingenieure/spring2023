# -*- coding: utf-8 -*-
"""
Beispielskript zum Thema broadcasting
"""

import numpy as np
import time

E = np.ones((4, 3))  # -> shape=(4, 3)
b = np.array([-1, 2, 7])  # -> shape=(3,)
print(E*b)  # -> shape=(4, 3)

b_13 = b.reshape((1, 3))
print(E*b_13)  # -> shape=(4, 3)

print("\n"*2, "Achtung, die nächste Anweisung erzeugt einen Fehler.")
time.sleep(2)

b_31 = b_13.T  # Transponieren -> shape=(3,1)
print(E*b_31) # broadcasting error
