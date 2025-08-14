with open("C:/Users/hp/Downloads/1a3n.pdb", "r") as pdb_file:
    for line in pdb_file:
        if line.startswith("REMARK 350 APPLY THE FOLLOWING TO CHAINS:"):
            chains =line[42:]
            print(chains)
            chain_id=str(input("enter chain id:"))
            if line.startswith("ATOM"):
                if line[21]==chain_id:
                    print(line.strip())





