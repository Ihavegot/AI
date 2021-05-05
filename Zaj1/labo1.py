f = open("C:\\Python\\AI\\Zaj1\\baza-wiedzy.txt")
#Podaje całą ścieżkę, ponieważ inaczej wyskakują błędy
read = f.readlines()
fakty = read[len(read)-1].rstrip('\n').split(',')
warunki = []
wnioski = []

for i in read:
    #Warunki
    zformatowane = i.rstrip('\n').split()
    if i == 'fakty\n':
        break
    temp = zformatowane[1].split(',')
    warunki.append(temp)
    #Wnioski
    temp = zformatowane[-1]
    wnioski.append(temp)

czyZaszlaZmiana = True
#Sprawdzenie
while czyZaszlaZmiana:
    czyZaszlaZmiana = False
    print(fakty)
    for i in range(len(warunki)):
        if all(j in fakty for j in warunki[i]):
            if wnioski[i] not in fakty:
                czyZaszlaZmiana = True
                fakty.append(wnioski[i])

f.close()