
import os
from binascii import hexlify, unhexlify
from hashlib import sha256

def generate_key(form='hex'):
    """Generates a random number in the specified format"""
    N = (1.158 * (10**77)) - 1
    random_bits = 0
    while (random_bits >= N) or random_bits == 0:
        random_bits = os.urandom(int(256/8))
    	key_hex = hexlify(sha256(random_bits).digest())
        if form == 'hex':
            return key_hex 
        elif form == 'int':
            return int(key_hex, 16)
        else:
            print("Check the inputs: format = {}".format(form))
   
if __name__ == "__main__":
    print(generate_key("hex"))
    print(generate_key("int"))
