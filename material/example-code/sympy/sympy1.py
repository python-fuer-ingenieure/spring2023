import sympy as sp
x = sp.Symbol('x')
a, b, c = sp.symbols('a b c') # verschiedene Wege Symbole zu erzeugen

z = a*b*x*b + b**2*a*x - c*b*(2*a/c*x*b-1/(b*2))
print(z)  # -> -b*c*(-1/(2*b) + 2*a*b*x/c) + 2*a*x*b**2
print(z.expand())  # -> c/2 (Ausmutiplizieren)

# Funktionen anwenden:
y = sp.sin(x)*sp.exp(3*x)*sp.sqrt(a)
print(y) # -> a**(1/2)*exp(x)*sin(x)

# Eigene Funktionen definieren
f1 = sp.Function('f') # -> sympy.core.function.f (nicht ausgewertet)
g1 = sp.Function('g')(x) # -> g(x)    (Funktion ausgewertet bei x)


# Differenzieren
print(y.diff(x))  # -> 3*sqrt(a)*exp(3*x)*sin(x) + sqrt(a)*exp(3*x)*cos(x)
print(g1.diff(x))  # -> Derivative(g(x), x)

# Vereinfachungen:
print(sp.trigsimp(sp.sin(x)**2+sp.cos(x)**2)) # -> 1
