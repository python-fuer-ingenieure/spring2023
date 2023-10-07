import numpy as np
a = np.arange(18)*2.0
A = np.array( [ [0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11] ] )

x1 = a[3] #  Element Nr. "3" (-> 6.0)
x2 = a[3:6] # Elemente 3 bis 5   -> array([  6.,   8.,  10.])
x3 = a[-3:] # Vom 3.-letzten bis Ende -> array([30.,32.,34.])
# Achtung a, x2 und x3 teilen sich die Daten!
a[-2:]*= -1
print(x3) # -> [-30.,-32.,-34.]

y1 = A[:, 0] # erste Spalte von A
y2 = A[1, :3 ] # ersten drei Elemente der zweiten Zeile
