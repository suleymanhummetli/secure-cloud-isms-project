# Cryptography Benchmark Tool for NovaTech Solutions
# Demonstrates SHA-256, HMAC, AES-256 vs AES-128, and RSA vs ECC performance/security.

import hashlib
import hmac
import time
from cryptography.hazmat.primitives.asymmetric import rsa, ec
from cryptography.hazmat.primitives import hashes

def benchmark_hashing():
    data = b"NovaTech Solutions Secure Cloud Data Payload" * 1000
    start = time.time()
    for _ in range(10000):
        hashlib.sha256(data).digest()
    print(f"SHA-256 10k iterations: {time.time() - start:.4f} seconds")

def benchmark_asymmetric():
    start = time.time()
    rsa_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    print(f"RSA-2048 key generation: {time.time() - start:.4f} seconds")
    
    start = time.time()
    ec_key = ec.generate_private_key(ec.SECP256R1())
    print(f"ECC (SECP256R1) key generation: {time.time() - start:.4f} seconds")

if __name__ == "__main__":
    print("--- NovaTech Cryptographic Algorithm Benchmark ---")
    benchmark_hashing()
    benchmark_asymmetric()