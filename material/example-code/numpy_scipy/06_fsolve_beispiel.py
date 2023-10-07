import numpy as np
from scipy import optimize

def fnc1(x):
    return x + 2.3*np.cos(x) - 1

sol = optimize.fsolve(fnc1, 0) # -> array([-0.723632])
# Probe:
print(sol, sol + 2.3*np.cos(sol)) # -> [-0.72363261] [1.]

