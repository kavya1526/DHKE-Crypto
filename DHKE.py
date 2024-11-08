import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class DHKE:
    def __init__(self):
        self.__sharedKey = 0

    def calculateSharedKey(self, g_e, g_c, N_e, N_c, x, gy_modN):
        g = 2**g_e - g_c
        N = 2**N_e - N_c
        self.__sharedKey = pow(gy_modN, x, N)
        return self.__sharedKey

# Get inputs from command-line arguments
IV = bytes.fromhex(sys.argv[1].replace(" ", ""))
g_e = int(sys.argv[2])
g_c = int(sys.argv[3])
N_e = int(sys.argv[4])
N_c = int(sys.argv[5])
x = int(sys.argv[6])
gy_modN = int(sys.argv[7])
ciphertext_hex = sys.argv[8].replace(" ", "")
plaintext_str = sys.argv[9]

# Initialize DHKE and calculate shared key
dhke = DHKE()
sharedKey = dhke.calculateSharedKey(g_e, g_c, N_e, N_c, x, gy_modN)
sharedKey = sharedKey.to_bytes(32, 'little')  # Adjust size if necessary

# Encryption
cipher = AES.new(sharedKey, AES.MODE_CBC, IV)
P = bytes(plaintext_str, 'utf-8')
P = pad(P, AES.block_size)
encryptedcypher = cipher.encrypt(P)

# Decryption
cipher = AES.new(sharedKey, AES.MODE_CBC, IV)
C = bytes.fromhex(ciphertext_hex)
decryptedtext = cipher.decrypt(C)
decryptedtext = unpad(decryptedtext, AES.block_size)

# Printing the output
print(f"{decryptedtext.decode()}, {encryptedcypher.hex().upper()}")
