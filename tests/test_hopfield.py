import unittest
import numpy as np
import hmip.hopfield as hop


class TestHopfield(unittest.TestCase):
    def setUp(self):
        self.H = np.array([[2, 0], [0, 1]])
        self.q = np.array([-2.7, -1.8])
        self.k_max = 20
        self.binary_indicator = np.array([0, 1])
        self.beta = 1
        self.ub = np.array([1, 1])
        self.lb = np.array([0, 0])
        self.L = 1

    def test_hopfield_default(self):
        x, x_h, f_val_hist, step_size = hop.hopfield(self.H, self.q, self.lb, self.ub, self.binary_indicator,
                                                     k_max=self.k_max)
        self.assertEqual(x.shape[0], self.q.shape[0])
        self.assertEqual(x.shape[1], self.k_max)

    def test_hopfield_step_type_classic(self):
        x, x_h, f_val_hist, step_size = hop.hopfield(self.H, self.q, self.lb, self.ub, self.binary_indicator,
                                                     k_max=self.k_max,
                                                     step_type='classic')

    def test_hopfield_step_type_armijo(self):
        x, x_h, f_val_hist, step_size = hop.hopfield(self.H, self.q, self.lb, self.ub, self.binary_indicator,
                                                     k_max=self.k_max,
                                                     step_type='armijo')

    def test_hopfield_step_type_wrong(self):
        pass


class TestOthers(unittest.TestCase):
    def setUp(self):
        self.dim = 10
        self.H = np.array([[2, 0], [0, 1]])

    def test_create_initial_ascent(self):
        pass

    def test_compute_inverse_activation(self):
        pass

    def test_compute_binary_absorption_mask(self):
        pass

    def test_smoothness_coefficient(self):
        output = hop.smoothness_coefficient(self.H)
        max_eigen_values = 2
        self.assertEqual(output, max_eigen_values)

    def test_alpha_hop(self):
        pass


class TestHopfieldUpdate(unittest.TestCase):
    def setUp(self):
        pass

    def test_hopfield_update(self):
        pass


class TestFindDirection(unittest.TestCase):
    def setUp(self):
        pass

    def test_find_direction_type_classic(self):
        pass

    def test_find_direction_type_stochastic(self):
        pass