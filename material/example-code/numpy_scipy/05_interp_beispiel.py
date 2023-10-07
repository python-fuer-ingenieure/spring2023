# -*- coding: utf-8 -*-

"""
Beispielskript zu den Themen
 * Regression und Interpolation
 * splines
"""

import numpy as np
import scipy as sc
import pylab as pl

# Quelle: http://www.scipy.org/Cookbook/LinearRegression
# angepasst

#####################################################

# Regression

#####################################################

# Erzeugung von Beispieldaten (Lineare Funktion mit Rauschen)
n = 10
t = np.linspace(-5, 5, n) # unabhängige Variable
# Parameters der Nominaldaten
a = 0.02
b = 0.8
c = -1
# x = np.polyval([a, b, c], t) # alternativ: x = a*t+b
# Nominaldaten berechnen
x = a*t**2 + b*t + c # alternativ: np.polyval([a, b, c], t)

# Zufallsgenerator initialisieren -> "Reproduzierbren Zufall bewirken"
np.random.seed(3)
# Rauschen auf Nominaldaten addieren
x_noise = x + 0.6*np.random.randn(n)

# Lineare Regressison mit polyfit (Polynom vom Grad 1 -> 2 Koeffizienten: c1, c0)
(c1, c0) = np.polyfit(t, x_noise, 1)
xr = np.polyval([c1, c0], t) # Auswertung des Polynoms mit entsprechenden Koeffs

# Quadratische Regression (Polynom vom Grad 2 -> 3 Koeffizienten: c2, c1, c0)
c2, c1, c0 = np.polyfit(t, x_noise, 2)
xqr = np.polyval([c2, c1, c0], t)


# 1. Grafische Darstellung:

# Bildgröße wird in Zoll erwartet -> Umrechnungsfaktor
mm = 1./25.4 # mm to inch
fs = [90*mm, 60*mm]
pl.figure(figsize=fs) # benutzerdefinierte Bildgröße erzwingen

pl.plot(t, x_noise, 'ro') # Daten
pl.savefig('bsp3_1.pdf')
pl.plot(t, xr, lw=2) # lw = linewidth
pl.savefig('bsp3_2.pdf')
pl.plot(t, xqr, 'g--', lw=2)
pl.savefig('bsp3_3.pdf')


#####################################################

# Interpolation

#####################################################



# siehe auch:
# - http://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
# https://docs.scipy.org/doc/scipy/reference/reference/generated/scipy.interpolate.interp1d.html#scipy.interpolate.interp1d

# Normalerweise sollten alle imports an den Anfang einer .py-Datei.
# Davon wird hier abgewichen, damit man sieht, dass man das erst hier braucht:

from scipy.interpolate import interp1d

func1 = interp1d(t, x_noise) # `kind='linear'` ist standard
func0 = interp1d(t, x_noise, kind='nearest') # Ordnung 0 ist 'nearest' (neighbor)
func3 = interp1d(t, x_noise, kind=3) # kubischer spline

t_highres = np.linspace(t[0], t[-1], 100)

xi0 = func0(t_highres)
xi1 = func1(t_highres)
xi3 = func3(t_highres)

# 2. Grafische Darstellung (neues Bild):
pl.figure(figsize=fs) # benutzerdef. Bildgröße erzwingen

pl.plot(t, x_noise, 'ro',) # Daten
pl.plot(t_highres, xi0, 'bo', ms=2)
pl.plot(t_highres, xi1, 'g', lw=1.3)
pl.savefig('bsp3_4.pdf')
pl.plot(t_highres, xi3, 'k-', lw=2)
pl.savefig('bsp3_5.pdf')


#####################################################

# "Smoothing Spline" (Geglättener Spline, also stückweise polynomiale Funktion)
# siehe auch:
# - http://www.scipy.org/Cookbook/Interpolation
# - https://docs.scipy.org/doc/scipy/reference/reference/generated/scipy.interpolate.splrep.html#scipy.interpolate.splrep

#####################################################


from scipy.interpolate import splrep, splev
# Spline-Parameter:
s = 0.4 # Glättungs-Parameter
k = 2 # Spline-Ordnung

# Spline-Objekte erzeugen
splobj1 = splrep(t, x_noise, s=s, k=k) # geglättet
splobj2 = splrep(t, x_noise, s=0.0, k=k) # ungeglättet (s=0)

# Werte der unabhängigen Variablen mit hoher Auflösung bestimmen
t_highres = np.linspace(t[0], t[-1], 100)

# Spline-Objekte für hochaufgelöste t-Werte auswerten
xspline = splev(t_highres, splobj1)
xspline2 = splev(t_highres, splobj2)


# 3. Grafische Darstellung (neues Bild):
pl.figure(figsize=fs) # benutzerdef. Bildgröße erzwingen

pl.plot(t, x_noise, 'ro') # Daten
pl.plot(t_highres, xspline, lw=1.5)
pl.savefig('bsp3_6.pdf')
pl.plot(t_highres, xspline2, 'g--', lw=2)
pl.savefig('bsp3_7.pdf')

pl.show()
