import fractions
from functions import sorted_masses_with_blowup_CHNOPS

__author__ = 'Cristina'
import datetime


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


def find_all(mass, i, c, a, rt):
    if i == 0:
        c[0] = mass / a[0]
        print c
    else:
        lcm = a[0] * a[i] / fractions.gcd(a[0],a[i])
        l = lcm / a[i]
        for j in range(0, l):
            c[i] = j
            m = mass - j * a[i]
            r = m % a[0]
            lbound = rt[i][r]
            while m >= lbound:
                find_all(mass, i-1, c, a, rt)
                m = m - lcm
                c[i] = c[i] + l

if __name__ == '__main__':

    time_start = datetime.datetime.utcnow()

#    b, rt_inverted_testing = parse_rt("rt_testing.txt")
#    b, rt_inverted = parse_rt("rt.txt")
    b, rt_inverted_CHNOPS = parse_rt("rt_CHNOPS.txt")
    mass = 24
    k = len(rt_inverted_CHNOPS)
    c = [0 for i in range(0, mass)]
    find_all(mass * b, k-1, c, sorted_masses_with_blowup_CHNOPS(b), rt_inverted_CHNOPS)

    time_end = datetime.datetime.utcnow()

    print "All computations successul in " + str(time_end - time_start)
