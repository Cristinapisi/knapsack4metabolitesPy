import sys
import the_7rules

__author__ = 'Cristina'

"""
Run this with python.
 - run_locally is used to search for solutions from console for a pair mass and tolerance
  for example, for Glucose, you would enter mass 180.06338811828 and tolerance 0 or 1 and expect C6H12O6
 - run_tests is used to search for solutions for a set of pairs of mass and tolerance, stored in a file, one pair per line, separated by a ','
    for example, look at Small.txt
 - run_for_frank will work with the framework in which this will be integrated, called FRANK

Parameters:
 - what function to use:
        - exhaustive_search
        - knapsack  (not yet, TO DO)
        (presumably soon opting in or out of 7 golden rules)
        (maybe other variations in the future)
 - in and out files where appropriate
 - a delta which is set below as the computation error allowed.
    At the moment it is set at the lowest value that does not affect the correctness of results
    This is not the tolerance value for measurement errors, as those vary among experiments.
    This is to cope with the limitations of python for high precision floats equality.

"""

import os
import datetime
from solvers import exhaustive_search, exhaustive_search_7rules, DP_Bellman, DP_Bellman_7rules, knapsack, knapsack_7rules
from functions import get_formula_string, read_file, get_output_folder, write_file_header, write_file_formulas, \
    prettyprint_solver

solvers_basic = [exhaustive_search, DP_Bellman ]#,
#     'greedy': greedy,
#     'knapsack': knapsack}

solvers_7rules = [exhaustive_search_7rules, DP_Bellman_7rules] #,
#     'greedy_7rules': greedy_7rules,
#     'knapsack_7rules': knapsack_7rules}

# computation error allowed
delta = 0.00000000001
# True if only using CHNOPS
# There are no molecules outside CHNOPS in the data set.
restricted = True

incorrect_input = "Nope, not what I asked you to enter"


def run_locally(function, delta):
    """
    Run from console
    Enter manually: 1 mass and 1 tolerance (in ppm)
    :return: print formulas
    """

    try:
        mass = float(input("Enter a mass: "))
        tolerance = float(input("Enter a tolerance (in ppm): ")) / 1000000
        t1 = datetime.datetime.utcnow()
        formulas = function.search(mass, tolerance, delta, True)
        t2 = datetime.datetime.utcnow()
        for formula in formulas:
            print get_formula_string(formula)
        print "Search time: " + str(t2 - t1)
    except SyntaxError:
        print incorrect_input
    except NameError:
        print incorrect_input


def run_for_file(filein, location, restrict):
    data_in = read_file(os.path.join(location, filein))
    output_folder = get_output_folder(filein, "output_files", restrict)
    for solver in solvers_7rules:
        output_file = os.path.join(output_folder, prettyprint_solver(solver) + '.txt')
        file_handler = write_file_header(output_file, False)
        for (mass, tolerance) in data_in:
            t1 = datetime.datetime.utcnow()
            formulas = solver.search(mass, tolerance, delta, restrict)
            t2 = datetime.datetime.utcnow()
            write_file_formulas(file_handler, formulas,mass, tolerance, t2-t1)
        file_handler.close()
    for solver in solvers_basic:
        output_file = os.path.join(output_folder, prettyprint_solver(solver) + '.txt')
        output_file_filtered = os.path.join(output_folder, prettyprint_solver(solver) + '_post_7rules.txt')
        file_handler = write_file_header(output_file, False)
        file_handler_filtered = write_file_header(output_file_filtered, solver, True)
        for (mass, tolerance) in data_in:
            t1 = datetime.datetime.utcnow()
            formulas = solver.search(mass, tolerance, delta, restrict)
            t2 = datetime.datetime.utcnow()
            formulas_filtered = the_7rules.filter_all(formulas, restrict)
            t3 = datetime.datetime.utcnow()
            write_file_formulas(file_handler, formulas, mass, tolerance, t2-t1)
            write_file_formulas(file_handler_filtered, formulas_filtered, mass, tolerance, t3-t1)
        file_handler.close()
        file_handler_filtered.close()


def run_for_frank():
    """
    TO DO
    It will take some annotations as parameters, make the appropriate calls to solvers and return an annotation
    :return:
    """


if __name__ == '__main__':
    # run_locally(solvers_list['exhaustive'], delta)
    # run_locally(solvers_list['greedy'], delta)
    # run_locally(solvers_list['greedy_7rules'], delta)
    # run_locally(solvers_list['knapsack'], delta)
    # run_locally(solvers_list['knapsack_7rules'], delta)

    run_for_file('testingthis.txt', '', True)

    """
    sys.setrecursionlimit(1500)

    run_for_file("Large.txt", "input_files", restricted)
    print "large done"
    """


    # run_for_frank()
    print "Done"
