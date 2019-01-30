#  Element Symbol and Atomic Weight:
elements = {
    "none": {"name": "None", "atomic_weight": 0},
    "H":  {"name": "Hydrogen", "atomic_weight": 1.00784},
    "He": {"name": "Helium", "atomic_weight": 4.002602},
    "Li": {"name": "Lithium", "atomic_weight": 6.938},
    "Be": {"name": "Beryllium", "atomic_weight": 9.0121831},
    "C":  {"name": "Carbon", "atomic_weight": 12.0096},
    "O":  {"name": "Oxygen", "atomic_weight": 15.99903},
    "N":  {"name": "Nitrogen", "atomic_weight": 14.00643},
    "F":  {"name": "Fluorine", "atomic_weight": 18.99840316},
    "Ne": {"name": "Neon", "atomic_weight": 20.1797},
    "Na": {"name": "Sodium", "atomic_weight": 22.98976928},
    "Mg": {"name": "Magnesium", "atomic_weight": 24.304},
    "Al": {"name": "Aluminium", "atomic_weight": 26.9815385},
    "Si": {"name": "Silicon", "atomic_weight": 28.084},
    "P":  {"name": "Phosphorus", "atomic_weight": 30.973762},
    "S":  {"name": "Sulfur", "atomic_weight": 32.059},
    "Cl": {"name": "Chlorine", "atomic_weight": 35.446},
    "Ar": {"name": "Argon", "atomic_weight": 39.948},
    "K":  {"name": "Potassium", "atomic_weight": 39.0983},
    "Ca": {"name": "Calcium", "atomic_weight": 40.078},
    "Sc": {"name": "Scandium", "atomic_weight": 44.955908},
    "Ti": {"name": "Titanium", "atomic_weight": 47.867},
    "V":  {"name": "Vanadium", "atomic_weight": 50.9415},
    "Cr": {"name": "Chromium", "atomic_weight": 51.9961},
    "Mn": {"name": "Manganese", "atomic_weight": 54.938044},
    "Fe": {"name": "Iron", "atomic_weight": 55.845},
    "Co": {"name": "Cobalt", "atomic_weight": 58.933194},
    "Ni": {"name": "Nickel", "atomic_weight": 58.6934},
    "Cu": {"name": "Copper", "atomic_weight": 63.546},
    "Zn": {"name": "Zinc", "atomic_weight": 65.38},
    "Ga": {"name": "Gallium", "atomic_weight": 69.723},
    "Ge": {"name": "Germanium", "atomic_weight": 72.63},
    "As": {"name": "Arsenic", "atomic_weight": 74.921595},
    "Se": {"name": "Selenium", "atomic_weight": 78.971},
    "Br": {"name": "Bromine", "atomic_weight": 79.901},
    "Kr": {"name": "Krypton", "atomic_weight": 83.798},
    "Rb": {"name": "Rubidium", "atomic_weight": 85.4678},
    "Sr": {"name": "Strontium", "atomic_weight": 87.62},
    "Y":  {"name": "Yttrium", "atomic_weight": 88.90594},
    "Zr": {"name": "Zirconium", "atomic_weight": 91.224},
    "Nb": {"name": "Niobium", "atomic_weight": 92.90637},
    "Mo": {"name": "Molybdenum", "atomic_weight": 95.95},
    "Tc": {"name": "Technetium", "atomic_weight": 97},
    "Ru": {"name": "Ruthenium", "atomic_weight": 101.07},
    "Rh": {"name": "Rhodium", "atomic_weight": 102.9055},
    "Pd": {"name": "Palladium", "atomic_weight": 106.42},
    "Ag": {"name": "Silver", "atomic_weight": 107.8682},
    "Cd": {"name": "Cadmium", "atomic_weight": 107.8682},
    "In": {"name": "Indium", "atomic_weight": 114.818},
    "Sn": {"name": "Tin", "atomic_weight": 118.71},
    "Sb": {"name": "Antimony", "atomic_weight": 121.76},
    "Te": {"name": "Tellurium", "atomic_weight": 127.6},
    "I":  {"name": "Iodine", "atomic_weight": 126.90447},
    "Xe": {"name": "Xenon", "atomic_weight": 131.293},
    "Cs": {"name": "Caesium", "atomic_weight": 132.905452},
    "Ba": {"name": "Barium", "atomic_weight": 137.327},
    "La": {"name": "Lanthanum", "atomic_weight": 138.90547},
    "Ce": {"name": "Cerium", "atomic_weight": 140.116},
    "Pr": {"name": "Praseodymium", "atomic_weight": 140.90766},
    "Nd": {"name": "Neodymium", "atomic_weight": 144.242},
    "Pm": {"name": "Promethium", "atomic_weight": 145},
    "Sm": {"name": "Samarium", "atomic_weight": 150.36},
    "Eu": {"name": "Europium", "atomic_weight": 151.964},
    "Gd": {"name": "Gadolinium", "atomic_weight": 157.25},
    "Tb": {"name": "Terbium", "atomic_weight": 158.92535},
    "Dy": {"name": "Dysprosium", "atomic_weight": 162.5},
    "Ho": {"name": "Holmium", "atomic_weight": 164.93033},
    "Er": {"name": "Erbium", "atomic_weight": 167.259},
    "Tm": {"name": "Thulium", "atomic_weight": 168.93422},
    "Yb": {"name": "Ytterbium", "atomic_weight": 173.045},
    "Lu": {"name": "Lutetium", "atomic_weight": 174.9668},
    "Hf": {"name": "Hafnium", "atomic_weight": 178.49},
    "Ta": {"name": "Tantalum", "atomic_weight": 180.94788},
    "W":  {"name": "Tungsten", "atomic_weigh": 183.84},
    "Re": {"name": "Rhenium", "atomic_weight": 186.207},
    "Os": {"name": "Osmium", "atomic_weight": 190.23},
    "Ir": {"name": "Iridium", "atomic_weight": 192.217},
    "Pt": {"name": "Platinum", "atomic_weight": 195.084},
    "Au": {"name": "Gold", "atomic_weight": 196.966569},
    "Hg": {"name": "Mercury", "atomic_weight": 200.592},
    "Tl": {"name": "Thalium", "atomic_weight": 204.382},
    "Pb": {"name": "Lead", "atomic_weight": 207.2},
    "Bi": {"name": "Bismuth", "atomic_weight": 208.9804},
    "Po": {"name": "Polonium", "atomic_weight": 209},
    "At": {"name": "Astatine", "atomic_weight": 210},
    "Rn": {"name": "Radon", "atomic_weight": 222},
    "Fr": {"name": "Francium", "atomic_weight": 223},
    "Ra": {"name": "Radium", "atomic_weight": 226},
    "Ac": {"name": "Actinium", "atomic_weight": 227},
    "Th": {"name": "Thorium", "atomic_weight": 232.0377},
    "Pa": {"name": "Protactinium", "atomic_weight": 231.03588},
    "U":  {"name": "Uranium", "atomic_weight": 238.02891},
    "Np": {"name": "Neptunium", "atomic_weight": 237},
    "Pu": {"name": "Plutonium", "atomic_weight": 244},
    "Am": {"name": "Americium", "atomic_weight": 243},
    "Cm": {"name": "Curium", "atomic_weight": 247},
    "Bk": {"name": "Berkelium", "atomic_weight": 247},
    "Cf": {"name": "Californium", "atomic_weight": 251},
    "Es": {"name": "Einsteinium", "atomic_weight": 252},
    "Fm": {"name": "Fermium", "atomic_weight_": 257},
    "Md": {"name": "Mendelevium", "atomic_weight": 258},
    "No": {"name": "Nobelium", "atomic_weight": 259},
    "Lr": {"name": "Lawrencium", "atomic_weight": 262},
    "Rf": {"name": "Rutherfordium", "atomic_weight": 263},
    "Db": {"name": "Dubnium", "atomic_weight": 268},
    "Sg": {"name": "Seaborgium", "atomic_weight": 271},
    "Bh": {"name": "Bohrium", "atomic_weight": 270},
    "Hs": {"name": "Hassium", "atomic_weight": 270},
    "Mt": {"name": "Meitnerium", "atomic_weight": 278},
    "Ds": {"name": "Darmstadtium", "atomic_weight": 281},
    "Rg": {"name": "Roentgenium", "atomic_weight": 281},
    "Cn": {"name": "Copernicium", "atomic_weight": 285},
    "Nh": {"name": "Nihonium", "atomic_weight": 286},
    "Fl": {"name": "Flerovium", "atomic_weight": 289},
    "Mc": {"name": "Moscovium", "atomic_weight": 289},
    "Lv": {"name": "Livermorium", "atomic_weight": 293},
    "Ts": {"name": "Tennessine", "atomic_weight": 294},
    "Og": {"name": "Organesson", "atomic_weight": 294},
}


