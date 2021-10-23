import random
import math
import numpy as np


def modalPow(num, power, n):
    c = 1

    for i in range(power):
        c = c * num % n

    return c


def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a % b)


def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            return False
    return True


def getPrimeNumbers(numByteSize, quantity=2):
    numByteLimit = 2 ** numByteSize
    primeNumbers = []

    for i in range(quantity):
        primeNumbers.append(random.randint(3, numByteLimit))

        while (not (isPrime(primeNumbers[i]) and primeNumbers[i] in primeNumbers)):
            primeNumbers[i] = random.randint(3, numByteLimit)

    return primeNumbers


def getModule(a, b):
    return a * b


def getEulerFuncValue(a, b):
    return (a - 1) * (b - 1)


def getPublicKey(eulerFuncValue, numByteSize, module):
    for i in range(int(eulerFuncValue / numByteSize), eulerFuncValue):
        if (gcd(i, eulerFuncValue) == 1 and i < module):
            return i


def getPrivateKey(publicKey, eulerFuncValue):
    for i in range(eulerFuncValue):
        if ((publicKey * i) % eulerFuncValue == 1):
            return i


def encrypt(n, e, text):
    encryptedText = []

    for char in text:
        encryptedChar = modalPow(ord(char), e, n)
        encryptedText.append(encryptedChar)

    return encryptedText


def decrypt(n, d, text):
    decryptedText = []

    for code in text:
        decryptedChar = modalPow(code, d, n)
        decryptedText.append(chr(decryptedChar))

    return decryptedText


def main():
    print('------------')
    text = input("Input your text: ")

    numByteSize = 10
    primeNumbers = getPrimeNumbers(numByteSize)
    module = getModule(*primeNumbers)
    eulerFuncValue = getEulerFuncValue(*primeNumbers)
    publicKey = getPublicKey(eulerFuncValue, numByteSize, module)
    privateKey = getPrivateKey(publicKey, eulerFuncValue)

    print('------------')
    print('p q:', *primeNumbers)
    print('n:', module)
    print('φ:', eulerFuncValue)
    print('e:', publicKey)
    print('d:', privateKey)

    print('------------')
    print('Your text:', text)
    print('------------')

    encryptedText = encrypt(module, publicKey, text)
    print('Encrepted text:', end=" ")
    for i in encryptedText:
        print(i, end=" ")

    print('\n------------')

    decryptText = decrypt(module, privateKey, encryptedText)
    print('Decrypted text:', end=" ")
    for i in decryptText:
        print(i, end="")

    print('\n------------')


if __name__ == '__main__':
    main()
