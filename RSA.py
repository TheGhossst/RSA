def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def rsa():
    p = int(input("Enter a large prime number (p): "))
    while not is_prime(p):
        p = int(input("Invalid input. Please enter a prime number for p: "))
        
    q = int(input("Enter another large prime number (q): "))
    while not is_prime(q):
        q = int(input("Invalid input. Please enter a prime number for q: "))


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
