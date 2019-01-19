#Element Symbol and Atomic Weight:
elements = {
"none": 0,
"H": "Helium", "atomic_weight_H": 1.00784,
""

}
none = 0 #This is used for is there is no element to be placed in function input (for input type: list)
He	= 4.002602
Li	= 6.938
Be	= 9.0121831
B	= 10.806
C	= 12.0096
N	= 14.00643
O	= 15.99903
F	= 18.99840316
Ne	= 20.1797
Na	= 22.98976928
Mg	= 24.304
Al	= 26.9815385
Si	= 28.084
P	= 30.973762
S	= 32.059
Cl	= 35.446
Ar	= 39.948
K	= 39.0983
Ca	= 40.078
Sc	= 44.955908
Ti	= 47.867
V	= 50.9415
Cr	= 51.9961
Mn	= 54.938044
Fe	= 55.845
Co	= 58.933194
Ni	= 58.6934
Cu	= 63.546
Zn	= 65.38
Ga	= 69.723
Ge	= 72.63
As	= 74.921595
Se	= 78.971
Br	= 79.901
Kr	= 83.798
Rb	= 85.4678
Sr	= 87.62
Y	= 88.90594
Zr	= 91.224
Nb	= 92.90637
Mo	= 95.95
Tc	= 97
Ru	= 101.07
Rh	= 102.9055
Pd	= 106.42
Ag	= 107.8682
Cd	= 112.414
In	= 114.818
Sn	= 118.71
Sb	= 121.76
Te	= 127.6
I	= 126.90447
Xe	= 131.293
Cs	= 132.905452
Ba	= 137.327
La	= 138.90547
Ce	= 140.116
Pr	= 140.90766
Nd	= 144.242
Pm	= 145
Sm	= 150.36
Eu	= 151.964
Gd	= 157.25
Tb	= 158.92535
Dy	= 162.5
Ho	= 164.93033
Er	= 167.259
Tm	= 168.93422
Yb	= 173.045
Lu	= 174.9668
Hf	= 178.49
Ta	= 180.94788
W	= 183.84
Re	= 186.207
Os	= 190.23
Ir	= 192.217
Pt	= 195.084
Au	= 196.966569
Hg	= 200.592
Tl	= 204.382
Pb	= 207.2
Bi	= 208.9804
Po	= 209
At	= 210
Rn	= 222
Fr	= 223
Ra	= 226
Ac	= 227
Th	= 232.0377
Pa	= 231.03588
U	= 238.02891
Np	= 237
Pu	= 244
Am	= 243
Cm	= 247
Bk	= 247
Cf	= 251
Es	= 252
Fm	= 257
Md	= 258
No	= 259
Lr	= 262
Rf	= 263
Db	= 268
Sg	= 271
Bh	= 270
Hs	= 270
Mt	= 278
Ds	= 281
Rg	= 281
Cn	= 285
Uut	= 286
Fl	= 289
Uup	= 289
Lv	= 293
Uus	= 294
Uuo	= 294

