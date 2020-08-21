D = int(input())
N = int(input())
coords = []
perimeter = 0
vazute = []
for _ in range(N):
    coord = list(map(int,input().split(",")))
    coords.append(tuple(coord))
d = int(input())
perimeter = 4 * N * d
for (i,j) in coords:
    if (i+1,j) in coords:
        perimeter -= d
    if (i,j+1) in coords:
        perimeter -= d
    if (i-1,j) in coords:
        perimeter -= d
    if (i,j-1) in coords:
        perimeter -= d
print(perimeter)