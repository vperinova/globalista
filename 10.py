delka_strany = int(input('Zadej delku strany: '))

for radek in range(delka_strany):
    for sloupec in range(delka_strany):
        print(radek * sloupec, end=' ')
    print()