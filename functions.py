__author__ = 'Cristina'

from periodic_table import elements, CHNOPS

def print_periodic_table(restrict):
    print "element".ljust(10) + "#isotopes".center(11) + "most freq".rjust(12)
    if restrict:
        list = CHNOPS
    else:
        list = elements
    for element in list:
        print element['name'].ljust(10) + str(len(element['isotopes'])).center(11) + str(int(round(element['freqisotope']['mass']))).rjust(12)

def get_formula_string(formula):
    return ''.join([element['symbol'] + str(number) for element, number in formula.iteritems() if number])

def get_formula_mass(formula):
    return sum([element['freqisotope']['mass'] * number for element,number in formula.iteritems()])