def main():
    public_key, private_key, encrypt, decrypt = rsa()

    message = int(input("Enter a message to encrypt (as an integer): "))