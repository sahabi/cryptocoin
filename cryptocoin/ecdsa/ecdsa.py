
import os
from binascii import hexlify, unhexlify
from hashlib import sha256
from binascii import unhexlify
import hashlib

def generate_secret(form='hex'):
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

def generate_pub_point(secret, generator):
    x,y = (secret*g).pair()
    return g.__class__(g.curve(), x, y)

def generate_uncompressed_sec(pub_point):
    prefix = "04"
    x = hex(pub_point.x())[2:-1]
    y = hex(pub_point.y())[2:-1]
    sec = prefix + x + y
    return unhexlify(sec)

def ripemd160(data):
    return hashlib.new("ripemd160", data)

def hash160(sec):
    return ripemd160(sha256(sec).digest()).digest()

if __name__ == "__main__":
    from secp256k1 import generator_secp256k1 as g
    secret = generate_secret("int")
    print(secret)
    pub_point = generate_pub_point(secret, g)
    print generate_uncompressed_sec(pub_point) 
