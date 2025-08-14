def extract_drug():
    hetero_atoms=set()
    with open("C:/Users/hp/Downloads/1a3n.pdb","r") as pdb_file:
        for line in pdb_file:
            if line.startswith("HETATM"):
                atom_name=line[17:20].strip()
                if atom_name not in ("HOH", "H2O"):
                    hetero_atoms.add(atom_name)
    print("Hetero Atoms:",hetero_atoms)
    drug=input("Enter a drug: ").strip().upper()
    output_file=f"C:/Users/hp/Downloads/extracted_drug_{drug}.pdb"
    with open("C:/Users/hp/Downloads/1a3n.pdb","r") as pdb_file,open(output_file,"w") as out_file:
        for line in pdb_file:
            if line.startswith("HETATM"):
                drug_name=line[17:20].strip()
                if drug_name == drug and drug_name not in ("HOH", "H2O"):
                    out_file.write(line)
                    print(line.strip())
    print(f"Extracted drug '{drug}' saved to:\n{output_file}")
extract_drug()