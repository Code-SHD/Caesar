def encrypt(plain_text, k):
    encrypted = ""
    plain_text = list(plain_text)
    for i in range(len(plain_text)):
        value = ord(plain_text[i])
        encrypted += chr(value + k)
    return encrypted

def decrypt(encrypted_text, k):
    decrypted = ""
    encrypted_text = list(encrypted_text)
    for i in range(len(encrypted_text)):
        value = ord(encrypted_text[i])
        decrypted += chr(value - k)
    return decrypted
