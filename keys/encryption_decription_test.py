from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode 

def encrypt_RSA(public_key_loc, message):
    '''
    param: public_key_loc Path to public key
    param: message String to be encrypted
    return base64 encoded encrypted string
    '''
    
    key = open(public_key_loc, "r").read()
    rsakey = RSA.importKey(key)
    rsakey = PKCS1_OAEP.new(rsakey)
    encrypted = rsakey.encrypt(message)
    return encrypted.encode('base64')
"""
def decrypt_RSA(private_key_loc, package):
    '''
    param: public_key_loc Path to your private key
    param: package String to be decrypted
    return decrypted string
    '''

    
    key = open(private_key_loc, "r").read() 
    rsakey = RSA.importKey(key) 
    rsakey = PKCS1_OAEP.new(rsakey) 
    decrypted = rsakey.decrypt(b64decode(package)) 
    return decrypted
"""

#print decrypt_RSA("private.pem",encrypt_RSA("public.pem",m))
def decrypt_RSA(private_key_loc, message):

#    open("zabb","w").write(message)
#    print "######################################\n"
    chunks = []
    print message.count('-')
    chunks = message.split('-')
    print "decrypting ... " + `chunks`
    plain = []
    key = open(private_key_loc, "r").read()
    rsakey = RSA.importKey(key)
    rsakey = PKCS1_OAEP.new(rsakey)
    for i in range(len(chunks)):
        print "chunk %s" %(i)
        decrypted = rsakey.decrypt(b64decode(chunks[i].rstrip()))
        plain.append(decrypted)
    return  "".join(plain)

m=open("../server/zabb","r").read()

x= decrypt_RSA("../server/server_private.pem",m)

print x