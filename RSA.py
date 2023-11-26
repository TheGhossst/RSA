def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

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
        
    n = p * q

    phi_n = (p - 1) * (q - 1)
    
    possible_e_values = [e for e in range(2, phi_n) if gcd(e, phi_n) == 1]
    
    print(f"Possible values of e (1 < e < {phi_n}) that are relatively prime to {phi_n}:")
    print(possible_e_values)
    
    e = int(input("Choose one of the values for e from the list above: "))
    while e not in possible_e_values:
        e = int(input("Invalid input. Please choose a valid value for e: "))



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
