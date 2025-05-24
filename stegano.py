# steganografi.py

from PIL import Image

def encode(image_path, message, output_path):
    img = Image.open(image_path)
    binary_msg = ''.join(format(ord(c), '08b') for c in message) + '11111110'  # Delimiter

    pixels = img.load()
    width, height = img.size
    idx = 0

    for y in range(height):
        for x in range(width):
            if idx < len(binary_msg):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary_msg[idx])
                idx += 1
                if idx < len(binary_msg):
                    g = (g & ~1) | int(binary_msg[idx])
                    idx += 1
                if idx < len(binary_msg):
                    b = (b & ~1) | int(binary_msg[idx])
                    idx += 1
                pixels[x, y] = (r, g, b)
            else:
                img.save(output_path)
                return True
    img.save(output_path)
    return True

def decode(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    binary_msg = ""
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_msg += str(r & 1)
            binary_msg += str(g & 1)
            binary_msg += str(b & 1)

    all_bytes = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    message = ""
    for byte in all_bytes:
        if byte == '11111110':  # delimiter
            break
        message += chr(int(byte, 2))
    return message

if __name__ == "__main__":
    pilih = input("Pilih (1) encode atau (2) decode: ")
    if pilih == '1':
        img_path = input("Masukkan path gambar PNG: ")
        pesan = input("Masukkan pesan yang ingin disisipkan: ")
        out_path = input("Masukkan nama file output (misal: out.png): ")
        if encode(img_path, pesan, out_path):
            print(f"Pesan berhasil disisipkan ke {out_path}")
    elif pilih == '2':
        img_path = input("Masukkan path gambar PNG yang sudah disisipi pesan: ")
        hasil = decode(img_path)
        print("Pesan tersembunyi:", hasil)
    else:
        print("Pilihan tidak valid.")
