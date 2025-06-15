
# 🔐 Hiding Text in an Image using Steganography

This is a Python-based project that uses **LSB (Least Significant Bit) steganography** to hide secret messages inside `.png` images. It allows users to securely embed and retrieve hidden text from images without visibly altering the image.

---

# How it Works

- **Input Image**: Use a `.png` image to hide your secret message.
- **Encode**: The message is converted to binary and embedded into the least significant bits of each pixel’s red color value.
- **Decode**: Extract the binary message from the image and convert it back to readable text.
- **No Visual Change**: The output image looks exactly the same as the input, making the message undetectable.

---

# Requirements

- Python 3.x  
- Pillow (install with: `pip install pillow`)

---

# How to Run

1. Clone or download the repository.

2. Install the required package:
   ```
   pip install pillow
   ```

3. Place your image in the project folder and rename it as:
   ```
   input.png
   ```

4. Open `steganography.py` and uncomment the following line to **encode**:
   ```python
   encode_text_to_image('input.png', 'output.png', 'you are beautiful')
   ```

5. Run the script:
   ```
   python steganography.py
   ```

6. To **decode** the message:
   - Comment the encode line
   - Uncomment the decode line:
     ```python
     decode_text_from_image('output.png')
     ```
   - Run the script again:
     ```
     python steganography.py
     ```

---

# Features

- Hide and retrieve short secret messages securely inside images
- No visible change in the image
- Supports both RGB and RGBA `.png` images
- Simple and lightweight logic using Pillow
- Command-line-based interaction

---

# Screenshots

### 🔐 Message Encoding Output
> After hiding the message into `input.png`
```
C:\Users\HP\OneDrive\Desktop\st_python>python steganography.py  
Message encoded successfully!
```
![Encoding](screenshots/encode_success.png)

---

### 🔓 Message Decoding Output
> After extracting the hidden message from `output.png`
```
Decoded message: you are beautiful
```
![Decoding](screenshots/decode_success.png)

---

### 📁 Folder View
> Final output image (`output.png`), input image (`input.png`), and code file (`steganography.py`) in the project folder.
![Folder View](screenshots/folder_view.png)

---

# Future Improvements

- Add support for hiding longer messages and even files
- Password-based encryption before hiding
- GUI version using Tkinter
- Drag-and-drop support for images and message input

---

# Created by

**Sakkuri Sirisha**  
CSE (AI-ML)  
Capstone Project – 2025
