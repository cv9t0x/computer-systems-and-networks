blockedNetworksCount = 0

with open("blocked-networks.txt") as f:
    while True:
        line = f.readline()

        if line == "":
            break

        freeBytes = int(line.split('/')[1])
        blockedNetworksCount += pow(2, (32 - freeBytes))

print(blockedNetworksCount)
