#Kirjuta programm, mis ütleb, kas kasutaja poolt etteantud täisarv on paarisarv või mitte. (paarisarvu mõiste - odd/even)

# Küsi kasutajalt täisarvu
arv = int(input("Sisesta täisarv: "))

# Kontrolli, kas arv on paarisarv
if arv % 2 == 0:
    print("Number on paarisarv.")
else:
    print("Number on paaritu arv.")
