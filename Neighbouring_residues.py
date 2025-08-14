import math
pdb_file = "C:/Users/hp/Downloads/1a3n.pdb"
chain1 = input("Enter first chain ID: ").strip().upper()
chain2 = input("Enter second chain ID: ").strip().upper()
residue_number = input("Enter residue number from first chain: ").strip()
chain1_atoms = {}
chain2_atoms = {}
with open(pdb_file, 'r') as file:
    for line in file:
        if line.startswith("ATOM") and line[12:16].strip() == "CA":
            chain = line[21].upper()
            res_num = line[22:26].strip()
            x = float(line[30:38])
            y = float(line[38:46])
            z = float(line[46:54])
            coord = (x, y, z)
            if chain == chain1:
                chain1_atoms[res_num] = coord
            elif chain == chain2:
                chain2_atoms[res_num] = coord
if residue_number not in chain1_atoms:
    print(f"Residue {residue_number} not found in chain {chain1}.")
else:
    ref_coord = chain1_atoms[residue_number]
    for res_num, coord in sorted(chain2_atoms.items(), key=lambda x: int(x[0])):
        distance = math.dist(ref_coord, coord)
        print(f"Residue {res_num} is at distance {distance:.2f}Å from Residue {residue_number}")