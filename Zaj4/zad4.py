with open("C:\\Python\\AI\\Zaj4\\bayes.txt") as f:
    read = f.readlines()

nodes = read[1].replace("\n", "").split(",")
prob = {}

isProb = False
for line in read:
    if line == "Probabilities:\n":
        isProb = True
        continue

    if isProb:
        line = line.replace("\n", "").replace("P(", "").replace(")", "").split("=")
        prob.update({
            line[0].replace(" ", ""):float(line[1])
        })

def solve_bayes(query):
    query = query.replace("P(", "").replace(")", "")
    if query in prob:
        return prob[query]
    else:
        if "|" not in query and query.startswith("~"):
            if query.replace("~", "") in prob:
                return 1 - prob[query.replace("~", "")]
            else:
                return 1-solve_bayes(query.replace("~", ""))

        out = 0
        if "|" not in query:
            for i in prob:
                key = i
                value = prob[i]
                if "|" in key:
                    if query in key.split("|")[0]:
                        arguments = key.split("|")[1].split(",")
                        tempOut = value
                        for j in arguments:
                            temp = solve_bayes(j)
                            tempOut *= float(temp)
                        out += tempOut
        else:
            if query in prob:
                return prob[query]
            tempQuery = query.split("|")[0]
            valList = query.split("|")[1].split(",")
            for i in valList:
                if i in prob:
                    prob[i] = 1
                else:
                    prob.update({
                        i:1
                    })
            return solve_bayes(tempQuery)

        if query.startswith("~"):
            return 1-out
        else:
            return out

print("Wprowadz szukane prawdopodobienstwo np. P(MA|G), P(~G), P(GR|G,D)\nProsze uzywac duzych liter!")
exampleInput = "P(MA|D)"
print(solve_bayes(input("> ")))

# for _ in range(1):
#     pass
