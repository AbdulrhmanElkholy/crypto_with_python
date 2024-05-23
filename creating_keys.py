#_______abdelrahman_mohamed_elkhooly_____#
#_______cryptography_with_python_3rd_cycle___________#
#_______March 2024___________#

from Crypto.Util.number import *

#  crating the paremeters   #
    
p = getPrime(1024)      # large prime number 
q = getPrime(1024)      # large prime number 

n = p * q               # to Calculate 'n'
phi = (p-1) * (q-1)     # to Calculate 'phi'
e = 65537               
d = pow(e, -1, phi)     # to Calculate the private key 'd'


# Saving public and private keys to a file
with open("public_key.txt", "w") as public_file:
    public_file.write(str(n)+'\n')
    public_file.write(str(e))


with open("private_key.txt", "w") as private_file:
    private_file.write(str(n)+'\n')
    private_file.write(str(d))

print("Public and private keys saved to public_key.der and private_key.der")


