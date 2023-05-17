def encrypt(text,s):
    result = ""
    for i in text:
        if i.isupper():
            result += chr((ord(i)+s-65)%26+65)
        elif i==' ':
            result += ' '
        else:
            result += chr((ord(i)+s-97)%26+97)
    return result

def decrypt(text, s):
    result = ""
    for i in text:
        if i.isupper():
            result += chr((ord(i)-65-s)% 26+65)
        elif i == ' ':
            result += ' '
        else:
            result += chr((ord(i)-s-97)%26+97)
    return result

def bruteforce(text):
    for i in range(25):
        r = decrypt(text,i)
        print(r)
text =  "Hello World"
shift = 4
result = encrypt(text, shift)
print("Encrpyted text" +result)
result1 = decrypt(result,shift)
print("Decrypted text" +result1)
bruteforce(text)