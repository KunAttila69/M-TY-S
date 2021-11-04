from typing import SupportsRound


f = open("alaprajz.txt", "r")
sorok = f.readlines()
f.close()
adatok = sorok[0].split()

for sor_cik in range(1,int(adatok[0])+1):
    sorok[sor_cik] = sorok[sor_cik][:int(adatok[1])]
    print(sorok[sor_cik])