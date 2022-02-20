'''
1.1 Feladat
Készíts egy programot, amely a felhasználótól számokat kér be mindaddig, amíg az csupán ENTER-t nem üt! A számokat tárolja el a program egy listában! Az adatbekérés befejezte után írja ki a program a lista elemeit, a legkisebb és a legnagyobb számot!

'''

lista = []

while True:
    beker = input('Szám: ')
    if beker == '':
        break
    lista.append(int(beker))

print('A lista elemei:',lista)
print(f'A lista legkisebb eleme: {min(lista)}')
print(f'A lista legnagyobb eleme: {max(lista)}')