f = open("C:\\Python\\AI\\Zaj2\\baza-wiedzy-negacja.txt")
read = f.readlines()
f.close()

fakty = read[-1].rstrip('\n').split(',')
warunki = []
wnioski = []
spelnione = []
stack = []


for i in read:
    if i == 'Fakty\n':
        break
    formated = i.rstrip('\n')
    conditionStart = formated.find(".")+1
    conditionEnd = formated.find("->")

    command = ""
    for j in range(conditionStart, conditionEnd):
        command += formated[j]
    
    warunki.append(command.split(","))
    wnioski.append(formated[-1])

    temp = []
    temp.append(command.split(","))
    temp.append(formated[-1])

    stack.append(temp)

czyZaszlaZmiana = True

while czyZaszlaZmiana:
    czyZaszlaZmiana = False
    print(fakty)
    for i in stack:
        isTrue = True
        for j in i[0]:
            if "~" in j:
                if j[1] in fakty:
                    isTrue = False
                    break
            else:
                if j not in fakty:
                    isTrue = False
                    break
        if isTrue:
            if i[1] not in fakty:
                if i not in spelnione:
                    spelnione.append(i)
                fakty.append(i[1])
                czyZaszlaZmiana = True
        else:
            if i in spelnione:
                if i[1] in fakty:
                    fakty.remove(i[1])
                spelnione.remove(i)
                czyZaszlaZmiana = True

print(f"Final: {fakty}")