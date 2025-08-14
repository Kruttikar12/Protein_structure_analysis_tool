import math
def residues_within_cutoff():
    chain=input("Enter chain ID: ").strip().upper()
    residue_number=input("Enter residue number: ").strip()
    cutoff_distance=float(input("Enter cutoff distance: "))
    ca_atoms={}
    with open("C:/Users/hp/Downloads/1a3n.pdb","r") as pdb_file:
        for line in pdb_file:
            if line.startswith("ATOM") and line[21].upper()==chain and line[12:16].strip()=="CA":
                res_num=line[22:26].strip()
                x=float(line[30:38])
                y=float(line[38:46])
                z=float(line[46:54])
                ca_atoms[res_num]=(x,y,z)
    if residue_number not in ca_atoms:
        print(f"Residue {residue_number} not found in chain {chain}.")
    else:
        ref_coord=ca_atoms[residue_number]
        print(f"Residues in chain {chain} within {cutoff_distance} Å of residue {residue_number}:")
        for res_num,coord in ca_atoms.items():
            if res_num==residue_number:
                continue
            distance=math.dist(ref_coord,coord)
            if distance<=cutoff_distance:
                print(f"Residue {res_num} at distance {distance:.2f} Å")
residues_within_cutoff()