with open("ping.txt", "r") as input:
    with open("data.txt", "w") as output:
        for line in input:
            if(len(line.split()) >= 8):
                if line.split()[7].startswith('time='):
                    output.write(line.split()[7].split('=')[1] + '\n')
