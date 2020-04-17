#taxi_id;  indulas;           idotartam;   tavolsag;  viteldij;   borravalo;   fizetes_modja
#0         1                  2            3          4           5            6
#5240;     2016.12.15 23:45;  900;         2,5;       10,75;      2,45;        bankkártya

#beolvasás
with open("fuvar.csv", 'r', encoding='UTF-8-sig') as f:
    fejlec = f.readline()
    matrix = [sor.replace(",",".").strip().split(';') for sor in f]

#3. feladat
print(f' 3. feladat: {len(matrix)} fuvar')

#4. feladat
bevetelek = 0
fuvar = 0
for sor in matrix:
    if sor[0]  == "6185":
        fuvar += 1
        viteldij  =  float(sor[4])
        borravalo =  float(sor[5])
        bevetelek =  bevetelek + viteldij + borravalo
print(f' 4. feladat: {fuvar} fuvar alatt {bevetelek} $')

#5. feladat
fiz_mod = []
for sor in matrix:
    fiz_mod.append(sor[6])

fiz_mod_halmaz = set(fiz_mod)
for i in fiz_mod_halmaz:
    darab = fiz_mod.count(i)
    print(i, darab)
    
#6.feladat
merfold = 0
for sor in matrix:
    merfold += float(sor[3])
print(f'6. feladat: {merfold*1.6:.2f}') #Csak Riconak: a :.2f az azért jó, mert a tizedespont után 2 tizedesig számol

#7. feladat
legnagyobb = 0
adatok = []
for sor in matrix:
    if int(sor[2]) > legnagyobb:
        legnagyobb = int(sor[2])
        adatok = sor
print(adatok)

#8. feladat
with open("hibak.txt", 'w', encoding='UTF-8') as f:
    f.write(fejlec)
    for r in matrix:
        tav = float(r[3])   == 0
        ido = float(r[2])   == 0
        vitel = float(r[4]) == 0
        if tav and not ido and not vitel:
            sor = f"{r[2]};{r[3]};{r[4]};{r[5]};{r[6]}".replace(".",",")
            print(f"{r[0]};{r[1]};{sor}")
            

            
        
            

