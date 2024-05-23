from Crypto.Hash import SHA256
from Crypto.Util.number import bytes_to_long
from Crypto.PublicKey import RSA
import sys

#________Reading the public key_____#
public_key = sys.argv[1]
with open(public_key) as pubkey:
    n = int(pubkey.readline())
    e = int(pubkey.readline())
    
#_______Reading the message and the signature files______#
with open("message.txt", "rb") as file_in:
    message = file_in.read()

with open("signature.txt", "rb") as file_in:
    signature = int (file_in.read())

#________Hashing________#
H = bytes_to_long(SHA256.new(message).digest())
check=pow(signature,e,n)

#________comparing and printing the decission
if check == H :
    print("This is the sender's signature.")
else:
    print("This is not the sender's signature.")
