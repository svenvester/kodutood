nimi = input("Tere! Mis su nimi on? ")

print(f"Tere, {nimi}!")

elukoht = input("Kus sa elad? ")

if elukoht.lower() == "saaremaa":
    print("Oi, Saaremaa on kaunis saar!")

vanus = int(input("Kui vana sa oled? "))

if vanus < 18:
    print("Sa oled liiga noor, et autot juhtida.")
elif vanus == 18:
    print("Palju õnne! Sa oled nüüd täisealine!")
else:
    print("Sa võid autot juhtida.")
