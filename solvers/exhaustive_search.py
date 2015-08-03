__author__ = 'Cristina'

from periodic_table import CHNOPS, elements
from functions import add_element_to_formula


def helper_search(mass_min, mass_max, formula_mass, formula, last_index, delta):
    # only get here if formula_mass <= mass_max, but still some mass left
    for index, (element, number) in enumerate(formula):
        if index >= last_index:
            new_formula_mass = formula_mass + element['freqisotope']['mass']
            if mass_max - new_formula_mass >= -delta:
                new_formula = add_element_to_formula(formula, element)
                if new_formula_mass - mass_min >= -delta:
                    # formula in tolerance interval, add it to rsolutions
                    formulas.append(new_formula)
                else:
                    # still some mass left, keep searching
                    helper_search(mass_min, mass_max, new_formula_mass, new_formula, index, delta)


def search(mass, tolerance, delta, restrict):
    global formulas
    formulas = []
    if restrict:
        formula = [(element, 0) for element in elements]
    else:
        formula = [(element, 0) for element in CHNOPS]
    helper_search(mass - tolerance, mass + tolerance, 0, formula, 0, delta)
    return formulas