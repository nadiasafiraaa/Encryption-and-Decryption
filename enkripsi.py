import tkinter as tk
from tkinter import messagebox

# Fungsi untuk Caesar Cipher (Shift Cipher)
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Fungsi untuk Vigenère Cipher
def vigenere_encrypt(text, keyword):
    encrypted_text = ""
    keyword = keyword.upper()
    keyword_repeated = ""
    
    for i in range(len(text)):
        keyword_repeated += keyword[i % len(keyword)]
        
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(keyword_repeated[i]) - 65
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(text, keyword):
    decrypted_text = ""
    keyword = keyword.upper()
    keyword_repeated = ""
    
    for i in range(len(text)):
        keyword_repeated += keyword[i % len(keyword)]
        
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(keyword_repeated[i]) - 65
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

# Fungsi untuk menjalankan enkripsi atau dekripsi
def encrypt_text():
    text = entry_plaintext.get()
    key = entry_key.get()
    if var_method.get() == 1:  # Caesar Cipher
        shift = int(key) if key.isdigit() else 0
        result = caesar_encrypt(text, shift)
    else:  # Vigenère Cipher
        result = vigenere_encrypt(text, key)
    entry_ciphertext.delete(0, tk.END)
    entry_ciphertext.insert(0, result)

def decrypt_text():
    text = entry_ciphertext.get()
    key = entry_key.get()
    if var_method.get() == 1:  # Caesar Cipher
        shift = int(key) if key.isdigit() else 0
        result = caesar_decrypt(text, shift)
    else:  # Vigenère Cipher
        result = vigenere_decrypt(text, key)
    entry_plaintext.delete(0, tk.END)
    entry_plaintext.insert(0, result)

# Membuat GUI
root = tk.Tk()
root.title("Enkripsi & Dekripsi")
root.geometry("600x300")
root.configure(bg="#f7f7f7")

# Frame untuk metode enkripsi
frame_top = tk.Frame(root, bg="#f7f7f7")
frame_top.pack(pady=15)

var_method = tk.IntVar(value=1)
tk.Radiobutton(frame_top, text="Caesar Cipher", variable=var_method, value=1, bg="#f7f7f7", font=("Arial", 12)).grid(row=0, column=0, padx=20)
tk.Radiobutton(frame_top, text="Vigenère Cipher", variable=var_method, value=2, bg="#f7f7f7", font=("Arial", 12)).grid(row=0, column=1, padx=20)

# Frame untuk input teks
frame_middle = tk.Frame(root, bg="#f7f7f7")
frame_middle.pack(pady=15)

# Input Plaintext
tk.Label(frame_middle, text="Plaintext:", bg="#f7f7f7", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
entry_plaintext = tk.Entry(frame_middle, width=40, font=("Arial", 12))
entry_plaintext.grid(row=0, column=1, padx=10)

# Input Kunci
tk.Label(frame_middle, text="Kunci (Shift/Keyword):", bg="#f7f7f7", font=("Arial", 12)).grid(row=1, column=0, sticky="w")
entry_key = tk.Entry(frame_middle, width=40, font=("Arial", 12))
entry_key.grid(row=1, column=1, padx=10)

# Input Ciphertext
tk.Label(frame_middle, text="Ciphertext:", bg="#f7f7f7", font=("Arial", 12)).grid(row=2, column=0, sticky="w")
entry_ciphertext = tk.Entry(frame_middle, width=40, font=("Arial", 12))
entry_ciphertext.grid(row=2, column=1, padx=10)

# Tombol untuk enkripsi dan dekripsi
frame_bottom = tk.Frame(root, bg="#f7f7f7")
frame_bottom.pack(pady=20)

button_encrypt = tk.Button(frame_bottom, text="Enkripsi", command=encrypt_text, bg="#ff8c00", fg="white", font=("Arial", 10, "bold"), width=10, height=1)
button_encrypt.grid(row=0, column=0, padx=15)

button_decrypt = tk.Button(frame_bottom, text="Dekripsi", command=decrypt_text, bg="#ff6347", fg="white", font=("Arial", 10, "bold"), width=10, height=1)
button_decrypt.grid(row=0, column=1, padx=15)

# Menjalankan aplikasi
root.mainloop()
