
def openFile(url):
    return open(str(url), "rb").read()


def modalPow(num, power, n):
    c = 1

    for i in range(power):
        c = c * num % n

    return c


def encrypt(n, e, text):
    encrypted_text = []

    for char_code in text:
        encrypted_char = modalPow(int(char_code), e, n)
        encrypted_text.append(encrypted_char)

    return encrypted_text


def decrypt(n, d, text):
    decrypted_text = []

    for char_code in text:
        decrypted_char = modalPow(int(char_code), d, n)
        decrypted_text.append(chr(decrypted_char))

    return decrypted_text


def main():

    #n = 221
    #e = 5
    #d = 77

    print("------------------")
    method = input(
        "What do you want to do? Enter ENC for encrypting and DEC for decrypting: ")

    if(method == "ENC"):
        print("------------------")
        fileUrl = input("Input url to the file, which you want to encrypt: ")
        text = openFile(fileUrl)

        print("------------------")
        n, e = map(int, input('Enter n and e: ').split())

        with open("encrypted_file.txt", "w") as output:
            for code in (encrypt(n, e, text)):
                output.write(str(code) + " ")

        print("------------------")
        print("SUCCESS!")
        print("------------------")
    elif(method == "DEC"):
        print("------------------")
        n, d = map(int, input('Enter n and d: ').split())

        with open("decrypted_file.txt", "w") as output:
            for char in (decrypt(n, d, openFile("encrypted_file.txt").split())):
                output.write(str((char)).strip("\n"))

        print("------------------")
        print("SUCCESS!")
        print("------------------")
    else:
        print("------------------")
        print("Unknown command")
        print("------------------")


if __name__ == "__main__":
    main()
