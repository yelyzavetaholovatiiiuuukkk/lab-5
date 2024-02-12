def wypisz_imie_i_wiek(imie, wiek=18):

    print("Imię:", imie)
    print("Wiek:", wiek)

# Wyświetlenie opisu funkcji
print(wypisz_imie_i_wiek.__doc__)

# Przykładowe wywołania funkcji
wypisz_imie_i_wiek("Sebastian", 19)
wypisz_imie_i_wiek("Bożena")