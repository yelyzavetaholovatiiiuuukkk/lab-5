def oblicz_bmi(waga, wzrost):

    bmi = waga / (wzrost ** 2)
    return bmi

def zakres_bmi(bmi):
   
    if bmi < 18.5:
        print("Niedowaga")
    elif bmi < 25:
        print("Waga prawidłowa")
    elif bmi < 30:
        print("Nadwaga")
    else:
        print("Otyłość")

# Przykładowe użycie funkcji
waga = float(input("Podaj wagę (w kg): "))
wzrost = float(input("Podaj wzrost (w metrach): "))

bmi = oblicz_bmi(waga, wzrost)
print("Wskaźnik BMI wynosi:", bmi)
print("Zakres BMI to:")
zakres_bmi(bmi)