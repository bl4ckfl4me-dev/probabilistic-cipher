import random
import string


def generate_key(length):
    """Генерирует случайный ключ заданной длины."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def probabilistic_cipher_encrypt(plaintext, key):
    """Шифрование с использованием одноразового ключа (OTP) с добавлением случайных смещений."""
    ciphertext = []
    offsets = []  # Список для хранения смещений

    for p, k in zip(plaintext, key):
        random_offset = random.randint(1, 10)
        c = chr((ord(p) + ord(k) + random_offset) % 256)
        ciphertext.append(c)
        offsets.append(random_offset)

    return ''.join(ciphertext), offsets


def probabilistic_cipher_decrypt(ciphertext, key, offsets):
    """Дешифрование с использованием одноразового ключа (OTP) с учётом смещения."""
    plaintext = []

    for c, k, offset in zip(ciphertext, key, offsets):
        p = chr((ord(c) - ord(k) - offset) % 256)
        plaintext.append(p)

    return ''.join(plaintext)
