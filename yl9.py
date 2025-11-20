#Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, võrdhaarseteks ja võrdkülgseteks. 
#Kirjutada programm, mis küsib kasutajalt kolme külje pikkused ning väljastab vastusena kolmnurga liigi. 
#Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab üldse eksisteerida. 
#Külje pikkused ei pea olema täisarvud. (ujukomaarv - float)


a = float(input("Sisesta esimese külje pikkus: "))
b = float(input("Sisesta teise külje pikkus: "))
c = float(input("Sisesta kolmanda külje pikkus: "))


if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("See on võrdkülgne kolmnurk.")
    elif a == b or a == c or b == c:
        print("See on võrdhaarne kolmnurk.")
    else:
        print("See on erikülgne kolmnurk.")
else:
    print("Sellist kolmnurka ei saa olemas olla.")


