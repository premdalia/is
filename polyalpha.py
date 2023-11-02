def polyalpha(plaintext,key):
    key=key.upper()
    ciphertext=''
    keylength=len(key)
    for i in range(len(plaintext)):
        char=plaintext[i]
        shift=ord(key[i%keylength])-65
        if char.isupper():
            enc_char=chr((ord(char)-65+shift)%26+65)
            ciphertext+=enc_char
        else:
             enc_char=chr((ord(char)-97+shift)%26+97)
             ciphertext+=enc_char
    return ciphertext
plaintext="abcd"
key="cde"
print("ans is: ",polyalpha(plaintext,key))