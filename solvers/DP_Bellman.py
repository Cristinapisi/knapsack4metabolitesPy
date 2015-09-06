import math
from functions import get_formula_mass, get_formula_string

__author__ = '2168879m'

from periodic_table import CHNOPS, elements


def helper_search(prev_row, max_c, element_list, last_index, repetitions, empty_formula, terminate):
    this_row = [(0, empty_formula)]
    while repetitions < 1 and last_index < len(element_list):
        last_index += 1
        if last_index == len(element_list):
            terminate = True
        else:
            this_mass = element_list[last_index]['freqisotope']['mass']
            repetitions = int(math.ceil(max_c / this_mass))
    repetitions -= 1
    if not terminate:
        this_mass = element_list[last_index]['freqisotope']['mass']
        this_mass_int = element_list[last_index]['freqisotope']['mass_int']
        for c in range(1, max_c):
            if max(this_mass, this_mass_int) > c:
                this_row.append(prev_row[c])
            else:
                (prev_mass, prev_formula) = prev_row[c]
                (other_mass, other_formula) = prev_row[c - this_mass_int]
                if prev_mass > max(this_mass, this_mass_int) + other_mass:
                    this_row.append(prev_row[c])
                else:
                    new_formula = other_formula.copy()
                    new_formula[element_list[last_index]] += 1
                    this_row.append((this_mass_int + other_mass, new_formula))
    return this_row, last_index, repetitions, terminate


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
        element_list = CHNOPS
    else:
        formula = {element: 0 for element in elements}
        element_list = elements

    # this algorithm work with int masses
    mass_total = int(math.floor(mass) + 1)

    # n is the enumber of decision points
    # for this unbounded implementation: n <= number_elements * mass
    # but early termination is implemented
    n = len(formula) * mass_total

    # initialise row 0
    odd_row = []
    even_row = [(0, formula) for i in range(0, mass_total)]

    i = 0
    last_index = -1
    repetitions = 0
    terminate = False
    while i < n and not terminate:
        i += 1
        if i % 2 == 0:
            (even_row, last_index, repetitions, terminate) = helper_search(odd_row, mass_total, element_list,
                                                                           last_index, repetitions, formula, terminate)
            (x, candidate) = even_row[-1]
            candidate_mass = get_formula_mass(candidate)
            if candidate_mass - mass > 2 * tolerance + delta and len(even_row) > 1:
                (x, candidate) = even_row[-2]
                candidate_mass = get_formula_mass(candidate)
            if candidate_mass + tolerance - mass >= -delta and mass + tolerance - candidate_mass >= -delta and not candidate in formulas:
                formulas.append(candidate)
        else:
            (odd_row, last_index, repetitions, terminate) = helper_search(even_row, mass_total, element_list,
                                                                          last_index, repetitions, formula, terminate)
            (x, candidate) = odd_row[-1]
            candidate_mass = get_formula_mass(candidate)
            if candidate_mass - mass > 2 * tolerance + delta and len(odd_row) > 1:
                (x, candidate) = odd_row[-2]
                candidate_mass = get_formula_mass(candidate)
            if candidate_mass + tolerance - mass >= -delta and mass + tolerance - candidate_mass >= -delta and not candidate in formulas:
                formulas.append(candidate)
    return formulas
