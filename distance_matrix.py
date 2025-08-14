import math
chain = input("Enter chain ID: ")
ca_coords = []
labels = []
with open("C:/Users/hp/Downloads/1a3n.pdb", "r") as pdb_file:
    for line in pdb_file:
        if line.startswith("ATOM") and line[21] == chain.upper() and line[13:15] == "CA":
            x = float(line[30:38])
            y = float(line[38:46])
            z = float(line[46:54])
            res = line[23:26].strip()
            ca_coords.append((x, y, z))
            labels.append(res)
n = len(ca_coords)
matrix = [[0.0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            matrix[i][j] = math.dist(ca_coords[i], ca_coords[j])
print("     ", end="")
for label in labels:
    print(f"{label:>5}", end="")
print()
for i in range(n):
    print(f"{labels[i]:>5}", end="")
    for j in range(n):
        print(f"{matrix[i][j]:5.1f}", end="")
    print()