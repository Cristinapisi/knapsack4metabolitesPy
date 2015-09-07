__author__ = 'Cristina'

import os
import datetime
import the_7rules
from periodic_table import *


def sorted_CHNOPS():
    return [HYDROGEN, CARBON, NITROGEN, OXYGEN, PHOSPHORUS, SULFUR]


def sorted_elements():
    return [HYDROGEN, CARBON, NITROGEN, OXYGEN, FLUORINE, NATRIUM, PHOSPHORUS, SULFUR, CHLORINE, BROMINE, IODINE]


def sorted_masses_with_blowup_CHNOPS(b):
    return [int(round(e['freqisotope']['mass'] * b)) for e in sorted_CHNOPS()]


def sorted_masses_with_blowup_elements(b):
    return [int(round(e['freqisotope']['mass'] * b)) for e in sorted_elements()]


def get_formula_string(formula):
    return ''.join([element['symbol'] + str(number) for element, number in formula.iteritems() if number])


def get_formula_mass(formula):
    return sum([element['freqisotope']['mass'] * number for element, number in formula.iteritems()])


def get_formula_mass_int(formula):
    return sum([element['freqisotope']['mass_int'] * number for element, number in formula.iteritems()])


def get_output_folder(filein, location, restrict):
    """

    :param filein: the file for which we process
    :param location: the location for this output folder
    :param restrict: True if CHNOPS restricted
    :return: a string for the output folder path
    """
    timestamp = str(datetime.datetime.utcnow().strftime("%b%d_%H%M%S"))
    output_folder = os.path.join(location, filein.split('.')[0], timestamp)
    if restrict:
        output_folder += "_CHNOPS_restricted"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    return output_folder


def prettyprint_solver(solver):
    return solver.__name__.split('.')[1]


def read_file(filein):
    """
    :param filein: the file path fron which to read
    :return: list of pairs read (mass, tolerance)
    """
    with open(filein, 'r') as f:
        data_in = f.read()
    f.close()
    return [(float(datum.split(', ')[0]), (float(datum.split(', ')[1])) / 1000000) for datum in data_in.splitlines()]


def write_file_header(fileout, post_7rules):
    f = open(fileout, 'w')
    if post_7rules:
        f.write("with post filtering using " + str(the_7rules) + '\n')
    else:
        f.write("no post filtering \n")
    f.write("mass".center(15) + "tolerance(ppm)".center(10) + "formula".center(20) + "mass delta".center(
        20) + "time elapsed".center(15) + "\n")
    f.flush()
    return f


def write_file_formulas(fileout, formulas, mass, tolerance, time):
    for formula in formulas:
        fileout.write(
            str(mass).rjust(15) + str(int(tolerance * 1000000)).rjust(10) + get_formula_string(formula).rjust(20) + str(
                get_formula_mass(formula) - mass).rjust(20) + str(time).rjust(20) + "\n")
    fileout.flush()


def print_periodic_table(restrict):
    """
    Prints to console a very short representation of the periodic table used
    :param restrict: True if CHNOPS_restricted
    :return:
    """
    print "element".ljust(10) + "#isotopes".center(11) + "most freq".rjust(12)
    if restrict:
        list = CHNOPS
    else:
        list = elements
    for element in list:
        print element['name'].ljust(10) + str(len(element['isotopes'])).center(11) + str(
            int(round(element['freqisotope']['mass']))).rjust(12)
