import math

output = ["0"] * 4
input = int(input("Input: "))

for i in range(math.ceil(input / 8)):
    sum = 0

    if(input <= 8):
        for j in range(7, 8 - input - 1, -1):
            sum += pow(2, j)

    elif(i == math.ceil(input / 8) - 1):
        for j in range(7, ((8 * (i + 1)) % input) - 1, -1):
            sum += pow(2, j)

    else:
        for j in range(8):
            sum += pow(2, j)

    output[i] = str(sum)

print("Mask is: " + ".".join(output))
