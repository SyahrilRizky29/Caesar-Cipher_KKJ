import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib

def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()

def hash_file(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            sha256.update(block)
    return sha256.hexdigest()

def browse_file():
    filename = filedialog.askopenfilename()
    if filename:
        entry_file.delete(0, tk.END)
        entry_file.insert(0, filename)

def action_hash():
    pilihan = var_choice.get()
    if pilihan == "text":
        teks = text_input.get("1.0", tk.END).strip()
        if not teks:
            messagebox.showerror("Error", "Masukkan teks terlebih dahulu.")
            return
        hasil = hash_text(teks)
        output_var.set(hasil)
    else:
        path = entry_file.get()
        if not path:
            messagebox.showerror("Error", "Pilih file terlebih dahulu.")
            return
        try:
            hasil = hash_file(path)
            output_var.set(hasil)
        except FileNotFoundError:
            messagebox.showerror("Error", "File tidak ditemukan.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal hashing file:\n{e}")

root = tk.Tk()
root.title("Hashing SHA-256")

var_choice = tk.StringVar(value="text")

rb_text = tk.Radiobutton(root, text="Hash Teks", variable=var_choice, value="text")
rb_text.grid(row=0, column=0, sticky="w", padx=5, pady=5)

rb_file = tk.Radiobutton(root, text="Hash File", variable=var_choice, value="file")
rb_file.grid(row=0, column=1, sticky="w", padx=5, pady=5)

text_input = tk.Text(root, width=40, height=5)
text_input.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

entry_file = tk.Entry(root, width=40)
entry_file.grid(row=2, column=0, padx=5, pady=5)

btn_browse = tk.Button(root, text="Browse File", command=browse_file)
btn_browse.grid(row=2, column=1, padx=5, pady=5)

btn_hash = tk.Button(root, text="Hitung Hash", command=action_hash)
btn_hash.grid(row=3, column=0, columnspan=2, pady=10)

output_var = tk.StringVar()
tk.Label(root, text="Hasil SHA-256:").grid(row=4, column=0, sticky="w", padx=5)
entry_output = tk.Entry(root, textvariable=output_var, width=60, state="readonly")
entry_output.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

def toggle_widgets(*args):
    if var_choice.get() == "text":
        text_input.config(state="normal")
        entry_file.config(state="disabled")
        btn_browse.config(state="disabled")
    else:
        text_input.config(state="disabled")
        entry_file.config(state="normal")
        btn_browse.config(state="normal")

var_choice.trace_add("write", toggle_widgets)
toggle_widgets()

root.mainloop()
