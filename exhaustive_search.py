__author__ = 'Cristina'

from periodic_table import elements
# computation error allowed
delta = 0.00000000001

def get_formula_string(formula):
    return ' '.join([str(number) + element['symbol'] for (element, number) in formula if number])

def get_formula_mass(formula):
    return sum([element['freqisotope']['mass'] * number for (element,number) in formula])

def build_new_formula(formula, element_added):
    new_formula = []
    for (element, number) in formula:
        if element == element_added:
            new_formula.append((element, number+1))
        else:
            new_formula.append((element,number))
    return new_formula

def helper_search(mass_min, mass_max, formula_mass, formula, last_index):
    # only get here if formula_mass <= mass_max, but still some mass left
    for index, (element, number) in enumerate(formula):
        if index >= last_index:
            new_formula_mass = formula_mass + element['freqisotope']['mass']
            if mass_max - new_formula_mass >= -delta:
                new_formula = build_new_formula(formula, element)
                if new_formula_mass - mass_min >= -delta:
                    # formula in tolerance interval
                    formulas.append(new_formula)
                else:
                    # still some mass left
                    helper_search(mass_min, mass_max, new_formula_mass, new_formula, index)


def search(mass, tolerance):
    global formulas
    formulas = []
    formula = [(element, 0) for element in elements]
    helper_search(mass-tolerance, mass+tolerance, 0, formula, 0)
    return formulas