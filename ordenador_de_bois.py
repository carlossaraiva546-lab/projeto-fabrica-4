nome1 = input("Digite o nome do boi: ")
peso1 = float(input(f"Digite o peso do {nome1}: "))

nome2 = input("Digite o nome do segundo boi: ")
peso2 = float(input(f"Digite o peso do {nome2}: "))

nome3 = input("Digite o nome do boi: ")
peso3 = float(input(f"ddigite o peso do {nome3}: "))

if peso1 > peso2 and peso1 > peso3:
    if peso2 > peso3:
        print(f"{nome1},{nome2},{nome3}")
    else:
        print(f"{nome1},{nome3},{nome2}")
elif peso2 > peso1 and peso2 > peso3:
    if peso1 > peso3:
        print(f"{nome2}, {nome1}, {nome3}")
    else:
        print(f"{nome2}, {nome3}, {nome1}")
else:
    if peso1 > peso2:
        print(f"{nome3}, {nome1}, {nome2}")
    else:
        print(f"{nome3}, {nome2}, {nome1}")