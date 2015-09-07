# all valid ones taken from https://metlin.scripps.edu/metabo_advanced.php
# no non-CHNOPS metabolites found there
# however, this script can accommodate non-CHNOPS formula for which elements that are in the periodic_table can be parsed
import os
import random
from periodic_table import *

metabolites_CHNOPS = [
    ("carbon dioxide", "C1 O2"),
    ("ethylene", "C2 H4"),
    ("glycerol", "C3 H8 O3"),
    ("L-Glutamate", "C5 H9 N1 O4"),
    ("aspartic acid", "C4 H7 N1 O4"),
    ("L-tryptophan", "C11 H12 N2 O2"),
    ("sucrose", "C12 H22 O11"),
    ("virodhamine", "C22 H37 N1 O2"),
    ("nefopam", "C17 H19 N1 O1"),
    ("sotalol", "C12 H20 N2 O3 S1"),
    ("campesterol", "C28 H48 O1"),
    ("folic acid", "C19 H19 N7 O6"),
    ("doxycicline", "C22 H24 N2 O8"),
    ("riboflavin (vit B2)", "C17 H20 N4 O6"),
    ("caffeine", "C8 H10 N4 O2"),
    ("ceroplastic acid", "C35 H70 O2"),
    ("glycogen", "C24 H42 O21"),
    ("primflasine", "C31 H36 O19"),
    ("tricrocin", "C38 H54 O12"),
    ("nystatin A1", "C47 H75 N1 O17"),
    ("pyoverdine I", "C55 H83 N17 O22"),
    ("lacto-n-hexaose", "C40 H68 N2 O31"),
    ("gentiodelphin", "C51 H52 O28"),
    ("acemannan", "C66 H100 N1 O49"),
    ("leoprolide", "C59 H84 N16 O12"),
    ("null", "H100"),
    ("null", "H1 C2"),
    ("null", "C24 H1 O21"),
    ("null", "C24 H42 O22"),
    ("null", "H4 C20 S7 N22 P10"),
    ("null", "H4 C20 S14 N40")
]

metabolites_non_CHNOPS = [
    ("amiloride", "C6 H8 Cl N7O"),
]


def get_element_mass(element):
    """
    :param element: an element object (e.g. CARBON)
    :return: the mass of the most frequent isotope
    """
    return element['freqisotope']['mass']


def parse_atom(atom):
    if atom[0] == 'C':
        element_mass = get_element_mass(CARBON)
        number = int(atom[1:])
    elif atom[0] == 'H':
        element_mass = get_element_mass(HYDROGEN)
        number = int(atom[1:])
    elif atom[0] == 'N':
        element_mass = get_element_mass(NITROGEN)
        number = int(atom[1:])
    elif atom[0] == 'O':
        element_mass = get_element_mass(OXYGEN)
        number = int(atom[1:])
    elif atom[0] == 'P':
        element_mass = get_element_mass(PHOSPHORUS)
        number = int(atom[1:])
    elif atom[0] == 'S':
        element_mass = get_element_mass(SULFUR)
        number = int(atom[1:])
    elif atom[0] == 'Cl':
        element_mass = get_element_mass(CHLORINE)
        number = int(atom[1:])
    elif atom[0] == 'F':
        element_mass = get_element_mass(FLUORINE)
        number = int(atom[1:])
    elif atom[0] == 'Na':
        element_mass = get_element_mass(NATRIUM)
        number = int(atom[1:])
    elif atom[0] == 'Br':
        element_mass = get_element_mass(BROMINE)
        number = int(atom[1:])
    elif atom[0] == 'I':
        element_mass = get_element_mass(IODINE)
        number = int(atom[1:])
    else:
        element_mass = 0
        number = 0
    return element_mass, number


def generate_data(metabolites):
    data = []
    for (name, metabolite) in metabolites:
        mass = 0
        atoms = metabolite.split(' ')
        for atom in atoms:
            (element_mass, number) = parse_atom(atom)
            mass += element_mass * number
        data.append(mass)
    return data


if __name__ == '__main__':
    masses = generate_data(metabolites_CHNOPS)
    small = open(os.path.join("input_files", "Small.txt"), 'w')
    medium = open(os.path.join("input_files", "Medium.txt"), 'w')
    large = open(os.path.join("input_files", "Large.txt"), 'w')
    for mass in masses:
        if mass < 500:
            small.write(str(mass) + ", " + str(random.randint(0, 20)) + '\n')
        elif mass < 1000:
            medium.write(str(mass) + ", " + str(random.randint(0, 20)) + '\n')
        else:
            large.write(str(mass) + ", " + str(random.randint(0, 20)) + '\n')
    small.close()
    medium.close()
    large.close()

