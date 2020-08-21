#CENZURA
propozitie = input()
n = int(input())
nepermise = input().split()
for i in nepermise:
    propozitie = propozitie.replace(i, "*" * len(i))
print(propozitie)
