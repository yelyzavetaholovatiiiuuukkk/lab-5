def oblicz_pole_trojkata(a, b, c):
    67
    # Sprawdzenie warunku trójkąta
    if a <= 0 or b <= 0 or c <= 0 or (a + b) <= c or (a + c) <= b or (b + c) <= a:
        raise ValueError("Długości boków nie spełniają warunku trójkąta.")

    # Obliczenie półobwodu
    p = (a + b + c) / 2

    # Obliczenie pola trójkąta za pomocą wzoru Herona
    pole = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return pole


# Przykładowe użycie funkcji
try:
    a = float(input("Podaj długość boku a: "))
    b = float(input("Podaj długość boku b: "))
    c = float(input("Podaj długość boku c: "))

    pole = oblicz_pole_trojkata(a, b, c)
    print("Pole trójkąta o bokach", a, ",", b, ",", c, "wynosi:", pole)
except ValueError as e:
    print("Wystąpił błąd:", e)