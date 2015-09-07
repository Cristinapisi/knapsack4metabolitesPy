import math
import fractions
from functions import CHNOPS, elements
from functions import sorted_masses_with_blowup_CHNOPS, get_formula_mass, sorted_CHNOPS

__author__ = 'Cristina'

def parse_rt(filein):
    with open(filein, 'r') as f:
        data_in = f.read()
    f.close()
    rows = data_in.splitlines()
    # set the same blowup factor
    b = int(rows[0].split()[1])

    parsed_rows = []
    for row in rows[1:]:
        row = row.split('[')[1].split(']')[0].split(',')
        parsed_rows.append([int(item) for item in row])
    return b, parsed_rows


def find_all(mass_in, mass, i, c, a, rt):
    if i == -1:
        c[0] = mass / a[0]
        formula = {elem: c[i] for i, elem, in enumerate(sorted_CHNOPS())}
        formula_mass = get_formula_mass(formula)
        if abs(formula_mass - mass_in) < 1:
            formulas.append(formula)
    else:
        lcm = a[0] * a[i] / fractions.gcd(a[0],a[i])
        l = lcm / a[i]
        for j in range(0, l):
            c[i] = j
            m = mass - j * a[i]
            r = m % a[0]
            lbound = rt[i-1][r]
            while m >= lbound:
                find_all(mass_in, m, i-1, c, a, rt)
                m = m - lcm
                c[i] = c[i] + l


def search(mass_in, tolerance, delta, restrict):
    global formulas
    formulas = []
    # read rt
    if restrict:
        b, rt_inverted_CHNOPS = parse_rt("rt_CHNOPS.txt")
    else:
        b, rt_inverted_CHNOPS = parse_rt("rt.txt")
    # initialize variables
    mass_int = int(math.floor(mass_in * b))
    k = len(rt_inverted_CHNOPS)
    c = [0 for i in range(0, k)]
    # setup the space of search, in terms of precision/tolerance
    precision_left = 5
    precision_right = 15
    if tolerance * b > precision_left:
        precision_left = int(math.ceil(tolerance * b))
    if tolerance * b > precision_right:
        precision_right = int(math.ceil(tolerance * b))
    for mass in range(mass_int - precision_left, mass_int + precision_right):
       find_all(mass_in, mass, k-1, c, sorted_masses_with_blowup_CHNOPS(b), rt_inverted_CHNOPS)

    return formulas