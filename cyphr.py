import tkinter as tk
from tkinter import ttk, messagebox

# Buat Fungsi Caesar Cipher
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

def proses_enkripsi():
    teks = entry_input.get()
    try:
        geser = int(entry_geser.get())
    except ValueError:
        messagebox.showerror("Error", "Nilai geser harus berupa angka.")
        return
    hasil = enkripsi(teks, geser)
    output_var.set(hasil)

def proses_dekripsi():
    teks = entry_input.get()
    try:
        geser = int(entry_geser.get())
    except ValueError:
        messagebox.showerror("Error", "Nilai geser harus berupa angka.")
        return
    hasil = dekripsi(teks, geser)
    output_var.set(hasil)

# Buat GUI nya
root = tk.Tk()
root.title("CYPHR")
root.minsize(480, 380)
root.resizable(True, True)
root.configure(bg="#2c3e50")

# Buat atur warna tema
warna_latar = "#2c3e50"
warna_teks = "#ecf0f1"
warna_aksen = "#3498db"
warna_hover = "#2980b9"

root.iconbitmap("D:/Xampp/htdocs/crypto-project/img/iconfinder.ico")

# Style
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Rounded.TButton",
    foreground="white",
    background=warna_aksen,
    font=("Arial", 10, "bold"),
    padding=6,
    borderwidth=0,
    relief="flat"
)

style.map(
    "Rounded.TButton",
    background=[("active", warna_hover)]
)

# Frame utamanya
main_frame = tk.Frame(root, bg=warna_latar, padx=30, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

label_judul = tk.Label(
    main_frame,
    text="Caesar Cipher",
    font=("Arial", 16, "bold"),
    fg=warna_aksen,
    bg=warna_latar
)
label_judul.pack(pady=(0, 25))

# Untuk Form Input
form_frame = tk.Frame(main_frame, bg=warna_latar)
form_frame.pack()

form_frame.columnconfigure(1, weight=1)

label_width = 15

label_input = tk.Label(
    form_frame,
    text="Masukkan Teks:",
    font=("Arial", 10),
    fg=warna_teks,
    bg=warna_latar,
    width=label_width,
    anchor="w"
)
label_input.grid(row=0, column=0, sticky="w", padx=5, pady=8)

entry_input = ttk.Entry(form_frame, font=("Arial", 11))
entry_input.grid(row=0, column=1, padx=10, pady=8, sticky="ew")

label_geser = tk.Label(
    form_frame,
    text="Nilai Geser:",
    font=("Arial", 10),
    fg=warna_teks,
    bg=warna_latar,
    width=label_width,
    anchor="w"
)
label_geser.grid(row=1, column=0, sticky="w", padx=5, pady=8)

entry_geser = ttk.Spinbox(
    form_frame,
    from_=0,
    to=25,
    width=6,
    font=("Arial", 11),
    justify="center"
)
entry_geser.set(13)
entry_geser.grid(row=1, column=1, padx=10, pady=8, sticky="w")

label_output = tk.Label(
    form_frame,
    text="Hasil:",
    font=("Arial", 10),
    fg=warna_teks,
    bg=warna_latar,
    width=label_width,
    anchor="w"
)
label_output.grid(row=2, column=0, sticky="w", padx=5, pady=(15, 8))

output_var = tk.StringVar()
entry_output = ttk.Entry(
    form_frame,
    textvariable=output_var,
    font=("Courier New", 11),
    state="readonly"
)
entry_output.grid(row=2, column=1, padx=10, pady=(15, 8), sticky="ew")

# Buat Tombol
button_frame = tk.Frame(main_frame, bg=warna_latar)
button_frame.pack(pady=20)

btn_encrypt = ttk.Button(
    button_frame,
    text="ENCRYPT",
    command=proses_enkripsi,
    style="Rounded.TButton"
)
btn_encrypt.pack(side=tk.LEFT, padx=15)

btn_decrypt = ttk.Button(
    button_frame,
    text="DECRYPT",
    command=proses_dekripsi,
    style="Rounded.TButton"
)
btn_decrypt.pack(side=tk.LEFT, padx=15)

# Footer
footer = tk.Label(
    main_frame,
    text="Cryptography",
    font=("Arial", 9),
    fg=warna_teks,
    bg=warna_latar
)
footer.pack(pady=(15, 0))

root.mainloop()