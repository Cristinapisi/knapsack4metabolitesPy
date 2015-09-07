import sys
import fractions
import datetime
from periodic_table import *

# Scale for better precision
# Set as a power of 10, between 10^1 and 10^6
# Be wary of precision - time trade-off
b = 1000

# Set infinity
infinite = sys.maxint


def find_n(n, p, d):
    minimum = infinite
    for q, elem in enumerate(n):
        if q % d == p:
            if elem < minimum:
                minimum = elem
    return minimum


def round_robin(a, filename):
    file_handler = open(filename, 'w')
    file_handler.write("Precision: " + str(b) + '\n')

    # initialize the variables
    k = len(a)
    a1 = a[0]
    n = [infinite for r in range(0, a1)]
    n[0] = 0

    file_handler.write(str(n) + '\n')

    for i in range(1, k):
        d = fractions.gcd(a1, a[i])
        for p in range(0, d):
            new_n = find_n(n, p, d)
            if new_n < infinite:
                for repeat in range(1, a1/d):
                    new_n = new_n + a[i]
                    r = new_n % a1
                    new_n = min(new_n, n[r])
                    n[r] = new_n
        file_handler.write(str(n) + '\n')

    file_handler.close()


if __name__ == '__main__':

    time_start = datetime.datetime.utcnow()

    sorted_CHNOPS = [HYDROGEN, CARBON, NITROGEN, OXYGEN, PHOSPHORUS, SULFUR]
    sorted_elements = [HYDROGEN, CARBON, NITROGEN, OXYGEN, FLUORINE, NATRIUM, PHOSPHORUS, SULFUR, CHLORINE, BROMINE, IODINE]

    masses_CHNOPS = [int(round(e['freqisotope']['mass'] * b)) for e in sorted_CHNOPS]
    masses_elements = [int(round(e['freqisotope']['mass'] * b)) for e in sorted_elements]

    round_robin([5, 8, 9, 12], "rt_testing.txt")
    round_robin(masses_CHNOPS, "rt_CHNOPS.txt")
    round_robin(masses_elements, "rt.txt")

    time_end = datetime.datetime.utcnow()

    print "All computations successul in " + str(time_end - time_start)