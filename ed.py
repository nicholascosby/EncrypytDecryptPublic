from Crypto.Cipher import AES
import random
import string
import os
import base64


def genKey():
    return(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32)))
    # return(Random.new().read(BLOCK_SIZE))


def encrypt(toenc, key):
    cipher = AES.new(key, AES.MODE_ECB)
    #toenc = "b\'"+toenc+'\''
    toenc = addLength(toenc)
    msg = base64.b64encode(cipher.encrypt(toenc))
    return(msg)


def addLength(srt):
    while len(srt) % 16 != 0:
        srt = srt + ' '
    return srt


def decrypt(todec, key):
    cipher2 = AES.new(key, AES.MODE_ECB)
    plaintext = cipher2.decrypt(base64.b64decode(todec))
    return(plaintext)


key = ''
text = ''
print('Welcome to AES Encryption')
print('COPYRIGHT SOMEWHERE SOMETHING RABBLE RABBLE, not really')
print('Made by Nick\n\n')
print('Press 1 to encrypt, 2 to decrypt, 3 to save a key, anything else to quit')
res = input()
while res == '1' or res == '2' or res == '3':
    if res == '1':
        print('\nEncrypton')
        print('Press 1 to input key, 2 to load from file, 3 for random')
        res2 = input()
        if res2 == '1':
            print('Key:')
            key = input()

        if res2 == '2':
            print("Contents of keys directory:")
            print(os.listdir('./keys'))
            print("Type file name with extention:")
            file = input()
            path = './keys/'+file
            openedfile = open(path, 'r')
            key = openedfile.read()

        if res2 == '3':
            key = genKey()

        key = addLength(key)
        print('Key: ', key)
        print('Message:')
        text = input()
        res = encrypt(text, key)
        print('Result: ', res.decode())
    if res == '2':
        print('\nDecrypton')
        print('Press 1 to input key, 2 to load from file')
        res2 = input()
        if res2 == '1':
            print("Key:")
            key = input()

        if res2 == '2':
            print("Contents of keys directory:")
            print(os.listdir('./keys'))
            print("Type file name with extention:")
            file = input()
            path = './keys/'+file
            openedfile = open(path, 'r')
            key = openedfile.read()
        print("Cypher Text:")
        msg = input()
        key = addLength(key)
        msg = addLength(msg)
        print(decrypt(msg, key).decode())
    if res == '3':
        print('\nSave key to file')
        print('Press 1 to manually enter key, 2 for random')
        sel = input()
        if sel == '1':
            print('Enter key:')
            key = input()
        if sel == '2':
            key = genKey()
        print("Choose name for the key:")
        keyname = './keys/'+input()+'.txt'
        file = open(keyname, 'w')
        file.write(key)
        file.close()
        print('Key saved!')
    print('Press 1 to encrypt, 2 to decrypt, 3 to save a key, anything else to quit')
    res = input()
