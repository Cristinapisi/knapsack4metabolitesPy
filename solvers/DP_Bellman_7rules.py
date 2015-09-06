__author__ = '2168879m'

from periodic_table import CHNOPS, elements


def helper_search(mass_min, mass_max, formula_mass, formula, last_index, delta):
    """
    This function is called when the formula_mass is less than the mass_max
    It attempts to add a new element and if still in the mass tolerance window calls itself recursively
    :param mass_min: Minimum mass accepted for solution
    :param mass_max: Maximum mass accepted for solution
    :param formula_mass: The mass of the formula now
    :param formula: The formula now
    :param last_index: The last element added
    :param delta: Computation error allowed
    :return: not explicit, it adds to global list of formulas
    """


def search(mass, tolerance, delta, restrict):
    """
    :param mass: the formula mass
    :param tolerance: tolerance to accommodate equipment errors
    :param delta: computation error allowed
    :param restrict: True indicates CHNOPS_restricted
    :return: a list of candidate formulas
    """
    global formulas
    formulas = []
    if restrict:
        formula = {element: 0 for element in CHNOPS}
    else:
        formula = {element: 0 for element in elements}
    helper_search(mass - tolerance, mass + tolerance, 0, formula, 0, delta)
    return formulas