from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from probabilistic_cipher import probabilistic_cipher_encrypt, probabilistic_cipher_decrypt, generate_key
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Вероятностный шифр')

        layout = QVBoxLayout()

        # Поле ввода текста
        self.plaintext_input = QLineEdit(self)
        self.plaintext_input.setPlaceholderText('Введите текст для шифрования')
        layout.addWidget(self.plaintext_input)

        # Кнопка для шифрования
        self.encrypt_button = QPushButton('Зашифровать', self)
        self.encrypt_button.clicked.connect(self.encrypt_text)
        layout.addWidget(self.encrypt_button)

        # Поле для вывода зашифрованного текста
        self.ciphertext_output = QTextEdit(self)
        self.ciphertext_output.setPlaceholderText('Зашифрованный текст...')
        self.ciphertext_output.setReadOnly(True)
        layout.addWidget(self.ciphertext_output)

        # Поле для вывода ключа
        self.key_output = QLabel('Ключ: ', self)
        layout.addWidget(self.key_output)

        # Поле для вывода расшифрованного текста
        self.decrypted_output = QTextEdit(self)
        self.decrypted_output.setPlaceholderText('Расшифрованный текст...')
        self.decrypted_output.setReadOnly(True)
        layout.addWidget(self.decrypted_output)

        self.setLayout(layout)

    def encrypt_text(self):
        plaintext = self.plaintext_input.text()
        key = generate_key(len(plaintext))

        ciphertext, offsets = probabilistic_cipher_encrypt(plaintext, key)
        decrypted_text = probabilistic_cipher_decrypt(ciphertext, key, offsets)

        self.ciphertext_output.setText(ciphertext)
        self.key_output.setText(f'Ключ: {key}')
        self.decrypted_output.setText(decrypted_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.resize(400, 300)
    ex.show()
    sys.exit(app.exec_())
