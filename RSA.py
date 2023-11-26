def rsa():
    p = int(input("Enter a large prime number (p): "))


def main():
    public_key, private_key, encrypt, decrypt = rsa()

    message = int(input("Enter a message to encrypt (as an integer): "))
    
    encrypted_message = encrypt(message)
    print("Public key is: ",public_key)
    print("Encrypted message:", encrypted_message)
    
    decrypted_message = decrypt(encrypted_message)
    print("Private key is: ",private_key)
    print("Decrypted message:", decrypted_message)
    
       
if __name__ == "__main__":
    main()
