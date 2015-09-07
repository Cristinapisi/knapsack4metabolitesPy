__author__ = 'Cristina'

"""
Run this with python.
 - run_locally is used to search for solutions from console for a pair mass and tolerance
  for example, for Glucose, you would enter mass 180.06338811828 and tolerance 0 or 1 and expect C6H12O6
 - run__for_file is used to search for solutions for a set of pairs of mass and tolerance, stored in a file, one pair per line, separated by a ','
    for example, look at Small.txt
 - run_for_frank will work with the framework in which this will be integrated; might be called FRANK
"""

import the_7rules
from solvers import exhaustive_search, exhaustive_search_7rules, DP_Bellman, DP_Bellman_7rules, knapsack
from functions import *

solvers_basic = [exhaustive_search, DP_Bellman, knapsack]
solvers_7rules = [exhaustive_search_7rules, DP_Bellman_7rules]

# computation error allowed
delta = 0.00000000001


# You should not use recursion in python for a depth of 1000 or more
# To run a recursive algorithm for masses > 999, uncomment the next line; strongly discourage bigger number
# sys.setrecursionlimit(1500)


def run_locally():
    """
    Run from console
    Enter manually: 1 mass and 1 tolerance (in ppm)
    :return: print formulas
    """

    # message for run_locally
    incorrect_input = "\n The input was not correctly formatted \n restarting..."

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
            function = solvers_basic[algorithm - 1]
        else:
            function = solvers_7rules[algorithm - len(solvers_basic) - 1]
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
            print "Filter time: " + str(t2 - t1)
        print

        # ask if to terminate
        print "This iteration is done, would you like to go again? "
        choice = raw_input("Enter y/n: ")
        if choice == 'y':
            run_locally()
    except SyntaxError as se:
        print incorrect_input
        run_locally()
    except NameError as ne:
        print incorrect_input
        run_locally()
    except IndexError as ie:
        print incorrect_input
        run_locally()


def run_for_file(filein, location, solver, restrict):
    data_in = read_file(os.path.join(location, filein))
    output_folder = get_output_folder(filein, "output_files", restrict)
    t_start = datetime.datetime.utcnow()
    if solver in solvers_7rules:
        output_file = os.path.join(output_folder, prettyprint_solver(solver) + '.txt')
        file_handler = write_file_header(output_file, False)
        for (mass, tolerance) in data_in:
            t1 = datetime.datetime.utcnow()
            formulas = solver.search(mass, tolerance, delta, restrict)
            t2 = datetime.datetime.utcnow()
            write_file_formulas(file_handler, formulas, mass, tolerance, t2 - t1)
        file_handler.close()
    elif solver in solvers_basic:
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
            write_file_formulas(file_handler, formulas, mass, tolerance, t2 - t1)
            write_file_formulas(file_handler_filtered, formulas_filtered, mass, tolerance, t3 - t1)
        file_handler.close()
        file_handler_filtered.close()
    t_end = datetime.datetime.utcnow()
    print prettyprint_solver(solver) + " processed " + filein + " in " + str(t_end - t_start)


def run_for_frank():
    """
    TO DO
    It will take some annotations as parameters, make the appropriate calls to solvers and return an annotation
    :return:
    """


if __name__ == '__main__':
    time_start = datetime.datetime.utcnow()

    # run from console
    run_locally()

    # There are no molecules outside CHNOPS in the data sets
    # Might as well restrict the search to CHNOPS
    restricted = True

    # run all on the Small dataset
    """
    solvers = solvers_basic + solvers_7rules
    for solver in solvers:
        run_for_file("Small.txt", "input_files", solver, restricted)
    """

    # run for exhaustive search with and without post filtering
    """
    run_for_file("Small.txt", "input_files", solvers_basic[0], restricted)
    run_for_file("Medium.txt", "input_files", solvers_basic[0], restricted)
    """

    # run for DP_Bellman with and without post filtering
    """
    run_for_file("Small.txt", "input_files", solvers_basic[1], restricted)
    run_for_file("Medium.txt", "input_files", solvers_basic[1], restricted)
    """

    # run for knapsack with and without post filtering
    """
    run_for_file("Small.txt", "input_files", solvers_basic[2], restricted)
    run_for_file("Medium.txt", "input_files", solvers_basic[2], restricted)
    """

    # run for exhaustive search with 7 rules pruning
    """
    run_for_file("Small.txt", "input_files", solvers_7rules[0], restricted)
    run_for_file("Medium.txt", "input_files", solvers_7rules[0], restricted)
    """

    # run for DP_Bellman with 7 rules pruning
    """
    run_for_file("Small.txt", "input_files", solvers_7rules[1], restricted)
    run_for_file("Medium.txt", "input_files", solvers_7rules[1], restricted)
    """

    time_end = datetime.datetime.utcnow()

    print "All computations successul in " + str(time_end - time_start)
