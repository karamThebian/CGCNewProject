from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(3072)

pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

def rsaEncrypt(token):
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(token)

    return encrypted
def rsaDecrypt(encToken):
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encToken)
    return  decrypted
