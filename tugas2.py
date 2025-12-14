from PIL import Image
import shutil
import os

INPUT_FILE = "image.png"

if not os.path.exists(INPUT_FILE):
    print(" File gambar tidak ditemukan:", INPUT_FILE)
    exit()


try:
    img = Image.open(INPUT_FILE)
    print(" Gambar berhasil dibuka")
except Exception as e:
    print(" ERROR membuka gambar:", e)
    exit()


try:
    resized_img = img.resize((200, 200))
    resized_img.save("resized_image.jpg")
    print(" Gambar berhasil di-resize menjadi 200x200 → resized_image.jpg")
except Exception as e:
    print(" ERROR saat resize:", e)
    exit()


try:
    if os.path.exists("copied_image.jpg"):
        os.remove("copied_image.jpg")   # hapus jika ada file lama
    shutil.copy("resized_image.jpg", "copied_image.jpg")
    print(" File berhasil disalin → copied_image.jpg")
except Exception as e:
    print(" ERROR saat copy:", e)
    exit()


try:
    if not os.path.exists("output"):
        os.makedirs("output")

    # hapus file lama jika ada
    output_copy = "output/copied_image.jpg"
    if os.path.exists(output_copy):
        os.remove(output_copy)

    shutil.move("copied_image.jpg", output_copy)
    print(" copied_image.jpg berhasil dipindahkan ke folder /output")
except Exception as e:
    print(" ERROR saat move:", e)
    exit()


try:
    converted_img = Image.open(output_copy)
    converted_img.save("output/image_converted.png")
    print(" Berhasil convert JPG → PNG → image_converted.png")
except Exception as e:
    print(" ERROR saat convert:", e)
    exit()

print("\n=== SELURUH PROSES BERHASIL ===")
