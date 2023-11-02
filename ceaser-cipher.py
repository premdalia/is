def encrypt(plain,key):
    result=""
    for i in range(len(plain)):
        char=plain[i]
        if char.islower():
            result=result+chr((ord(char)-97+key)%26+97)
        else:
            result=result+chr((ord(char)-65+key)%26+65)

    return result

plaintext="H"
key=3
print("ans is : "+encrypt(plaintext,key))



def decrypt(plain,key):
    result=""
    for i in range(len(plain)):
        char=plain[i]
        if char.islower():
            result=result+chr((ord(char)-97-key)%26+97)
        else:
            result=result+chr((ord(char)-65-key)%26+65)

    return result
plaintext="ebh"
key=3
print("ans is : "+decrypt(plaintext,key))
