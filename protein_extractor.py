def extract_protein():
    output_file = "C:/Users/hp/Downloads/extracted_protein.pdb"
    with open("C:/Users/hp/Downloads/1a3n.pdb", "r") as pdb_file, open(output_file, "w") as out_file:
        for line in pdb_file:
            if line.startswith("ATOM"):
                out_file.write(line)
                print(line.strip())
    print(f"Extracted protein saved to:\n{output_file}")
extract_protein()