import numpy as np
from scipy.optimize import minimize


sensors = np.array([
    [0, 0],    
    [10, 0],   
    [0, 10]    
])


time_diffs = np.array([0.01, 0.015])  


speed_of_sound = 343


distance_diffs = time_diffs * speed_of_sound

def objective_function(p):
    x, y = p
    dist_A = np.sqrt((x - sensors[0, 0])*2 + (y - sensors[0, 1])*2)
    dist_B = np.sqrt((x - sensors[1, 0])*2 + (y - sensors[1, 1])*2)
    dist_C = np.sqrt((x - sensors[2, 0])*2 + (y - sensors[2, 1])*2)

    eq1 = dist_A - dist_B - distance_diffs[0]
    eq2 = dist_A - dist_C - distance_diffs[1]

    return eq1*2 + eq2*2


initial_guess = [5, 5]


result = minimize(objective_function, initial_guess, method='Nelder-Mead')

print("Estimated location of gunshot:", result.x)