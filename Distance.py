chain=input("enter chain ID: ")
aa1=input("enter amino acid residue 1: ")
aa2=input("enter amino acid residue 2: ")
with open("C:/Users/hp/Downloads/1a3n.pdb", "r") as pdb_file:
    for line in pdb_file:
        if line.startswith("ATOM"):
            if chain.upper()==line[21]:
                if line[13:15]=="CA":
                    import math
                    if line[17:20]==aa1.upper():
                        x1=line[32:38]
                        y1=line[40:46]
                        z1=line[48:54]
                        point1 = [x1, y1, z1]
                    if line[17:20]==aa2.upper():
                        x2=line[32:38]
                        y2=line[40:46]
                        z2=line[48:54]
                        point2 = [x2, y2, z2]
                    distance = math.dist(point1, point2)
                    print(distance)

