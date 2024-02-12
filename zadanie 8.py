def potega(a, n):
   
    # Warunek zakończenia rekurencji - gdy wykładnik jest równy 0
    if n == 0:
        return 1
    # Warunek zakończenia rekurencji - gdy wykładnik jest równy 1
    elif n == 1:
        return a
    # Warunek rekurencyjny
    else:
        return a * potega(a, n - 1)

# Przykładowe użycie funkcji
a = float(input("Podaj liczbę a: "))
n = int(input("Podaj wykładnik potęgi n: "))

wynik = potega(a, n)
print(f"{a} do potęgi {n} wynosi: {wynik}")