def composition_of_compounds(element1,element2,element3):
    # Molar Mass Calculations:
    print(element1[0])
    print(elements[element1[0]])
    molar_info_element1 = elements[element1[0]]['atomic_weight'] * element1[1]
    molar_info_element2 = elements[element2[0]]['atomic_weight'] * element2[1]
    molar_info_element3 = elements[element3[0]]['atomic_weight'] * element3[1]
    molar_mass = molar_info_element1 + molar_info_element2 + molar_info_element3
    # Percent Composition Calculations:
    percent_composition_element1 = (molar_info_element1 / molar_mass) * 100
    percent_composition_element2 = (molar_info_element1 / molar_mass) * 100
    percent_composition_element3 = (molar_info_element1 / molar_mass) * 100
    # Print_Statements:
    print("")
    print("Molar Mass of compound:")
    print(molar_mass)
    print("---------------------------")
    print(elements[element1[0]]['name'] + "'s percent:")
    print(str(percent_composition_element1) + "%")
    print("---------------------------")
    print(elements[element2[0]]['name'] + "'s percent:")
    print(str(percent_composition_element2) + "%")
    print("---------------------------")
    print(elements[element3[0]]['name'] + "'s percent:")
    print(str(percent_composition_element3) + "%")
    print("---------------------------")
    print("")


composition_of_compounds(["Au", 6], ["C", 3], ["Eu", 5])