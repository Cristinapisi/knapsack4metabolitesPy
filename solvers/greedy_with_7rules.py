__author__ = '2168879m'

from periodic_table import CHNOPS, elements

def search(mass, tolerance, delta, restrict):
    global formulas
    formulas = []
    if restrict:
        formula = [(element, 0) for element in elements]
    else:
        formula = [(element, 0) for element in CHNOPS]
    return formulas
