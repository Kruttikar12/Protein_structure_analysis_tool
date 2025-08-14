with open("C:/Users/hp/Downloads/1a3n.pdb", "r") as pdb_file:
    for line in pdb_file:
        if line.startswith("ATOM") or line.startswith("HETATM"):
            atom_serial = line[6:11].strip()
            atom_name = line[12:16].strip()
            residue_name = line[17:20].strip()
            chain_id = line[21].strip()
            residue_seq = line[22:26].strip()
            x = line[30:38].strip()
            y = line[38:46].strip()
            z = line[46:54].strip()
            print(f"Atom#: {atom_serial}, Atom: {atom_name}, Residue: {residue_name}, Chain: {chain_id}, Position: ({x}, {y}, {z})")