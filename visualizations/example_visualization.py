import matplotlib.pyplot as plt
import numpy as np
from hmip.hopfield import HopfieldSolver
import visualizations.utils_visuals as visuals
import hmip.utils as utils

H = np.array([[2, 0], [0, 1]])
q = np.array([-2.7, -1.8])
k_max = 200
binary_indicator = np.array([0, 1])
ub = np.array([1, 1])
lb = np.array([0, 0])
H = utils.make_symmetric(H)
smoothness_coefficient = utils.smoothness_coefficient(H)
beta = np.array([10.0, 1.0])

objective_function = lambda x: 1 / 2 * np.dot(np.dot(x.T, H), x) + np.dot(q.T, x)
gradient = lambda x: np.dot(H, x) + q

# activation_types = ['sin', 'tanh', 'exp', 'pwl', 'identity']
activation_types = ['tanh']

for activation_type in activation_types:
    solver = HopfieldSolver(max_iterations=k_max, activation_type=activation_type)
    solver.setup_optimization_problem(objective_function, gradient, lb, ub, binary_indicator,
                                      smoothness_coef=smoothness_coefficient, beta=beta)
    x, x_h, f_val_hist, step_size = solver.solve_optimization_problem()

    visuals.plot_evolution_objective_function_2d(H, q, x, lb, ub, k_max, 'objective_function_2d.png')
    # visuals.plot_value_function(f_val_hist, 'value_function.png')
    # visuals.plot_step_size(step_size, 'step_size.png')
