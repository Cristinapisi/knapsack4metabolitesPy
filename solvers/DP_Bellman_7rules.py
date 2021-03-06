__author__ = '2168879m'

import math
import the_7rules
from periodic_table import *
from functions import get_formula_mass

# scale up al masses for better precision
# but time trade-off
scalar = 1


def helper_search(prev_row, max_c, element_list, last_index, repetitions, empty_formula, terminate, restrict):
    this_row = [(0, empty_formula)]
    while repetitions < 1 and last_index < len(element_list):
        last_index += 1
        if last_index == len(element_list):
            terminate = True
        else:
            this_mass = element_list[last_index]['freqisotope']['mass'] * scalar
            this_mass_int = element_list[last_index]['freqisotope']['mass_int'] * scalar
            repetitions = int(math.ceil(max_c / min(this_mass, this_mass_int))) + 1
    repetitions -= 1
    if not terminate:
        this_mass = element_list[last_index]['freqisotope']['mass'] * scalar
        this_mass_int = element_list[last_index]['freqisotope']['mass_int'] * scalar
        for c in range(1, max_c):
            if min(this_mass, this_mass_int) < c:
                (prev_mass, prev_formula) = prev_row[c]
                (other_mass, other_formula) = prev_row[c - this_mass_int]
                if prev_mass < this_mass + other_mass:
                    new_formula = other_formula.copy()
                    new_formula[element_list[last_index]] += 1
                    if the_7rules.rule1(new_formula,restrict):
                        this_row.append((this_mass + other_mass, new_formula))
                    else:
                        this_row.append(prev_row[c])
                else:
                    this_row.append(prev_row[c])
            else:
                this_row.append(prev_row[c])
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
        # order is important, need to be decreasing
        element_list = [SULFUR, PHOSPHORUS, OXYGEN, NITROGEN, CARBON, HYDROGEN]
    else:
        formula = {element: 0 for element in elements}
        element_list = elements

    # scale the input data
    mass *= scalar
    tolerance *= scalar

    # this algorithm work with int masses
    mass_total = int(math.ceil(mass) + 1)


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
                                                                           last_index, repetitions, formula, terminate, restrict)
            (candidate_mass, candidate) = even_row[-1]
            if candidate_mass - mass > tolerance + delta and len(even_row) > 1:
                (candidate_mass, candidate) = even_row[-2]
                candidate_mass = get_formula_mass(candidate)
            if candidate_mass + tolerance - mass >= -delta and mass + tolerance - candidate_mass >= -delta and not candidate in formulas and the_7rules.filter_formula(
                    candidate, restrict):
                formulas.append(candidate)
        else:
            (odd_row, last_index, repetitions, terminate) = helper_search(even_row, mass_total, element_list,
                                                                          last_index, repetitions, formula, terminate, restrict)
            (candidate_mass, candidate) = odd_row[-1]
            if candidate_mass - mass > tolerance + delta and len(odd_row) > 1:
                (candidate_mass, candidate) = odd_row[-2]
            if candidate_mass + tolerance - mass >= -delta and mass + tolerance - candidate_mass >= -delta and not candidate in formulas and the_7rules.filter_formula(
                    candidate, restrict):
                formulas.append(candidate)
    return formulas
