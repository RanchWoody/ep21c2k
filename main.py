
try:
    file = open("valaszok.txt", "r")
    irando = open("pontok.txt", "w+")
except Exception:
    print("----------------------------------------------")
    print(("Hiba a fájl beolvasásakor!").center(40))
    print("----------------------------------------------")

temp = ""
adatok = [[""]]

elso = True

try:
    eredmenyek = file.readline()
except Exception:
    print("----------------------------------------------")
    print(("I/O Hiba!").center(40))
    print("----------------------------------------------")

try:
    for i in file:

        temp = i.split(" ")

        adatok.append(temp)

    print("1. feladat: Az adatok beolvasva!")
    print("")
except Exception:
    print("----------------------------------------------")
    print(("I/O Hiba!").center(40))
    print("----------------------------------------------")

##a versenyzők kiiratása ellenőrzés szempontjából
'''
for i in range(len(adatok)):
    if i > 0:
        print(f"A versenyző kódja: {adatok[i][0]} és eredménye {adatok[i][1]}")
'''

print("")
print(f"2. fealdat: A versenyen {len(adatok)-1} résztvevő indult.")
print("")

print("3. feladat: Kérem adja meg a versenyző azonosítóját: ")
bekert = input()
megfeleloBekertAdat = True
kilepes = False
versenyzoIndex = 1


for i in range(len(adatok)):
    if i > 0:
        if bekert == adatok[i][0]:
            print(adatok[i][1])
            print("")
            versenyzoIndex = i
            kilepes = True
            break
        else:
            megfeleloBekertAdat = False
    if kilepes:
        break

egyezes = []

if not(megfeleloBekertAdat):
    print("A megadott azonosító nem létezik!")
    print("")
    print("4. feladat: A helyes megoldás: ")
    print(eredmenyek)
    for i in range(len(eredmenyek)):
        if eredmenyek[i] == adatok[1][1][i]:
            egyezes.append("+")
        else:
            egyezes.append(" ")

    print(egyezes[0], egyezes[1], egyezes[2], egyezes[3], egyezes[4], egyezes[5], egyezes[6], egyezes[7], egyezes[8],
          egyezes[9], egyezes[10], egyezes[11], egyezes[12], egyezes[13])
else:
    print("4. A helyes megoldás: ")
    print(eredmenyek)
    for i in range(len(eredmenyek)):
        if eredmenyek[i] == adatok[versenyzoIndex][1][i]:
            egyezes.append("+")
        else:
            egyezes.append(" ")

    print(egyezes[0], egyezes[1], egyezes[2], egyezes[3], egyezes[4], egyezes[5], egyezes[6], egyezes[7], egyezes[8],
          egyezes[9], egyezes[10], egyezes[11], egyezes[12], egyezes[13])

print("5. feladat: Kérem adja meg a feladat sorszámát: ")
sorszam = input()
helyesValaszok = 0

for i in range(len(adatok)):
    if i > 0:
        if adatok[i][1][int(sorszam)-1] == eredmenyek[int(sorszam)-1]:
            helyesValaszok += 1

print(f"A feladatra {helyesValaszok} fő, a versenyzők {round(helyesValaszok/(len(adatok))*100, 2)}%-a adott helyes választ.")

print("6. feladat: A versenyzők pontszámának meghatározása.")

pontszamok = [[]]
asd = [" ", " "]
for i in range(len(adatok)):
    pontszamok.append(asd)

for i in range(len(adatok)):
    if i > 0:
        pontszamok[i][0] = adatok[i][0]

        pont = 0

        for j in range(len(eredmenyek)):
            if j <= 4:
                if adatok[i][1][j] == eredmenyek[j]:
                    pont += 3
            elif j > 4 and j <= 9:
                if adatok[i][1][j] == eredmenyek[j]:
                    pont += 4
            elif j > 9 and j <= 12:
                if adatok[i][1][j] == eredmenyek[j]:
                    pont += 5
            elif j == 14:
                if adatok[i][1][j] == eredmenyek[j]:
                    pont += 6

        pontszamok[i][1] = pont

try:
    for i in range(len(pontszamok)):
        irando.write(f"{pontszamok[i][0]} {pontszamok[i][1]}")
except Exception:
    print("----------------------------------------------")
    print(("Hiba a fájl írásakor!").center(40))
    print("----------------------------------------------")


##random tömb készítése a sorrendbe rakás bemutatására
sorrend = [["CG982", "11"], ["XC423", "33"], ["OP856", "12"], ["ER112", "51"], ["LK548", "44"], ]

tombTemp1 = 0
tombTemp2 = 0
vege = True


print("")
print("7. feladat: A verseny legjobbjai: ")

while(vege):
    if (sorrend[0][1] > sorrend[1][1]) and (sorrend[0][1] > sorrend[2][1]) and (sorrend[0][1] > sorrend[3][1]) and (sorrend[0][1] > sorrend[4][1]):
        for j in range(len(sorrend)):
            print(f"{j+1}. díj ({sorrend[j][1]} pont): {sorrend[j][0]}")
            vege = False

    else:
        for i in range(len(sorrend)-1):
            if sorrend[i][1] < sorrend[i+1][1]:
                tombTemp1 = sorrend[i][0]
                tombTemp2 = sorrend[i][1]
                sorrend[i][0] = sorrend[i+1][0]
                sorrend[i][1] = sorrend[i + 1][1]
                sorrend[i+1][0] = tombTemp1
                sorrend[i+1][1] = tombTemp2

file.close()
irando.close()