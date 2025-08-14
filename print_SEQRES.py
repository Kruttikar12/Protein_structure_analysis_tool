with open("C:/Users/hp/Downloads/1a3n.pdb", "r") as pdb_file:
    for line in pdb_file:
        if line.startswith("SEQRES"):
            chain_id=line[11].strip()
            residue_num=line[13:17].strip()
            residue_name=line[19:70]
            print(f" Chain: {chain_id}, Residue No: {residue_num}, Residue: {residue_name}")