import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def proses_encrypt():
    teks = entry_input.get()
    try:
        geser = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Error", "Shift harus berupa angka.")
        return
    hasil = encrypt(teks, geser)
    output_var.set(hasil)

def proses_decrypt():
    teks = entry_input.get()
    try:
        geser = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Error", "Shift harus berupa angka.")
        return
    hasil = decrypt(teks, geser)
    output_var.set(hasil)

root = tk.Tk()
root.title("Kriptografi Caesar Cipher")

tk.Label(root, text="Masukkan teks:").grid(row=0, column=0, sticky="w")
entry_input = tk.Entry(root, width=40)
entry_input.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Jumlah shift:").grid(row=1, column=0, sticky="w")
entry_shift = tk.Entry(root, width=10)
entry_shift.grid(row=1, column=1, sticky="w", padx=10, pady=5)

btn_encrypt = tk.Button(root, text="Encrypt", command=proses_encrypt)
btn_encrypt.grid(row=2, column=0, pady=10)

btn_decrypt = tk.Button(root, text="Decrypt", command=proses_decrypt)
btn_decrypt.grid(row=2, column=1, pady=10)

output_var = tk.StringVar()
tk.Label(root, text="Hasil:").grid(row=3, column=0, sticky="w")
entry_output = tk.Entry(root, textvariable=output_var, width=40, state="readonly")
entry_output.grid(row=3, column=1, padx=10, pady=5)

root.mainloop()