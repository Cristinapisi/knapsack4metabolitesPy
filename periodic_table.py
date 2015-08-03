__author__ = 'Cristina'

elements = []
CHNOPS = []

C12 = {'mass': 12.00000000000, 'percent': 98.9300}
C13 = {'mass': 13.00335483780, 'percent': 1.0700}
C14 = {'mass': 14.00324198800, 'percent': 0.0000}
CARBON = {'name': "carbon", 'symbol' : "C", 'mass': 12.01070000000, 'freqisotope': C12, 'isotopes': [C12, C13, C14]}
CHNOPS.append(CARBON)

H1 = {'mass': 1.00782503214, 'percent': 99.9885}
H2 = {'mass': 2.01410177800, 'percent': 0.0115}
H3 = {'mass': 3.01604926750, 'percent': 0.0000}
HYDROGEN = {'name': "hydrogen", 'symbol': "H", 'mass': 1.00794000000, 'freqisotope': H1, 'isotopes': [H1, H2, H3]}
CHNOPS.append(HYDROGEN)

N14 = {'mass': 14.00307400524, 'percent': 99.6320}
N15 = {'mass': 15.00010889840, 'percent':  0.3680}
NITROGEN = {'name': "nitrogen", 'symbol': "N", 'mass': 14.00670000000, 'freqisotope': N14, 'isotopes': [N14, N15]}
CHNOPS.append(NITROGEN)

O16 = {'mass': 15.99491462210, 'percent': 99.7570}
O17 = {'mass': 16.99913150000, 'percent':  0.0380}
O18 = {'mass': 17.99916040000, 'percent':  0.2050}
OXYGEN = {'name': "oxygen", 'symbol': "O", 'mass': 15.99940000000, 'freqisotope': O16, 'isotopes': [O16, O17, O18]}
CHNOPS.append(OXYGEN)

P31 = {'mass': 30.97376151200, 'percent': 100.0000}
PHOSPHORUS = {'name': "phosphor", 'symbol': "P", 'mass': 30.97376149000, 'freqisotope': P31, 'isotopes': [P31]}
CHNOPS.append(PHOSPHORUS)


S32 = {'mass': 31.97207069000, 'percent': 94.9300}
S33 = {'mass': 32.97145850000, 'percent':  0.7600}
S34 = {'mass': 33.96786683000, 'percent':  4.2900}
S35 = {'mass': 34.96903214000, 'percent':  0.0000}
S36 = {'mass': 35.96708088000, 'percent':  0.0200}
SULFUR ={'name': "sulfur", 'symbol': "S", 'mass': 32.06533000000, 'freqisotope': S32, 'isotopes':[S32, S33, S34, S35, S36]}
CHNOPS.append(SULFUR)

elements.extend(CHNOPS)