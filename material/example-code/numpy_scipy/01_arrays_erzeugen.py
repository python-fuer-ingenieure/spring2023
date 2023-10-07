import numpy as np
x0 = np.arange(10) # wie range(...) nur mit arrays
x1 = np.linspace(-10, 10, 200)
        # 200 Werte: array([-10., -9.899497, ..., 10])
x2 = np.logspace(1,100, 1e4) # 10000 Werte, immer gleicher Quotient

x3 = np.zeros(10) # np.ones analog
x4 = np.zeros( (3, 5) ) # Achtung: nur ein Argument! (=shape)

x5 = np.eye(3)
x6 = np.diag( (1, 2, 3) ) # 3x3-Diagonalmatrix

x7 = np.random.rand(5) # array mit 5 Zufallszahlen
x8 = np.random.rand(4, 2) # array mit 8 Zufallszahlen (shape=(4, 2))

from numpy import r_, c_ # index-Tricks für rows und columns
x9 = r_[6, 5, 4.] # array([ 6.,  5.,  4.])
x10 = r_[x9, -84, x3[:2]] # array([ 6.,  5.,  4.,  -84, 0.,  1.])
x11 = c_[x9, x6 , x5] # in Spalten-Richtung stapeln -> 7x3 array
