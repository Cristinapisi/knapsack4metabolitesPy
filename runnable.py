__author__ = 'Cristina'

"""
for Glucose
 enter mass 180.063388118 and tolerance 0
 expect C6H12O6
"""

import datetime
import exhaustive_search
import knapsack
from functions import get_formula_string

# computation error allowed
delta = 0.00000000001

incorrect_input = "Nope, not what I asked you to enter"

def run_locally(function, delta):
    """
    Run from console
    Enter manually: 1 mass and 1 tolerance (in ppm)
    :return: print formulas
    """

    try:
        mass = float(input("Enter a mass: "))
        tolerance = float(input("Enter a tolerance (in ppm): ")) /1000000
        t1 = datetime.datetime.utcnow()
        formulas = function.search(mass, tolerance, delta)
        t2 = datetime.datetime.utcnow()
        for formula in formulas:
            print get_formula_string(formula)
        print "Search time: " + str(t2 - t1)
    except SyntaxError:
        print incorrect_input
    except NameError:
        print incorrect_input

def run_tests(inputfile, outputfile, function, delta):
    """

    :param inputfile: String with the name of the input file
    :param outputfile: String with the name of the output file
    :param function: for which script to run search (exhaustive_search or knapsack)
    :return: list of formulas
    """
    # read mass and tolerance pairs
    with open(inputfile,'r') as f:
        data_in = f.read()
    f.close()
    data_in = [(float(datum.split(', ')[0]), (float(datum.split(', ')[1]))/1000000) for datum in data_in.splitlines()]

    # print all formulas found for that set
    f = open(outputfile, 'w')
    f.write("mass".center(15) + "tolerance(ppm)".center(10) + "formula".center(20) + "time elapsed".center(15) + "\n")
    for (mass, tolerance) in data_in:
        t1 = datetime.datetime.utcnow()
        formulas = function.search(mass, tolerance, delta)
        t2 = datetime.datetime.utcnow()
        for formula in formulas:
            f.write(str(mass).rjust(15) + str(int(tolerance*1000000)).rjust(10) + get_formula_string(formula).rjust(20) + str(t2-t1).rjust(15) + "\n")
    f.close()

def run_for_frank():
    """
    TO DO
    :return:
    """

if __name__ == '__main__':
    run_locally(knapsack, delta)
    # run_tests('Test_data_in.txt', 'Test_data_out.txt', exhaustive_search, delta)
    # run_tests('Test_data_in.txt', 'Test_data_out2.txt', knapsack, delta)
    # run_for_frank()
    print "Done"

