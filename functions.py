__author__ = 'Cristina'

from periodic_table import elements

def print_periodic_table():
    print "element".ljust(10) + "#isotopes".center(13) + "most frequent".center(15)
    for element in elements:
        print element['name'].ljust(10) + str(len(element['isotopes'])).center(13) + str(int(round(element['freqisotope']['mass']))).center(15)

def get_formula_string(formula):
    return ''.join([element['symbol'] + str(number) for (element, number) in formula if number])

def get_formula_mass(formula):
    return sum([element['freqisotope']['mass'] * number for (element,number) in formula])

def add_element_to_formula(formula, element_added):
    return [(element, number+1) if element == element_added else (element, number) for (element, number) in formula]