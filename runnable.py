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

incorrect_input = "\n The input was not correctly formatted \n restarting..."


def run_locally():
    """
    Run from console
    Enter manually: 1 mass and 1 tolerance (in ppm)
    :return: print formulas
    """

    try:
        # display algorithms
        i = 1
        for solver in solvers_basic:
            print str(i) + " " + prettyprint_solver(solver)
            i += 1
        for solver in solvers_7rules:
            print str(i) + " " + prettyprint_solver(solver)
            i += 1
        print

        # get input from user
        algorithm = int(input("Enter number for your choice: "))
        mass = float(input("Enter a mass: "))
        tolerance = float(input("Enter a tolerance (in ppm): ")) / 1000000
        if algorithm <= len(solvers_basic):
            function = solvers_basic[algorithm-1]
        else:
            function = solvers_7rules[algorithm - len(solvers_basic) - 1]
        print function
        print
        print "Would you like to restrict the search to CHNOPS? (recommended)"
        choice = raw_input("Enter y/n: ")
        restrict = False
        if choice == 'y':
            restrict = True
        print


        # perform search using input
        t1 = datetime.datetime.utcnow()
        formulas = function.search(mass, tolerance, delta, restrict)
        t2 = datetime.datetime.utcnow()
        for formula in formulas:
            print get_formula_string(formula)
        if len(formulas) == 0:
            print "No results"
        print "Search time: " + str(t2 - t1)
        print

        # get input for filtering and proceed as required
        print "Would you like to filter these? "
        choice = raw_input("Enter y/n: ")
        if choice == 'y':
            t1 = datetime.datetime.utcnow()
            formulas_filtered = the_7rules.filter_all(formulas, restrict)
            for formula in formulas_filtered:
                print get_formula_string(formula)
            if len(formulas_filtered) == 0:
                print "No results"
            t2 = datetime.datetime.utcnow()
            print "Filter time: " + str(t2-t1)
        print

        # ask if to terminate
        print "This iteration is done, would you like to go again? "
        choice = raw_input("Enter y/n: ")
        if choice == 'y':
            run_locally()
    except SyntaxError:
        print incorrect_input
        run_locally()
    except NameError:
        print incorrect_input
        run_locally()


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
        file_handler_filtered = write_file_header(output_file_filtered, True)
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

    # run_for_file('testingthis.txt', '', True)

    run_locally()

    """
    sys.setrecursionlimit(1500)

    run_for_file("Large.txt", "input_files", restricted)
    print "large done"
    """


    # run_for_frank()
    print "Done"
