# Calculate the mass of a protein based on the sequence.
# Masses derived from the monoisotopic mass table.
# Mass table represented by dictionary.

amino_acid_mass = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333}

# This loop iterates over the sequence, finds the mass in the dictionary and sums the masses.

with open('aa_seq.txt') as f:
    for line in f:
        n = 0
        for char in line:
            if char == "\n":
                pass
            else:
                n += amino_acid_mass[char]
    print(round(n, 3))
