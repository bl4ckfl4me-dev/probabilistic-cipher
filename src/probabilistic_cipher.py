import random
import string


def generate_key(length):
    """Генерирует случайный ключ заданной длины."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def probabilistic_cipher_encrypt(plaintext, key):
    """Шифрование с использованием одноразового ключа (OTP)."""
    ciphertext = []
    for p, k in zip(plaintext, key):
        c = chr((ord(p) + ord(k)) % 256)
        ciphertext.append(c)
    return ''.join(ciphertext)


def probabilistic_cipher_decrypt(ciphertext, key):
    """Дешифрование с использованием одноразового ключа (OTP)."""
    plaintext = []
    for c, k in zip(ciphertext, key):
        p = chr((ord(c) - ord(k)) % 256)
        plaintext.append(p)
    return ''.join(plaintext)
