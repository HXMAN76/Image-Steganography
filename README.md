# Image Steganography App 👀

## Description

Image Steganography is the art of hiding text data within images such that it is invisible to the human eye. This project provides a graphical user interface (GUI) built with Python's Tkinter library, enabling users to:

* Import images
* Embed secret messages using Least Significant Bit (LSB) steganography
* Extract hidden messages from stego-images
* Save the resulting image after embedding a message

The goal of this application is to allow secure, user-friendly, and practical message hiding for privacy-conscious users.

---

## Table of Contents

1. [Installation](#installation)
2. [How to Use](#how-to-use)
3. [Technologies Used](#technologies-used)
4. [Challenges & Future Work](#challenges--future-work)
5. [Screenshots](#screenshots)
6. [Credits](#credits)
7. [License](#license)

---

## Installation

### Prerequisites:

* Python 3.x
* pip package manager
* Libraries: `tkinter`, `Pillow`

### Steps to Install:

```bash
# Clone the repository
git clone https://github.com/Rag-795/Image-Steganography.git

# Install required packages
pip install Pillow
```

---

## How to Use

1. **Run the App**

```bash
python MAIN.py
```

2. **Import Image**

* Click on "Import Image"
* Choose a PNG or JPG image from your system

3. **Embed Text**

* Type your secret message in the provided text box
* Click on "Hide message & save image"
* Save the modified image when prompted

4. **Extract Text**

* Import a stego-image (an image that contains hidden text)
* Click on "Show hidden message" to reveal the secret message

---

## Technologies Used

* **Python 3.x** - Core language for development
* **Tkinter** - For GUI components
* **Pillow (PIL)** - To manipulate and edit images
* **LSB Steganography Algorithm** - To hide data within image pixels

---

## Challenges & Future Work

### Challenges

* Ensuring that large texts don’t overflow the image capacity
* Proper error handling during embedding and extraction
* Maintaining image quality after embedding

### Future Enhancements

* Add support for audio/video steganography
* Implement drag-and-drop image upload
* Encrypt messages before embedding for double security
* Add format compatibility checks

---

## Screenshots

1. Embedding the text
![image](https://github.com/user-attachments/assets/2a7271f3-001d-4ffd-86e8-16507e30213a)

2. Retreiving the text
![image](https://github.com/user-attachments/assets/3950e8ea-9a2e-4364-b8ec-186864639ec6)

---

## Credits

* Hari Heman V K ([GitHub](https://github.com/HXMAN76))
* Raghav N ([GitHub](https://github.com/Rag-795))
* Dev Bala Saragesh ([GitHub](https://github.com/dbsaragesh-bs))
* Ghanasree ([GitHub](https://github.com/your-username))

### References:

* LSB Steganography concept from [Wikipedia](https://en.wikipedia.org/wiki/Steganography)

---

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). You are free to use, modify, and distribute this software.

---

## How to Contribute

If you'd like to contribute:

* Fork this repository
* Make your changes in a new branch
* Submit a Pull Request

For major changes, please open an issue first to discuss what you would like to change.

---
