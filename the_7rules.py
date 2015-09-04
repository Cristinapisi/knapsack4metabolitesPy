__author__ = 'Cristina'

from functions import get_formula_mass

def rule1(formula):
    """
    restrictions for the number of elements
    :param formula: a formula
    :return: true if it passes the test
    """
    mass = get_formula_mass(formula)
    if mass < 500:
        print 'nothing'
    elif mass < 1000:
        print 'nothing'
    elif mass < 2000:
        print 'nothing'
    elif mass < 3000:
        print 'nothing'


def filter(formulas):
    return formulas