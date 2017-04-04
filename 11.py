pocet_radku = int(input('Zadej vysku pyramidy: '))
for radek in range(pocet_radku):
    for sloupec in range(radek+1):
        print('X', end = ' ') 
    print()    