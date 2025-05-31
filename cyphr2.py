import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox

# Fungsi Caesar Cipher
def enkripsi(teks, geser):
    hasil = ""
    for karakter in teks:
        if karakter.isalpha():
            awal = ord('A') if karakter.isupper() else ord('a')
            hasil += chr((ord(karakter) - awal + geser) % 26 + awal)
        else:
            hasil += karakter
    return hasil

def dekripsi(teks, geser):
    return enkripsi(teks, -geser)

# Fungsi tombol Encrypt
def proses_enkripsi():
    teks = entry_input.get()
    try:
        geser = int(entry_geser.get())
    except ValueError:
        messagebox.showerror("Error", "Nilai geser harus berupa angka.")
        return
    hasil = enkripsi(teks, geser)
    output_var.set(hasil)
    
# Fungsi tombol Decrypt
def proses_dekripsi():
    teks = entry_input.get()
    try:
        geser = int(entry_geser.get())
    except ValueError:
        messagebox.showerror("Error", "Nilai geser harus berupa angka.")
        return
    hasil = dekripsi(teks, geser)
    output_var.set(hasil)

def disable_typing(event):
    # Buat cegah input keyboard di kolom hasil
    return "break"

# Buat Window utama dengan tema modern
root = tb.Window(themename="solar")
root.title("CYPHR")
root.geometry("500x400")
root.iconbitmap("D:/Xampp/htdocs/crypto-project/img/iconfinder.ico")

# Frame utama
main_frame = tb.Frame(root, padding=20)
main_frame.pack(fill=BOTH, expand=True)

judul = tb.Label(
    main_frame,
    text="Caesar Cipher",
    font=("Segoe UI", 18, "bold"),
    bootstyle="info"
)
judul.pack(pady=(0, 20))

# Form input
form_frame = tb.Frame(main_frame)
form_frame.pack(fill=X, pady=10)

tb.Label(form_frame, text="Masukkan Teks:", font=("Segoe UI", 10)).grid(row=0, column=0, sticky=W, padx=5, pady=5)
entry_input = tb.Entry(form_frame, font=("Segoe UI", 11))
entry_input.grid(row=0, column=1, padx=10, pady=5, sticky=EW)

tb.Label(form_frame, text="Nilai Geser:", font=("Segoe UI", 10)).grid(row=1, column=0, sticky=W, padx=5, pady=5)
entry_geser = tb.Spinbox(form_frame, from_=-999, to=999, width=5, font=("Segoe UI", 11))
entry_geser.set(13)
entry_geser.grid(row=1, column=1, padx=10, pady=5, sticky=W)

tb.Label(form_frame, text="Hasil:", font=("Segoe UI", 10)).grid(row=2, column=0, sticky=W, padx=5, pady=10)
output_var = tb.StringVar()
entry_output = tb.Entry(form_frame, textvariable=output_var, font=("Courier New", 11), state="readonly")
entry_output.grid(row=2, column=1, padx=10, pady=10, sticky=EW)

# entry_output.bind("<Key>", disable_typing)

form_frame.columnconfigure(1, weight=1)

# Tombol
button_frame = tb.Frame(main_frame)
button_frame.pack(pady=15)

btn_encrypt = tb.Button(button_frame, text="ENCRYPT", command=proses_enkripsi, bootstyle="primary")
btn_encrypt.pack(side=LEFT, padx=10)

btn_decrypt = tb.Button(button_frame, text="DECRYPT", command=proses_dekripsi, bootstyle="secondary")
btn_decrypt.pack(side=LEFT, padx=10)

# Footer
footer = tb.Label(
    main_frame,
    text="Cryptography",
    font=("Segoe UI", 9),
    bootstyle="secondary"
)
footer.pack(pady=(20, 0))

root.mainloop()