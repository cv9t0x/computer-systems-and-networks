import matplotlib.pyplot as plt

data = []

with open("data.txt") as f:
    while True:
        line = f.readline()[:-1]

        if line == "":
            break

        data.append(float(line))

plt.hist(data, bins=10000)
plt.ylabel("Частота")
plt.xlabel("Время в мс")
plt.xlim([60, 95])

plt.show()
