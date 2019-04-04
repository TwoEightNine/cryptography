from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

if __name__ == "__main__":
    data = b'some data'
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    encryptor = Cipher(
        algorithms.AES(b'x01' * 16), modes.CBC(b'\x00' * 16), default_backend()
    ).encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    print(ciphertext)
