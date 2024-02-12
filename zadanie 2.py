def pole_trapezu(a, b, h):
    pole = 0.5 * (a + b) * h
    return pole

a = float(input("Podaj długość krótszej podstawy trapezu: "))
b = float(input("Podaj długość dłuższej podstawy trapezu: "))
h = float(input("Podaj wysokość trapezu: "))

pole = pole_trapezu(a, b, h)
print("Pole trapezu o podstawach", a, "i", b, "oraz wysokości", h, "wynosi:", pole)