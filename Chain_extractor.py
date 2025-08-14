def extract_chain():
    with open("C:/Users/hp/Downloads/1a3n.pdb","r") as pdb_file:
        for line in pdb_file:
            if line.startswith("REMARK 350 APPLY THE FOLLOWING TO CHAINS:"):
                chains=line[42:]
                print("Chains:",chains)
    chain_id=input("Enter the chain ID: ")
    output_file=f"C:/Users/hp/Downloads/extracted_chain_{chain_id}.pdb"
    with open("C:/Users/hp/Downloads/1a3n.pdb","r") as pdb_file,open(output_file,"w") as out_file:
        for line in pdb_file:
            if line.startswith("ATOM"):
                if line[21]==chain_id:
                    out_file.write(line)
                    print(line.strip())
    print(f"Extracted chain {chain_id} saved to:\n{output_file}")
extract_chain()