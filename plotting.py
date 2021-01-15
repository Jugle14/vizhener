from json import load
import matplotlib.pyplot as plt
import matplotlib as mpl

def x_y_maker(dic):
    xs = []
    ys = [[], [], []]
    
    for key, value in dic.items():
        xs.append(int(key))

        summ = sum(value.values())

        numbers = list(value.values())
        for i in range(3):
            ys[i].append(100*numbers[i]/summ)


    return xs, ys

modification = int(input("Write the number of modification>>"))

if modification == 0:
    path = "data_gather.json"
elif modification == 2:
    path = "data_gather_2.json"
elif modification == 3:
    path = "data_gather_3.json"

with open(path, 'r') as r:
    dic = load(r)

dic = list(dic.values())[0]
dpi = 80

figure = plt.figure(dpi=dpi, figsize = (2024/dpi, 1536/dpi))
mpl.rcParams.update({"font.size": 10})   #!!!!

#plt.title("Ефективність метода Лінквіста ")
plt.xlabel("Довжина зашифрованого тексту")
plt.ylabel("Відсоткове відношення випадків")

xs, ys = x_y_maker(dic)

y_max = 100

ax = plt.axes()
ax.yaxis.grid(True)
ax.xaxis.grid(True)
#plt.yticks([1, 3] + list(range(0, y_max))[::2])
plt.xticks(xs[::5] + [xs[-1]])
colors = ['r', 'c', 'k']
labels = ["I-ий випадок", "II-ий випадок", "III-ий випадок"]

for i in range(3):
    plt.plot(xs, ys[i], linestyle = 'solid', color=colors[i], label=labels[i])

plt.legend()

name = "results_" + str(modification) + ".png"
figure.savefig(name)
plt.xlim(10, xs[-1])
plt.show()
