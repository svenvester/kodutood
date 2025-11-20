# Küsi kasutajalt nimi
nimi = input("Tere! Mis su nimi on? ")

# Tervita kasutajat nimepidi
print(f"Tere, {nimi}!")

# Küsi kasutajalt elukohta
elukoht = input("Kus sa elad? ")

# Kui elukoht on Saaremaa, väljastame kommentaari
if elukoht.lower() == "saaremaa":
    print("Oi, Saaremaa on kaunis saar!")

# Küsi kasutajalt vanust
vanus = int(input("Kui vana sa oled? "))

# Kontrollime vanuse põhjal sõnumit
if vanus < 18:
    print("Sa oled liiga noor, et autot juhtida.")
elif vanus == 18:
    print("Palju õnne! Sa oled nüüd täisealine!")
else:
    print("Sa võid autot juhtida.")
