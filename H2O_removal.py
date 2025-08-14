def remove_h2o():
    output_file="C:/Users/hp/Downloads/without_HOH.pdb"
    with open("C:/Users/hp/Downloads/1a3n.pdb","r") as pdb_file,open(output_file,"w") as out_file:
        for line in pdb_file:
            if line.startswith("HETATM"):
                hetatm=line[17:20].strip()
                if hetatm!="HOH":
                    out_file.write(line)
                    print(line.strip())
            else:
                out_file.write(line)
                print(line.strip())
    print(f"File without h2o atoms saved to:\n{output_file}")
remove_h2o()