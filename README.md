# AICTE---Secure-Data-Hiding-in-image-using-Steagnography


📌 Project Overview
This project provides a secure and user-friendly way to encrypt and decrypt messages within images using steganography and password protection. The message is embedded inside an image using OpenCV and can only be retrieved with the correct password.

🛠️ Technologies Used
Python – Programming language
OpenCV – Image processing
NumPy – Array manipulation
PyQt6 – Graphical User Interface (GUI)
🔥 Features
✔ Steganography-based encryption – Hides messages within image pixels.
✔ Password-protected decryption – Ensures secure message retrieval.
✔ Graphical User Interface (GUI) – Easy-to-use interface.
✔ No need for external storage – The message is stored directly in the image.
✔ Works with PNG images – Saves encrypted images in lossless format.

Install dependencies:
pip install opencv-python numpy PyQt6
🚀 Usage
Encrypt an Image
Run the encryption script:
python encrypt_gui.py
Enter the secret message and password.
Click on Encrypt Image, and it will generate an encrypted image.
Decrypt an Image
Run the decryption script:
python decrypt_gui.py
Enter the password used during encryption.
If the password is correct, the hidden message will be revealed.
🎯 Screenshots
🔐 Encryption Process
Encryption_Output

🔓 Decryption Process
Decryption_Output

🎯 Future Scope
✅ Support for multiple image formats (JPG, BMP, etc.)
✅ Implementation of AES encryption for extra security
✅ Development of a mobile and web application
✅ AI-based image security and tampering detection

🙌 Contributing
Feel free to fork this repository, raise issues, or contribute enhancements! 😊
