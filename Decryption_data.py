import sys
import cv2
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox

# Path to the encrypted image
image_path = r"C:\Users\Downloads\download_decrypt.png"

class DecryptGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Decryption")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Enter passcode for decryption:")
        layout.addWidget(self.label)

        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        self.decrypt_button = QPushButton("Decrypt Image", self)
        self.decrypt_button.clicked.connect(self.decrypt_image)
        layout.addWidget(self.decrypt_button)

        self.setLayout(layout)

    def decrypt_image(self):
        password_attempt = self.password_input.text()
        if not password_attempt:
            QMessageBox.warning(self, "Error", "Please enter the password to decrypt!")
            return

        img = cv2.imread(image_path)
        if img is None:
            QMessageBox.warning(self, "Error", "Encrypted image not found.")
            return

        # Get image dimensions
        height, width, _ = img.shape
        print(f"Image dimensions: {height}x{width}")

        n, m, z = 0, 0, 0

        try:
            # Retrieve stored password length and message length
            password_length = int(img[n, m, z])
            message_length = int(img[n + 1, m + 1, (z + 1) % 3])

            print(f"Password Length: {password_length}, Message Length: {message_length}")

            # Validate extracted lengths
            if password_length <= 0 or password_length > min(height, width):
                QMessageBox.warning(self, "Error", "Invalid password length detected.")
                return
            if message_length <= 0 or message_length > min(height, width):
                QMessageBox.warning(self, "Error", "Invalid message length detected.")
                return

            n += 2
            m += 2
            z = (z + 2) % 3
            extracted_password = ""

            # Extract stored password
            for _ in range(password_length):
                if n >= height or m >= width:
                    QMessageBox.warning(self, "Error", "Decryption failed: Out of bounds access.")
                    return
                extracted_password += chr(int(img[n, m, z]))
                n += 1
                m += 1
                z = (z + 1) % 3

            print(f"Extracted Password: {extracted_password}")

            # Check if password is correct
            if extracted_password != password_attempt:
                QMessageBox.warning(self, "Error", "Incorrect password! Access denied.")
                return

            message = ""

            # Extract hidden message
            for _ in range(message_length):
                if n >= height or m >= width:
                    QMessageBox.warning(self, "Error", "Decryption failed: Out of bounds access.")
                    return
                message += chr(int(img[n, m, z]))
                n += 1
                m += 1
                z = (z + 1) % 3

            print(f"Decrypted Message: {message}")

            QMessageBox.information(self, "Decryption Successful", f"Secret Message: {message}")

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Decryption failed: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DecryptGUI()
    window.show()
    sys.exit(app.exec())
