# Cryptography Benchmark Tool for NovaTech Solutions
# Implements SHA-256, HMAC-SHA256, AES-128/256 GCM, and RSA vs ECC signing/verification.

import hashlib
import hmac
import time
from cryptography.hazmat.primitives.asymmetric import rsa, ec, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def benchmark_hashing_and_hmac():
    data = b"NovaTech Solutions Secure Cloud Data Payload" * 1000
    secret_key = b"super-secret-hmac-key"
    
    start = time.time()
    for _ in range(10000):
        hashlib.sha256(data).digest()
    sha_time = time.time() - start
    
    start = time.time()
    for _ in range(10000):
        hmac.new(secret_key, data, hashlib.sha256).digest()
    hmac_time = time.time() - start
    
    print(f"SHA-256 (10k ops): {sha_time:.4f}s")
    print(f"HMAC-SHA256 (10k ops): {hmac_time:.4f}s")

def benchmark_aes():
    data = b"Confidential Customer Records Payload" * 100
    key_128 = AESGCM.generate_key(bit_length=128)
    key_256 = AESGCM.generate_key(bit_length=256)
    
    aes128 = AESGCM(key_128)
    aes256 = AESGCM(key_256)
    nonce = b"12bytesnonce!!"
    
    start = time.time()
    for _ in range(5000):
        ct = aes128.encrypt(nonce, data, None)
        aes128.decrypt(nonce, ct, None)
    aes128_time = time.time() - start
    
    start = time.time()
    for _ in range(5000):
        ct = aes256.encrypt(nonce, data, None)
        aes256.decrypt(nonce, ct, None)
    aes256_time = time.time() - start
    
    print(f"AES-128-GCM (5k enc/dec): {aes128_time:.4f}s")
    print(f"AES-256-GCM (5k enc/dec): {aes256_time:.4f}s")

def benchmark_signatures():
    message = b"Audit compliance verification token"
    
    # RSA 2048
    rsa_priv = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    rsa_pub = rsa_priv.public_key()
    
    start = time.time()
    sig = rsa_priv.sign(message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
    rsa_sign_time = time.time() - start
    
    start = time.time()
    rsa_pub.verify(sig, message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
    rsa_verify_time = time.time() - start
    
    # ECC SECP256R1
    ec_priv = ec.generate_private_key(ec.SECP256R1())
    ec_pub = ec_priv.public_key()
    
    start = time.time()
    ec_sig = ec_priv.sign(message, ec.ECDSA(hashes.SHA256()))
    ec_sign_time = time.time() - start
    
    start = time.time()
    ec_pub.verify(ec_sig, message, ec.ECDSA(hashes.SHA256()))
    ec_verify_time = time.time() - start
    
    print(f"RSA-2048 Sign: {rsa_sign_time:.4f}s | Verify: {rsa_verify_time:.4f}s")
    print(f"ECC-SECP256R1 Sign: {ec_sign_time:.4f}s | Verify: {ec_verify_time:.4f}s")

if __name__ == "__main__":
    print("=== NovaTech Cryptographic Performance Benchmark ===")
    benchmark_hashing_and_hmac()
    benchmark_aes()
    benchmark_signatures()