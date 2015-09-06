__author__ = 'Cristina'

import os
import datetime
import the_7rules
from periodic_table import elements, CHNOPS


def get_formula_string(formula):
    return ''.join([element['symbol'] + str(number) for element, number in formula.iteritems() if number])


def get_formula_mass(formula):
    return sum([element['freqisotope']['mass'] * number for element, number in formula.iteritems()])


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


def read_file(filein):
    """
    :param filein: the file path fron which to read
    :return: list of pairs read (mass, tolerance)
    """
    with open(filein, 'r') as f:
        data_in = f.read()
    f.close()
    return [(float(datum.split(', ')[0]), (float(datum.split(', ')[1])) / 1000000) for datum in data_in.splitlines()]


def write_file_header(fileout, solver, post_7rules):
    f = open(fileout, 'w')
    f.write("using" + str(solver) + '\n')
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


def solve(data, delta, restrict, solver, post_7rules, output_file, output_file_filtered):
    """
    :param data: input data as a list of pairs
    :param delta: computation error allowed
    :param restrict: boolean which if true means to use only CHNOPS
    :param solver: a script solver
    :param post_7rules: boolean which indicated whether to run 7rule filtering post solution finding
    :param output_file: a string with the name of the output_files file
    :return: list of formulas
    """
    file_handler = write_file_header(output_file, solver, False)
    if post_7rules:
        file_handler_filtered = write_file_header(output_file_filtered, solver, True)
    for (mass, tolerance) in data:
        t1 = datetime.datetime.utcnow()
        formulas = solver.search(mass, tolerance, delta, restrict)
        t2 = datetime.datetime.utcnow()
        if post_7rules:
            formulas_filtered = the_7rules.filter_all(formulas, restrict)
        t3 = datetime.datetime.utcnow()
        write_file_formulas(file_handler, formulas, mass, tolerance, t2-t1)
        if post_7rules:
            write_file_formulas(file_handler_filtered, formulas_filtered, mass, tolerance, t3-t1)
    file_handler.close()
    file_handler_filtered.close()


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
