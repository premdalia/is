def monoencry(plaintext,key):
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    Cipher=""
    for char in plaintext:
        if char.upper() in alphabet:
            charindex=alphabet.index(char.upper())
            enc_chr=key[charindex]
            if char.islower():
                Cipher=Cipher+enc_chr.lower()
            else:
                Cipher=Cipher+enc_chr
        else:
             Cipher+=char       
    return Cipher
plaintext="ABC2VD"
key="FADHIWOMNKPLJUXTBSQVGRCBYZ"
print("ans is : ",monoencry(plaintext,key))