def fibonacci(n):

    # Warunek zakończenia rekurencji
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Warunek rekurencyjny
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Przykładowe użycie funkcji
n = int(input("Podaj numer wyrazu ciągu Fibonacciego: "))

wynik = fibonacci(n)
print(f"{n}-ty wyraz ciągu Fibonacciego to: {wynik}")