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
    :return: True if the formula is within restrictions
    """
    if restrict:
        if formula[CARBON] > c or formula[HYDROGEN] > h or formula[NITROGEN] > n or formula[OXYGEN] > o or formula[PHOSPHORUS] > p or formula[SULFUR] > s:
            return False
    elif formula[FLUORINE] > f or formula[CHLORINE] > cl or formula[BROMINE] > br:
        return False
    return True


def rule1(formula, restrict):
    """
    restrictions for the number of elements, from table 1 in 7 golden rules paper
    using the largest from the two sets, rather than a consecvent set
    :param formula: a formula
    :return: true if it passes the test
    """
    mass = get_formula_mass(formula)
    if mass < 500:
        element_numbers_restriction(formula, 39, 72, 20, 20, 9, 10, 16, 10, 5, restrict)
    elif mass < 1000:
        element_numbers_restriction(formula, 78, 126, 25, 27, 9, 14, 34, 12, 8,   restrict)
    elif mass < 2000:
        element_numbers_restriction(formula, 156, 236, 32, 63, 9, 12, 48, 12, 10,  restrict)
    elif mass < 3000:
        element_numbers_restriction(formula, 162, 208, 48, 78, 6, 9, 16, 11, 8, restrict)
    return True


def rule2():
    return True


def rule3():
    return True


def rule4():
    return True


def rule5():
    return True


def rule6():
    return True


def rule7():
    return True


def filter_all(formulas, restrict):

    for formula in formulas:
        if not (rule1(formula, restrict) and rule2() and rule2() and rule4() and rule5() and rule6() and rule7()):
            formulas.remove(formula)
    return formulas
