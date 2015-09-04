__author__ = 'Cristina'

elements = []
CHNOPS = []

C12 = {'mass': 12.00000000000, 'percent': 98.9300}
C13 = {'mass': 13.00335483780, 'percent': 1.0700}
C14 = {'mass': 14.00324198800, 'percent': 0.0000}
CARBON = {'name': "carbon", 'symbol' : "C", 'mass': 12.01070000000, 'valence': 4, 'freqisotope': C12, 'isotopes': [C12, C13, C14]}
CHNOPS.append(CARBON)

H1 = {'mass': 1.00782503214, 'percent': 99.9885}
H2 = {'mass': 2.01410177800, 'percent': 0.0115}
H3 = {'mass': 3.01604926750, 'percent': 0.0000}
HYDROGEN = {'name': "hydrogen", 'symbol': "H", 'mass': 1.00794000000, 'valence': 1, 'freqisotope': H1, 'isotopes': [H1, H2, H3]}
CHNOPS.append(HYDROGEN)

N14 = {'mass': 14.00307400524, 'percent': 99.6320}
N15 = {'mass': 15.00010889840, 'percent':  0.3680}
NITROGEN = {'name': "nitrogen", 'symbol': "N", 'mass': 14.00670000000, 'valence': 3, 'freqisotope': N14, 'isotopes': [N14, N15]}
CHNOPS.append(NITROGEN)

O16 = {'mass': 15.99491462210, 'percent': 99.7570}
O17 = {'mass': 16.99913150000, 'percent':  0.0380}
O18 = {'mass': 17.99916040000, 'percent':  0.2050}
OXYGEN = {'name': "oxygen", 'symbol': "O", 'mass': 15.99940000000, 'valence': 2, 'freqisotope': O16, 'isotopes': [O16, O17, O18]}
CHNOPS.append(OXYGEN)

P31 = {'mass': 30.97376151200, 'percent': 100.0000}
PHOSPHORUS = {'name': "phosphor", 'symbol': "P", 'mass': 30.97376149000, 'valence': 3, 'freqisotope': P31, 'isotopes': [P31]}
CHNOPS.append(PHOSPHORUS)


S32 = {'mass': 31.97207069000, 'percent': 94.9300}
S33 = {'mass': 32.97145850000, 'percent':  0.7600}
S34 = {'mass': 33.96786683000, 'percent':  4.2900}
S35 = {'mass': 34.96903214000, 'percent':  0.0000}
S36 = {'mass': 35.96708088000, 'percent':  0.0200}
SULFUR ={'name': "sulfur", 'symbol': "S", 'mass': 32.06533000000, 'valence': 2, 'freqisotope': S32, 'isotopes':[S32, S33, S34, S35, S36]}
CHNOPS.append(SULFUR)

elements.extend(CHNOPS)

Cl35 = {'mass': 34.96885271000, 'percent': 75.7800}
Cl36 = {'mass': 35.96830695000, 'percent':  0.0000}
Cl37 = {'mass': 36.96590260000, 'percent': 24.2200}
CHLORINE = {'name': "chlorine", 'symbol': "Cl", 'mass': 35.45273000000, 'valence': 1, 'freqisotope': Cl35, 'isotopes': [Cl35, Cl36, Cl37]}
elements.append(CHLORINE)

F19 = {'mass': 18.99840320500, 'percent': 100.0000}
FLUORINE = {'name': 'fluorine', 'symbol': "F", 'mass': 18.99840325000, 'valence': 1, 'freqisotope': F19, 'isotopes': [F19]}
elements.append(FLUORINE)

Na23 = {'mass': 22.989770, 'percent': 100.0000}
NATRIUM = {'name': 'natrium', 'symbol': "Na", 'mass': 22.989770, 'valence': 1, 'freqisotope': Na23, 'isotopes': [Na23]}
elements.append(NATRIUM)

Br79 = {'mass': 78.9183376, 'percent': 50.69}
Br81 = {'mass': 80.9162910, 'percent': 49.31}
BROMINE = {'name': 'bromine', 'symbol': "Br", 'mass': 79.904, 'valence': 0, 'freqisotope': Br79, 'isotopes': [Br79, Br81]}
elements.append(BROMINE)

I127 ={'mass': 126.904468, 'percent': 100.0000}
IODINE = {'name': 'iodine', 'symbol': "I", 'mas': 126.90447, 'valence': 0, 'freqisotope': I127, 'isotopes': [I127]}
elements.append(IODINE)
