import datetime

print("Na podstawie numeru PESEL program wyznacza datę urodzenia, wiek oraz płeć osoby.")
numer_pesel = str(input("Podaj nr PESEL: "))
data_urodzenia = numer_pesel[0:6]
rok = numer_pesel[0:2]
if int(numer_pesel[2]) > 1:
    rok_urodzenia = '20'+rok
else:
    rok_urodzenia = '19'+rok
if int(numer_pesel[2]) > 1:
    cyfra_3 = int(numer_pesel[2]) - 2
    cyfra_4 = int(numer_pesel[3])
    miesiac_dokladny = str(cyfra_3) + str(cyfra_4)
else:
    miesiac_dokladny = (numer_pesel[2:4])

# Obliczanie wieku
aktualna_data = datetime.date.today()
data_urodzenia = datetime.datetime.strptime(rok_urodzenia + miesiac_dokladny + numer_pesel[4:6], "%Y%m%d").date()
wiek = aktualna_data.year - data_urodzenia.year - ((aktualna_data.month, aktualna_data.day) < (data_urodzenia.month, data_urodzenia.day))

plec_numer = int(numer_pesel[9])
if (plec_numer%2 == 0):
    plec = 'kobietą'
else:
    plec = 'mężczyzną'
print("Osoba, której Pesel to: ", numer_pesel, " urodziła się ", data_urodzenia.strftime("%d.%m.%Y"), ", ma ", wiek, " lat i jest ", plec, sep="")
