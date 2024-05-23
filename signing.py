#_______abdelrahman_mohamed_elkhooly_____#
#_______cryptography_with_python_3rd_cycle___________#
from Crypto.Util.number import bytes_to_long
from Crypto.Hash import SHA256
import sys

usage = "Usage:\n> python sign.py [privkey.txt] [message.txt]"
if len(sys.argv) < 2:
    print(usage)
    exit()

#___load private key___#
with open(sys.argv[1], 'rb') as privkey:
    n = int(privkey.readline())
    d = int(privkey.readline())
    privkey.close()

#___read one-line message___#
with open(sys.argv[2], 'rb') as msg:
    M = msg.readline()
    msg.close()

#___calculate hash of the message M___#
H = bytes_to_long(SHA256.new(M).digest())

#___sign message M___#
signature = pow(H, d, n)

#___save signature file___#
with open("signature.txt", "w") as fout:
    fout.write(str(signature))
    print("signature saved to signature.txt")
    fout.close()
