import math

def pole_kola(promien):
    pole = math.pi * promien**2
    return pole

promien = float(input("Podaj promień koła: "))
pole = pole_kola(promien)
print("Pole koła o promieniu", promien, "wynosi:", pole)