__author__ = 'Cristina'
import datetime

def parse_rt(filein):
    with open(filein, 'r') as f:
        data_in = f.read()
    f.close()
    rows = data_in.splitlines()
    # set the same blowup factor
    b = rows[0].split()[1]

    parsed_rows = []
    for row in rows[1:]:
        row = row.split('[')[1].split(']')[0].split(',')
        print row
        parsed_rows.append([int(item) for item in row])
    return parsed_rows

if __name__ == '__main__':

    time_start = datetime.datetime.utcnow()

    rt_inverted_testing = parse_rt("rt_testing.txt")
    rt_inverted = parse_rt("rt.txt")
    rt_inverted_CHNOPS = parse_rt("rt_CHNOPS.txt")

    print rt_inverted_testing

    time_end = datetime.datetime.utcnow()

    print "All computations successul in " + str(time_end - time_start)
