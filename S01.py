#challenge1
import codecs
hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
ba64 = codecs.encode(codecs.decode(hex,"hex"),"base64").decode()
print(ba64)


#challenge 2:


def xor_cry_decry(text,key):
    texte_en = bytes.fromhex(text)
    key_en = key.encode()
    
    resultat = []
    for i in range(len(texte_en)):
        byt = texte_en[i] ^ key_en[i % len(key_en)]
        resultat.byte.hex()
    text_de = bytes(resultat).decode()    
    
    return text_de

text = "1c0111001f010100061a024b53535009181c"
key =  "686974207468652062756c6c277320657965"
    
text_de = xor_cry_decry(text,key)
print("Decry",text_de)   

def it2(x,y):
    
    a = bytes.fromhex(x)
    b = bytes.fromhex(y)
    c = bytes([b1 ^ b2 for b1, b2 in zip(a,b)])
    d = c.hex()
    return d

x = "1c0111001f010100061a024b53535009181c"
y =  "686974207468652062756c6c277320657965"
    
d = it2(x,y)

print("Decry",d)   

#challenge 3
import binascii

def hex_to_bytes(hex_string):
    return binascii.unhexlify(hex_string)


def decrypt_single_byte_xor(ciphertext):
    
    ciphertext_bytes = hex_to_bytes(ciphertext) 
    max_score = 0  
    best_plaintext = ''  
    best_key = None  
    
    for key in range(256):
        plaintext_bytes = bytearray()
        for byte in ciphertext_bytes:
            plaintext_bytes.append(byte ^ key)
        
        plaintext = plaintext_bytes.decode(errors='ignore')  
        score = sum([plaintext.count(char.lower()) for char in 'etaoinshrdlu'])
        
    if score > max_score:
          max_score = score
          best_plaintext = plaintext
          best_key = key
    
    return best_plaintext, best_key

hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
plaintext, key = decrypt_single_byte_xor(hex_string)

print(f"Message déchiffré: {plaintext}")
print(f"Clé utilisée: {key}")






#challenge 7  
    
from Crypto.Cipher import AES
import base64

def decrypt_aes_ecb(ciphertext_b64, key):
    
    ciphertext = base64.b64decode(ciphertext_b64)
    
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    
    plaintext = cipher.decrypt(ciphertext)
    
    # Remove any PKCS#7 padding that may have been added during encryption
    plaintext = remove_pkcs7_padding(plaintext)
    
    # Decode from bytes to string
    plaintext = plaintext.decode('utf-8')
    
    return plaintext

def remove_pkcs7_padding(data):
    pad_len = data[-1]
    return data[:-pad_len]

# Base64-encoded ciphertext
ciphertext_base64 = b"""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"""

# Key for AES-128 in ECB mode (16 bytes)
key = "YELLOW SUBMARINE"

# Decrypt and print the plaintext
plaintext = decrypt_aes_ecb(ciphertext_base64, key)
print("Decrypted plaintext:")
print(plaintext)

 
 
 # ERROR#challenge 7_2
 #from Crypto.Cipher import AES
#import binascii

#key = b'ABCDEFGHIJIKLMOP'
#cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
#msg = cipher.encrypt(b'a4dd23fff740b203efe19d5cbbc24bba')
#msg = (b'AAAAAAAAAAAAAAAA')
#print(type(msg))
#print(msg.hex())
#cipher = AES.new(key, AES.MODE_ECB)


#msg_en = cipher.encrypt(msg)
#print("       ")
#print(binascii.hexlify(msg_en))
#print(type(msg_en))

#print("--------")
#decipher = AES.new(key, AES.MODE_ECB)

#msg_dec = decipher.decrypt(msg_en)
#print(msg_dec)
#print(binascii.hexlify(msg_dec))
#print(type(msg_dec))   


#challenge 5

def iter5(message, key):
    message_bytes = message.encode()
    key_bytes = key.encode()
    
    ciphertext = []
    
    for i in range(len(message_bytes)):
        encrypted_byte = message_bytes[i] ^ key_bytes[i % len(key_bytes)]
        ciphertext.append(encrypted_byte)
    
    encrypted_hex = ''.join(format(byte, '02x') for byte in ciphertext)
    
    return encrypted_hex

message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"

encrypted_text = iter5(message, key)
print(encrypted_text)
 