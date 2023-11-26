def main():
    public_key, private_key, encrypt, decrypt = rsa()

    message = int(input("Enter a message to encrypt (as an integer): "))
    
    encrypted_message = encrypt(message)
    print("Public key is: ",public_key)
    print("Encrypted message:", encrypted_message)