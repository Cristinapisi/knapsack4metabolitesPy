__author__ = 'Cristina'

from periodic_table import *
from functions import get_formula_mass


def element_numbers_restriction(formula, c, h, n, o, p, s, f, cl, br, restrict):
    """
    :param formula: the formula to check if in restrictions
    :param c: maximum number of carbon
    :param h: maximum number of hydrogen
    :param n: maximum number of nitrogen
    :param o: maximum number of oxygen
    :param p: maximum number of phosphorus
    :param s: maximum number of sulfur
    :param f: maximum number of fluorine
    :param cl: maximum number of chlorine
    :param br: maximum number of bromine
    :param restrict:  boolean which if true indicates to use only CHNOPS
    :return: True if the formula is outside restrictions
    """
    if formula[CARBON] > c or formula[HYDROGEN] > h or formula[NITROGEN] > n or formula[OXYGEN] > o or formula[
        PHOSPHORUS] > p or formula[SULFUR] > s:
        return True
    if not restrict:
        if formula[FLUORINE] > f or formula[CHLORINE] > cl or formula[BROMINE] > br:
            return True
    return False


def rule1(formula, restrict):
    """
    restrictions for the number of elements, from table 1 in 7 golden rules paper
    using the largest from the two sets, rather than a consecvent set
    :param formula: a formula
    :param restrict: True if the formula is within restrictions
    :return: true if it passes the test
    """
    mass = get_formula_mass(formula)
    if mass < 500:
        if element_numbers_restriction(formula, 39, 72, 20, 20, 9, 10, 16, 10, 5, restrict):
            return False
    elif mass < 1000:
        if element_numbers_restriction(formula, 78, 126, 25, 27, 9, 14, 34, 12, 8, restrict):
            return False
    elif mass < 2000:
        if element_numbers_restriction(formula, 156, 236, 32, 63, 9, 12, 48, 12, 10, restrict):
            return False
    elif mass < 3000:
        if element_numbers_restriction(formula, 162, 208, 48, 78, 6, 9, 16, 11, 8, restrict):
            return False
    return True


def rule2(formula):
    """
    second rule regards valences and has 3 conditions:
    i. sum of all valences must be even
    ii. sum of all valences >= 2* max valence
    iii. sum of all valences >= 2 * #atoms-1
    second condition was not implemented
    :param formula: a formula
    :return: True if the formula passed this test
    """
    valence_sum = 0
    atoms = 0
    for element, number in formula.iteritems():
        valence_sum += element['valence'] * number
        atoms += number
    if not (valence_sum % 2 == 0 and valence_sum >= 2 * atoms - 1):
        return False
    return True


def rule3():
    """
    not implemented, due to limited usefulness
    :return:
    """
    return True


def rule4(formula):
    """
    rule 4 concerns the hidrogen to carbon ratios
    :param formula: a formula
    :return: True if the formula passed this test
    """
    if formula[CARBON] > 0:
        h_c_ratio = formula[HYDROGEN] / formula[CARBON] * 1.0
        if not (6 > h_c_ratio > 0.1):
            return False
    return True


def rule5(formula, restrict):
    """
    rule 5 concerns NOPS to carbon ratios
    :param formula: a formula
    :return: True if the formula passed this test
    """
    if formula[CARBON] > 0:
        n_c_ratio = formula[NITROGEN] / formula[CARBON] * 1.0
        o_c_ratio = formula[OXYGEN] / formula[CARBON] * 1.0
        p_c_ratio = formula[PHOSPHORUS] / formula[CARBON] * 1.0
        s_c_ratio = formula[SULFUR] / formula[CARBON] * 1.0
        if not (4 > n_c_ratio and 3 > o_c_ratio and 2 > p_c_ratio and 3 > s_c_ratio):
            return False
        if not restrict:
            f_c_ratio = formula[FLUORINE] / formula[CARBON] * 1.0
            cl_c_ratio = formula[CHLORINE] / formula[CARBON] * 1.0
            br_c_ratio = formula[BROMINE] / formula[CARBON] * 1.0
            if not (6 > f_c_ratio and 2 > cl_c_ratio and 2 > br_c_ratio):
                return False
    return True


def rule6(formula):
    """
    rule 6 concerns NOPS ratio among each other
    :param formula: a formula
    :return: True if the formula passed this test
    """
    n = formula[NITROGEN]
    o = formula[OXYGEN]
    p = formula[PHOSPHORUS]
    s = formula[SULFUR]
    if (n > 1 and o > 1 and p > 1 and s > 1 and not (n < 10 and o < 20 and p < 4 and s < 3)) or \
            (n > 3 and p > 3 and p > 3 and not (n < 11 and o < 22 and p < 6)) or \
            (o > 1 and p > 1 and s > 1 and not (o < 14 and p < 3 and s < 3)) or \
            (n > 1 and p > 1 and s > 1 and not (p < 3 and s < 3 and n < 4)) or \
            (n > 6 and o > 6 and s > 6 and not (n < 19 and o < 14 and s < 8)):
        return False
    return True


def rule7():
    """
    not implemented, due to limited usefulness
    :return:
    """
    return True


def filter_formula(formula, restrict):
    """
    filter applying all the 7 golden rules to 1 formula
    :param formula: a formula
    :param restrict: True if the formula is within restrictions
    :return: True if it passes all tests
    """
    return rule1(formula, restrict) and rule2(formula) and rule3() and rule4(formula) and rule5(formula, restrict) and rule6(formula) and rule7()


def filter_all(formulas, restrict):
    """
    filter applying all the 7 golden rules to a list of formulas
    :param formulas: a list of formulas
    :param restrict: True if the formula is within restrictions
    :return: a list of formulas that have passed the test
    """
    filtered_formulas = []
    for formula in formulas:
        if filter_formula(formula, restrict):
            filtered_formulas.append(formula)
    return filtered_formulas
