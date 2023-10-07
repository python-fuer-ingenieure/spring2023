# -*- coding: utf-8 -*-
"""
Beispielskript zum Thema Indizierung
"""
import numpy as np

a = np.array ([10, 11, 12, 13, 14, 15])

# trivial mit int - Werten (wie bei Listen):
a[2] # -> 12
a[2:5] # -> 12 , 13 , 14
a[ -2:] # -> 14 , 15

# mit int - Sequenzen (das geht bei Listen nicht !)
# (Länge: egal)
idcs = [1, 3, 0, 1]
a[ idcs ] # -> 11, 13, 10, 11

# direkt :
a[[1, 3, 0, 1]]

# mit bool-Sequenzen ("Masken") (das geht bei Listen auch nicht !)
# (Länge muss passen)
idcs2 = [True, False, True, False, False, True]
a[ idcs2 ] # -> 10 , 12 , 15

# nützlich für sowas
a[ a > 11.5] # -> 12 , 13 , 14 , 15
# ... geht alles n - dimensional
