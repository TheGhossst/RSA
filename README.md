# RSA
Basic python implementation of RSA public key algorithm

# Algorithm
1. select two large prime numbers p and q 
2. multiply p and q to get n
3. chose a  number e which is less than n such that e is relatively prime to (p-1)*(q-1)    { (p-1)*(q-1) = phy(n) }
4. public key is the pair e,n 
5.cipher text is calculated as  m^e mod n
6.  private key equation is de mod phy(n) = 1   ( find d)
7. private key is the pair d,n
8. plain text is  CT^d mod n
