import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt

def calculate_psnr(original, compressed):
    if original is None or compressed is None:
        raise ValueError("Salah satu gambar tidak valid. Pastikan file tersedia dan dapat dibaca.")
    mse = np.mean((original - compressed) ** 2)
    if mse == 0:
        return 100
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

# Membaca gambar
original = cv2.imread(r'C:\Users\rahma\Desktop\uas pratikum pengolahan citra\captured_image.jpg', cv2.IMREAD_GRAYSCALE)
compressed = cv2.imread(r'C:\Users\rahma\Desktop\uas pratikum pengolahan citra\captured_image_compressed.jpg', cv2.IMREAD_GRAYSCALE)

# Validasi gambar
if original is not None and compressed is not None:
    # Resize the 'compressed' image to match the dimensions of the 'original' image
    compressed_resized = cv2.resize(compressed, (original.shape[1], original.shape[0]))

    # Perhitungan PSNR dan SSIM
    psnr_value = calculate_psnr(original, compressed_resized)
    # Calculate SSIM using the resized image
    ssim_value = ssim(original, compressed_resized)

    # Menampilkan hasil PSNR dan SSIM
    print(f"PSNR: {psnr_value:.2f} dB")
    print(f"SSIM: {ssim_value:.2f}")

    # Menampilkan gambar menggunakan matplotlib
    plt.figure(figsize=(10, 5))

    # Gambar asli
    plt.subplot(1, 2, 1)
    plt.imshow(original, cmap='gray')
    plt.title('Gambar Asli')
    plt.axis('off')

    # Gambar terkompresi
    plt.subplot(1, 2, 2)
    plt.imshow(compressed_resized, cmap='gray')
    plt.title('Gambar Terkompresi')
    plt.axis('off')

    # Menampilkan plot
    plt.tight_layout()
    plt.show()
else:
    print("Error: Tidak dapat memuat salah satu atau kedua gambar.")
