__author__ = 'Cristina'

from periodic_table import CHNOPS, elements


def helper_search(mass_min, mass_max, formula_mass, formula, last_index, delta):
    # only get here if formula_mass <= mass_max, but still some mass left
    for index, element in enumerate(formula):
        if index >= last_index:
            new_formula_mass = formula_mass + element['freqisotope']['mass']
            if mass_max - new_formula_mass >= -delta:
                new_formula = formula.copy()
                new_formula[element] += 1
                if new_formula_mass - mass_min >= -delta:
                    # formula in tolerance interval, add it to solutions
                    formulas.append(new_formula)
                else:
                    # still some mass left, keep searching
                    helper_search(mass_min, mass_max, new_formula_mass, new_formula, index, delta)


def search(mass, tolerance, delta, restrict):
    """
    :param mass: the formula mass
    :param tolerance: tolerance to accomodate equipment errors
    :param delta: computation error allowed
    :param restrict: boolean which if true indicates to use only CHNOPS
    :return:
    """
    global formulas
    formulas = []
    if restrict:
        formula = {element: 0 for element in CHNOPS}
    else:
        formula = {element: 0 for element in elements}
    helper_search(mass - tolerance, mass + tolerance, 0, formula, 0, delta)
    return formulas