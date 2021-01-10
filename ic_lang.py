from json import load

with open("data.json") as r:
    data = load(r)

for language, data_2 in data.items():
    ic = 0
    for key, value in data_2.items():
        ic += value**2
    print("For", language, 'index of coincidence is', ic)