def composition_of_compounds(element1,element2,element3):
    #Molar_Mass:
    if len(element1) == 2 and len(element2) == 2 and len(element3) == 2: #checking to make sure it is basic outline for compound
        molar_info_element1 = element1[0] * element1[1] #finding the molar mass of the fist element
        molar_info_element2 = element2[0] * element2[1] #finding the molar mass of the second element
        molar_info_element3 = element3[0] * element3[1] #finding the molar mass of the third element
        molar_mass = molar_info_element1 + molar_info_element2 + molar_info_element3 #adding up the molar mass of each element into the compound's molar mass
        #Percent Composition:
        percent_composition_element1 = (molar_info_element1 / molar_mass) * 100 #finding the percentage of the first element
        percent_composition_element2 = (molar_info_element2 / molar_mass) * 100 #finding the percentage of the second element
        percent_composition_element3 = (molar_info_element3 / molar_mass) * 100 #finding the percentage of the third element
        print("") #for easier output reading
        print("Molar Mass of Compound:") #letting you know in the output that the number below is the molar mass
        print(molar_mass) #printing the molar mass
        print("---------------------------") #for easier output reading
        print("Element 1's percent:") #letting you know in the output that the number below is the percentage of element 1 in the compound
        print(str(percent_composition_element1) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("Element 2's percent:") #letting you know in the output that the number below is the percentage of element 2 in the compound
        print(str(percent_composition_element2) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("Element 3's percent:") #letting you know in the output that the number below is the percentage of element 3 in the compound
        print(str(percent_composition_element3) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("") #for easier output reading
    elif len(element1) == 6 and len(element2) == 2 and len(element3) == 2: #checking to make sure it has element 1 be a multi-compound
        #Molar Mass:
        molar_info_element1 = (element1[0] * element1[1]) + (element1[2] * element1[3]) + (element1[4] + element1[5]) #finding the molar mass of the first element compound
        molar_info_element2 = element2[0] * element2[1] #finding the molar mass of the second element
        molar_info_element3 = element3[0] * element3[1] #finding the molar mass of the third element
        molar_mass = molar_info_element1 + molar_info_element2 + molar_info_element3 #adding up the molar mass of each element into the compound's molar mass
        #Percent Composition:
        percent_composition_element1 = (molar_info_element1 / molar_mass) * 100 #finding the percentage of the first element compound
        percent_composition_element2 = (molar_info_element2 / molar_mass) * 100 #finding the percentage of the second element
        percent_composition_element3 = (molar_info_element3 / molar_mass) * 100 #finding the percentage of the third element
        print("") #for easier output reading
        print("Molar Mass of Compound:") #letting you know in the output that the number below is the molar mass
        print(molar_mass) #printing the molar mass
        print("---------------------------") #for easier output reading
        print("Compound 1's percent:") #letting you know in the output that the number below is the percentage of element 1 in the compound
        print(str(percent_composition_element1) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("Element 2's percent:") #letting you know in the output that the number below is the percentage of element 2 in the compound
        print(str(percent_composition_element2) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("Element 3's percent:") #letting you know in the output that the number below is the percentage of element 3 in the compound
        print(str(percent_composition_element3) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("") #for easier output reading
    elif len(element1) == 2 and len(element2) == 6 and len(element3) == 2: #checking to make sure it has element 2 be a multi-compound
        #Molar Mass:
        molar_info_element1 = element1[0] * element1[1] #finding the molar mass of the fist element
        molar_info_element2 = (element2[0] * element2[1]) + (element2[2] * element2[3]) + (element2[4] + element2[5]) #finding the molar mass of the second element compound
        molar_info_element3 = element3[0] * element3[1] #finding the molar mass of the third element
        molar_mass = molar_info_element1 + molar_info_element2 + molar_info_element3 #adding up the molar mass of each element into the compound's molar mass
        #Percent Composition:
        percent_composition_element1 = (molar_info_element1 / molar_mass) * 100 #finding the percentage of the first element
        percent_composition_element2 = (molar_info_element2 / molar_mass) * 100 #finding the percentage of the second element compound
        percent_composition_element3 = (molar_info_element3 / molar_mass) * 100 #finding the percentage of the third element
        print("") #for easier output reading
        print("Molar Mass of Compound:") #letting you know in the output that the number below is the molar mass
        print(molar_mass) #printing the molar mass
        print("---------------------------") #for easier output reading
        print("Element 1's percent:") #letting you know in the output that the number below is the percentage of element 1 in the compound
        print(str(percent_composition_element1) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("Compound 2's percent:") #letting you know in the output that the number below is the percentage of element 2 in the compound
        print(str(percent_composition_element2) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("Element 3's percent:") #letting you know in the output that the number below is the percentage of element 3 in the compound
        print(str(percent_composition_element3) + "%") #printing the composition percentage of that element in the compound #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("") #for easier output reading
    elif len(element1) == 2 and len(element2) == 2 and len(element3) == 6: #checking to make sure it has element 3 be a multi-compound
        #Molar Mass:
        molar_info_element1 = element1[0] * element1[1] #finding the molar mass of the fist element
        molar_info_element2 = element2[0] * element2[1] #finding the molar mass of the second element
        molar_info_element3 = (element3[0] * element3[1]) + (element3[2] * element3[3]) + (element3[4] + element3[5]) #finding the molar mass of the third element compound
        #Percent Composition:
        percent_composition_element1 = (molar_info_element1 / molar_mass) * 100 #finding the percentage of the first element
        percent_composition_element2 = (molar_info_element2 / molar_mass) * 100 #finding the percentage of the second element
        percent_composition_element3 = (molar_info_element3 / molar_mass) * 100 #finding the percentage of the third element compound
        print("") #for easier output reading
        print("Molar Mass of Compound:") #letting you know in the output that the number below is the molar mass
        print(molar_mass) #printing the molar mass
        print("---------------------------") #for easier output reading
        print("Element 1's percent:") #letting you know in the output that the number below is the percentage of element 1 in the compound
        print(str(percent_composition_element1) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("Element 2's percent:") #letting you know in the output that the number below is the percentage of element 2 in the compound
        print(str(percent_composition_element2) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("Compound 3's percent:") #letting you know in the output that the number below is the percentage of element 3 in the compound
        print(str(percent_composition_element3) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("") #for easier output reading
    elif len(element1) == 7 and len(element2) == 2 and len(element3) == 2: #checking to make sure it has element 1 be a multi-compound being multiplied
        #Molar Mass:
        molar_info_element1 = ((element1[0] * element1[1]) + (element1[2] * element1[3]) + (element1[4] + element1[5])) * element1[6] #finding the molar mass of the first element that is a multicompound that is multiplied
        molar_info_element2 = element2[0] * element2[1] #finding the molar mass of the second element
        molar_info_element3 = element3[0] * element3[1]
        molar_mass = molar_info_element1 + molar_info_element2 + molar_info_element3 #adding up the molar mass of each element into the compound's molar mass
        #Percent Composition:
        percent_composition_element1 = (molar_info_element1 / molar_mass) * 100 #finding the percentage of the first element compound
        percent_composition_element2 = (molar_info_element2 / molar_mass) * 100 #finding the percentage of the second element
        percent_composition_element3 = (molar_info_element3 / molar_mass) * 100 #finding the percentage of the third element
        print("") #for easier output reading
        print("Molar Mass of Compound:") #letting you know in the output that the number below is the molar mass
        print(molar_mass) #printing the molar mass
        print("---------------------------") #for easier output reading
        print("Compound 1's (the multiplied) percent:") #letting you know in the output that the number below is the percentage of element 1 in the compound
        print(str(percent_composition_element1) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("Element 2's percent:") #letting you know in the output that the number below is the percentage of element 2 in the compound
        print(str(percent_composition_element2) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("Element 3's percent:") #letting you know in the output that the number below is the percentage of element 3 in the compound
        print(str(percent_composition_element3) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("") #for easier output reading
    elif len(element1) == 2 and len(element2) == 7 and len(element3) == 2: #checking to make sure it has element 2 be a multi-compound being multiplied
        #Molar Mass:
        molar_info_element1 = element1[0] * element1[1] #finding the molar mass of the fist element
        molar_info_element2 = ((element2[0] * element2[1]) + (element2[2] * element2[3]) + (element2[4] + element2[5])) * element2[6] #finding the molar mass of the second element that is a multicompound that is multiplied
        molar_info_element3 = element3[0] * element3[1]
        molar_mass = molar_info_element1 + molar_info_element2 + molar_info_element3 #adding up the molar mass of each element into the compound's molar mass
        #Percent Composition:
        percent_composition_element1 = (molar_info_element1 / molar_mass) * 100 #finding the percentage of the first element
        percent_composition_element2 = (molar_info_element2 / molar_mass) * 100 #finding the percentage of the second element compound
        percent_composition_element3 = (molar_info_element3 / molar_mass) * 100
        print("") #for easier output reading
        print("Molar Mass of Compound:") #letting you know in the output that the number below is the molar mass
        print(molar_mass) #printing the molar mass
        print("---------------------------") #for easier output reading
        print("Element 1's percent:") #letting you know in the output that the number below is the percentage of element 1 in the compound
        print(str(percent_composition_element1) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("Compound 2's (the multiplied) percent:") #letting you know in the output that the number below is the percentage of element 2 in the compound
        print(str(percent_composition_element2) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("Element 3's percent:") #letting you know in the output that the number below is the percentage of element 3 in the compound
        print(str(percent_composition_element3) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("") #for easier output reading
    elif len(element1) == 2 and len(element2) == 2 and len(element3) == 7: #checking to make sure it has element 3 be a multi-compound being multiplied
        #Molar Mass:
        molar_info_element1 = element1[0] * element1[1] #finding the molar mass of the fist element
        molar_info_element2 = element2[0] * element2[1] #finding the molar mass of the second element
        molar_info_element3 = ((element3[0] * element3[1]) + (element3[2] * element3[3]) + (element3[4] + element3[5])) * element3[7] #finding the molar mass of the third element that is a multicompound that is multiplied
        molar_mass = molar_info_element1 + molar_info_element2 + molar_info_element3 #adding up the molar mass of each element into the compound's molar mass
        #Percent Composition:
        percent_composition_element1 = (molar_info_element1 / molar_mass) * 100 #finding the percentage of the first element
        percent_composition_element2 = (molar_info_element2 / molar_mass) * 100 #finding the percentage of the second element
        percent_composition_element3 = (molar_info_element3 / molar_mass) * 100
        print("") #for easier output reading
        print("Molar Mass of Compound:") #letting you know in the output that the number below is the molar mass
        print(molar_mass) #printing the molar mass
        print("---------------------------") #for easier output reading
        print("Element 1's percent:") #letting you know in the output that the number below is the percentage of element 1 in the compound
        print(str(percent_composition_element1) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("Element 2's percent:") #letting you know in the output that the number below is the percentage of element 2 in the compound
        print(str(percent_composition_element2) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("Compound 3's (the multiplied) percent:") #letting you know in the output that the number below is the percentage of element 3 in the compound
        print(str(percent_composition_element3) + "%") #printing the composition percentage of that element in the compound
        print("---------------------------") #for easier output reading
        print("") #for easier output reading
    else: #checking if the function inputs are wrong
        print("There is a problem! Check your function inputs")

#Examples:
composition_of_compounds([Ag,1,Na,2,H,4],[F,1],[O,0])
composition_of_compounds([Ag,1,Na,2,H,4,2],[F,1],[O,0])
composition_of_compounds([Na,3],[P,1],[O,4])
