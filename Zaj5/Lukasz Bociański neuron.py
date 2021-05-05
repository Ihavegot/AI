import random

with open("C:\\Python\\AI\\Zaj5\\funkcje-logiczne.csv") as f:
    read = f.readlines()

logic = []

for line in read:
    if line == "x1,x2,x3,y1,y2,y3\n":
        continue
    temp = line.replace("\n", "").split(",")
    temp2 = []
    for i in temp:
        temp2.append(float(i))
    logic.append(temp2)


def sign(n):
    if n >= 1:
        return 1
    return 0


class Neuron:
    def __init__(self, size):
        self.weights = [
            random.uniform(-2, 2) for _ in range(size)
        ]

    def guess(self, inp):
        weigth_sum = 0
        for i, w in zip(inp, self.weights):
            weigth_sum += i * w
        return sign(weigth_sum)

    def train(self, inputs, target):
        error = float(target) - self.guess(inputs)
        for index in range(len(self.weights)):
            self.weights[index] += error * inputs[index] * 0.1


outs = [
    Neuron(4) for _ in range(3)
]

x = 3
for neuron in outs:
    for __ in range(100):
        for t in logic:
            neuron.train(t[:3] + [1], t[x])
    x += 1

guess_list = [
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1]
]

for ls in guess_list:
    out_temp = []
    for neuron in outs:
        out_temp.append(neuron.guess(ls+[1]))
    print(f"For {ls} = {out_temp}")