import math

__author__ = '2168879m'

from periodic_table import CHNOPS, elements


def helper_search(prev_row, max_c, element_list, last_index, repetitions, empty_formula):
    this_row = [(0, empty_formula)]
    this_mass = element_list[last_index]['freqisotope']['mass_int']
    while repetitions < 1 and last_index < len(element_list)-1:
        last_index += 1
        this_mass = element_list[last_index]['freqisotope']['mass_int']
        repetitions = int(math.ceil(max_c / this_mass))
    repetitions -= 1
    for c in range(1, max_c):
        if this_mass > c:
            this_row.append(prev_row[c])
        else:
            (prev_mass, prev_formula) = prev_row[c]
            (other_mass, other_formula) = prev_row[c - this_mass]
            if prev_mass >= other_mass:
                this_row.append(prev_row[c])
            else:
                new_formula = other_formula.copy()
                new_formula[element_list[last_index]] += 1
                this_row.append((this_mass + other_mass, new_formula))
    print this_row
    return this_row, last_index, repetitions



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
    element_list = list(formula.keys())


    # this algorithm work with int masses
    mass_total = int(math.floor(mass) + 1)
    mass_left = mass_total

    # n is the enumber of decision points
    # for this unbounded implementation: n <= number_elements * mass

    # need lower estimate :(

    n = len(formula) * mass_total

    # initialise row 0
    odd_row = []
    even_row = [(0, formula) for i in range(0, mass_total)]

    i = 0
    last_index = 0
    repetitions = 0
    while i < n:
        i += 1
        if i % 2 == 0:
            (even_row, last_index, repetitions) = helper_search(odd_row, mass_total, element_list, last_index, repetitions, formula)
        else:
            (odd_row, last_index, repetitions) = helper_search(even_row, mass_total, element_list, last_index, repetitions, formula)

    print odd_row
    print even_row

    return formulas
