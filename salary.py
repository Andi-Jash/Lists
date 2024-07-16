salary = [340, 210 ,450, 600, 230, 500, 550, 300]
shumaEpagave = 0
for x in salary:
    shumaEpagave = shumaEpagave + x
print(f"Shuma e pagave eshte: {shumaEpagave}")

pagaMesatare = shumaEpagave / len(salary)
print(f"Paga mesatare eshte {pagaMesatare}")

pagaMin = salary[0]
for pagaAktuale in salary:
    if(pagaAktuale < pagaMin):
        pagaMin = pagaAktuale
print(f"Paga minimale eshte {pagaMin}")
    
pagaMax = salary[0]
for paga_aktuale in salary:
    if paga_aktuale > pagaMax:
        pagaMax = paga_aktuale
print(f"Paga maksimale eshte {pagaMax}")