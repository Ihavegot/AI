import itertools

f = open("C:\\Python\\AI\\Zaj3\\dung.txt")
read = f.readlines()
f.close()

class Actions:
    def __init__(self):
        self.attack = []
        self.state = None # IN = True, OUT = False, DEF = None

delSpecChar = read[3].replace(")"," ")
delSpecChar = delSpecChar.replace("(","").rstrip(" ")
delSpecChar = delSpecChar.split(" ,")

actions = {
    i:Actions() for i in read[1].rstrip("\n").split(",")
}

for i in actions:
    for j in delSpecChar:
        if j[2]==i:
            actions[i].attack.append(j[0])

#Grounded
visited = []
hasChanged = True
while hasChanged:
    hasChanged = False
    for defedner in actions:
        if defedner in visited:
            continue
        if not actions[defedner].attack and actions[defedner].state == None:
            visited.append(defedner)
            actions[defedner].state = True
            hasChanged = True
            break
        else:
            outCount = 0
            for attacker in actions:
                if attacker in actions[defedner].attack:
                    if actions[attacker].state == True:
                        visited.append(defedner)
                        actions[defedner].state = False
                        hasChanged = True
                        break
                    elif actions[attacker].state == False:
                        outCount += 1

            if outCount == len(actions[defedner].attack):
                visited.append(defedner)
                actions[defedner].state = True
                hasChanged = True

grounded = []
defensible = []
#Test
for i in actions:
    if actions[i].state == True:
        #print(f"{i} | IN")
        grounded.append(i)
    elif actions[i].state == False:
        #print(f"{i} | OUT")
        pass
    else:
        #print(f"{i} | DEF")
        defensible.append(i)

print("> GROUNDED <")
print(grounded)

#Prefered
options = [
    list(i) for i in itertools.product([True, False], repeat=len(defensible))
]

def chechDefensible(o):
    for k in actions[o].attack:
        if not actions[o].state and actions[k].state:
            return True
        if actions[o].state and actions[k].state:
            return False
    return actions[o].state

print("> PREFERED <")
for i in options:
    prefered = []
    isAcceptable = True
    for j, n in zip(defensible, i):
        actions[j].state = n
    for o in defensible:
        if not chechDefensible(o):
            isAcceptable = False
            break
    if isAcceptable:
        for m in actions:
            if actions[m].state:
                prefered.append(m)
        print(prefered)