def polyencrypt(plaintext,key):
    key=key.upper()
    key_length=len(key)
    ciphertext=""
    for i in range(len(plaintext)):
        char=plaintext[i]
        shift=ord(key[i%key_length])-65
        if char.isupper():
            ciphertext+=chr((ord(char)-65+shift)%26+65)
        else:
            ciphertext+=chr((ord(char)-97+shift)%26+97)
    return ciphertext
plaintext="ABCD"
key="bcd"
print("ans is/n",polyencrypt(plaintext,key))


def polydecrypt(plaintext,key):
    key=key.upper()
    key_length=len(key)
    plaintext=""
    for i in range(len(ciphertext)):
        char=ciphertext[i]
        shift=ord(key[i%key_length])-65
        if char.isupper():
            plaintext+=chr((ord(char)-65-shift)%26+65)
        else:
            plaintext+=chr((ord(char)-97-shift)%26+97)
    return plaintext
ciphertext="BDFE"
key="bcd"
print("ans is/n",polydecrypt(plaintext,key))


