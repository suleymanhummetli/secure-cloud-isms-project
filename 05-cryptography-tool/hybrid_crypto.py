import os
import argparse
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import serialization

def generate_keys(priv_path, pub_path):
    # RSA-2048 açar cütü yaratmaq
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    # Özəl açarı yadda saxlamaq
    with open(priv_path, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

    # Açıq açarı yadda saxlamaq
    with open(pub_path, "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
    print("[+] RSA açar cütü uğurla yaradıldı.")

def encrypt_file(file_path, pub_path, out_path):
    # Açıq açarı oxumaq
    with open(pub_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    # AES üçün təsadüfi 256 bitlik (32 bayt) açar yaratmaq
    aes_key = AESGCM.generate_key(bit_length=256)
    aesgcm = AESGCM(aes_key)
    
    # 12 baytlıq təsadüfi Nonce (IV) yaratmaq
    nonce = os.urandom(12)

    # Fayl məzmununu oxumaq
    with open(file_path, "rb") as f:
        plaintext = f.read()

    # Faylı AES-256-GCM ilə şifrələmək
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)

    # AES açarını RSA açıq açarı ilə şifrələmək (Hibrid mexanizm)
    encrypted_aes_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Şifrələnmiş məlumatları bir faylda toplamaq (Uzunluqlar + Şifrələnmiş açar + Nonce + Ciphertext)
    with open(out_path, "wb") as f:
        f.write(len(encrypted_aes_key).to_bytes(2, 'big'))
        f.write(encrypted_aes_key)
        f.write(nonce)
        f.write(ciphertext)

    print(f"[+] Fayl uğurla hibrid üsulla şifrələndi: {out_path}")

def decrypt_file(file_path, priv_path, out_path):
    # Özəl açarı oxumaq
    with open(priv_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    with open(file_path, "rb") as f:
        key_len = int.from_bytes(f.read(2), 'big')
        encrypted_aes_key = f.read(key_len)
        nonce = f.read(12)
        ciphertext = f.read()

    # AES açarını RSA özəl açarı ilə deşifrələmək
    aes_key = private_key.decrypt(
        encrypted_aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    aesgcm = AESGCM(aes_key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)

    with open(out_path, "wb") as f:
        f.write(plaintext)

    print(f"[+] Fayl uğurla deşifrələndi: {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NovaTech Hibrid Şifrələmə Aləti")
    subparsers = parser.add_subparsers(dest="command")

    # Keygen
    parser_keygen = subparsers.add_parser("keygen")
    parser_keygen.add_argument("--priv", required=True)
    parser_keygen.add_argument("--pub", required=True)

    # Encrypt
    parser_enc = subparsers.add_parser("encrypt")
    parser_enc.add_argument("--file", required=True)
    parser_enc.add_argument("--pub", required=True)
    parser_enc.add_argument("--out", required=True)

    # Decrypt
    parser_dec = subparsers.add_parser("decrypt")
    parser_dec.add_argument("--file", required=True)
    parser_dec.add_argument("--priv", required=True)
    parser_dec.add_argument("--out", required=True)

    args = parser.parse_args()

    if args.command == "keygen":
        generate_keys(args.priv, args.pub)
    elif args.command == "encrypt":
        encrypt_file(args.file, args.pub, args.out)
    elif args.command == "decrypt":
        decrypt_file(args.file, args.priv, args.out)
