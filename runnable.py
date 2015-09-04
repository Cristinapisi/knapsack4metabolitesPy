import os

__author__ = 'Cristina'


"""
I plan to run experiments to test times for
  exhaustive vs greedy vs SIRIUS
  no 7rules vs post filtering with 7rules vs interleaved pruning with 7rules
  for each of the 3 solver strategies, which 7rules approach is best
"""

"""
Run this with python.
 - run_locally is used to search for solutions from console for a pair mass and tolerance
  for example, for Glucose, you would enter mass 180.06338811828 and tolerance 0 or 1 and expect C6H12O6
 - run_tests is used to search for solutions for a set of pairs of mass and tolerance, stored in a file, one pair per line, separated by a ','
    for example, look at Test_data_in.txt
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

Observations: this does not include the 7 golden rules at the moment
"""

import datetime
import the_7rules
from solvers import exhaustive_search, exhaustive_search_with_7rules, greedy, greedy_with_7rules, SIRIUS_knapsack, SIRIUS_knapsack_with_7rules
from functions import get_formula_string, get_formula_mass, print_periodic_table

solvers_basic = \
    {'exhaustive':          exhaustive_search,
     'greedy':              greedy,
     'knapsack':            SIRIUS_knapsack}

solvers_7rules = \
    {'exhaustive_7rules':   exhaustive_search_with_7rules,
     'greedy_7rules':       greedy_with_7rules,
     'knapsack_7rules':     SIRIUS_knapsack_with_7rules}

solvers_all = {}
solvers_all.update(solvers_basic)
solvers_all.update(solvers_7rules)

# computation error allowed
delta = 0.00000000001

incorrect_input = "Nope, not what I asked you to enter"

def read_file(input_file):
    # read mass and tolerance pairs
    with open(input_file,'r') as f:
        data_in = f.read()
    f.close()
    return [(float(datum.split(', ')[0]), (float(datum.split(', ')[1]))/1000000) for datum in data_in.splitlines()]

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

def run_tests(data, solver, post_7rules, output_file, delta, restrict):
    """
    :param data: input data as a list of pairs
    :param solver: a script solver
    :param post_7rules: boolean which indicated whether to run 7rule filtering post solution finding
    :param output_file: a string with the name of the output_files file
    :param delta: computation error allowed
    :param restrict: boolean which if true means to use only CHNOPS
    :return: list of formulas
    """

    # print all formulas found for that set
    f = open(output_file, 'w')
    f.write("using " + str(solver) + '\n')
    if post_7rules:
        f.write("with post filtering using "+ str(the_7rules) + '\n')
    else:
        f.write("no post filtering \n")
    f.write("mass".center(15) + "tolerance(ppm)".center(10) + "formula".center(20) + "mass delta".center(20) +  "time elapsed".center(15) + "\n")
    for (mass, tolerance) in data:
        t1 = datetime.datetime.utcnow()
        formulas = solver.search(mass, tolerance, delta, restrict)
        if post_7rules:
            formulas = the_7rules.filter_all(formulas, restrict)
        t2 = datetime.datetime.utcnow()
        for formula in formulas:
            f.write(str(mass).rjust(15) + str(int(tolerance*1000000)).rjust(10) + get_formula_string(formula).rjust(20) + str(get_formula_mass(formula)-mass).rjust(20) +str(t2-t1).rjust(20) + "\n")
    f.close()

def run_for_frank():
    """
    TO DO
    :return:
    """

if __name__ == '__main__':
    # run_locally(solvers_list['exhaustive'], delta)
    # run_locally(solvers_list['greedy'], delta)
    # run_locally(solvers_list['greedy_7rules'], delta)
    # run_locally(solvers_list['knapsack'], delta)
    # run_locally(solvers_list['knapsack_7rules'], delta)
    data_in = read_file('testingthis.txt')
    run_tests(data_in, exhaustive_search, True, 'thisresult.txt', delta, True)
    """
    restrict = True
    d_in = "input_files"
    d_out = "output_files"
    filenames = [(os.path.join(d_in, f), os.path.join(d_out,f)) for f in os.listdir(d_in) if os.path.isfile(os.path.join(d_in, f))]
    for (f_in, f_out) in filenames:
        data_in = read_file(f_in)
        for solver in solvers_all:
            run_tests(data_in, solvers_all[solver], False, f_out.split('.')[0]+"_"+solver+'.txt', delta, restrict)
        for solver in solvers_basic:
            run_tests(data_in, solvers_basic[solver], True, f_out.split('.')[0]+"_"+solver+'_post_7rules'+'.txt', delta, restrict)
    """
    # run_for_frank()
    print "Done"

