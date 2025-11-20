# Küsi kasutajalt kolm arvu
a = float(input("Sisesta esimene arv: "))
b = float(input("Sisesta teine arv: "))
c = float(input("Sisesta kolmas arv: "))

# Leia maksimum loogikatehete abil
if (a >= b) and (a >= c):
    maksimum = a
elif (b >= a) and (b >= c):
    maksimum = b
else:
    maksimum = c

print("Maksimum on:", maksimum)
