
import math
chain = input("Enter chain ID: ").strip().upper()
res1 = int(input("Enter residue number 1: "))
res2 = int(input("Enter residue number 2: "))
point1 = None
point2 = None
with open("C:/Users/hp/Downloads/1a3n.pdb", "r") as pdb_file:
    for line in pdb_file:
        if line.startswith("ATOM"):
            if line[21].upper() == chain and line[12:16].strip() == "CA":
                residue = line[22:26].strip()
                if not residue.isdigit():
                    continue
                res_num = int(residue)
                x = float(line[30:38])
                y = float(line[38:46])
                z = float(line[46:54])
                if res_num == res1:
                    point1 = (x, y, z)
                elif res_num == res2:
                    point2 = (x, y, z)
if point1 is None:
    print(f"Residue number {res1} not found in chain {chain}.")
elif point2 is None:
    print(f"Residue number {res2} not found in chain {chain}.")
else:
    distance = math.dist(point1, point2)
    print(f"Distance between {res1} and {res2} in chain {chain} is: {distance:.2f} Å")