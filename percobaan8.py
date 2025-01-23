import os
from PIL import Image
import cv2  # Untuk mengambil gambar dari kamera

def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
    1253656 => '1.20MB'
    1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"

def compress_img(image_name, new_size_ratio=0.9, quality=90, width=None, height=None, to_jpg=True):
    # Load the image to memory
    img = Image.open(image_name)

    # Print the original image shape
    print("[*] Image shape:", img.size)

    # Get the original image size in bytes
    image_size = os.path.getsize(image_name)

    # Print the size before compression/resizing
    print("[*] Size before compression:", get_size_format(image_size))

    if new_size_ratio < 1.0:
        # If resizing ratio is below 1.0, then multiply width & height with this ratio to reduce image size
        img = img.resize((int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)), Image.Resampling.LANCZOS)
        # Print new image shape
        print("[+] New Image shape:", img.size)
    elif width and height:
        # If width and height are set, resize with them instead
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        # Print new image shape
        print("[+] New Image shape:", img.size)

    # Split the filename and extension
    filename, ext = os.path.splitext(image_name)

    # Make new filename appending _compressed to the original file name
    if to_jpg:
        # Change the extension to JPEG
        new_filename = f"{filename}_compressed.jpg"
    else:
        # Retain the same extension of the original image
        new_filename = f"{filename}_compressed{ext}"

    try:
        # Save the image with the corresponding quality and optimize set to True
        img.save(new_filename, quality=quality, optimize=True)
    except OSError:
        # Convert the image to RGB mode first
        img = img.convert("RGB")
        # Save the image with the corresponding quality and optimize set to True
        img.save(new_filename, quality=quality, optimize=True)

    print("[+] New file saved:", new_filename)

    # Get the new image size in bytes
    new_image_size = os.path.getsize(new_filename)

    # Print the new size in a good format
    print("[+] Size after compression:", get_size_format(new_image_size))

    # Calculate the saving bytes
    saving_diff = new_image_size - image_size

    # Print the saving percentage
    print(f"[+] Image size change: {saving_diff / image_size * 100:.2f}% of the original image size.")


if __name__ == "__main__":
    # Capture an image from the camera
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Error: Unable to access the camera.")
        exit()

    print("Press 'Space' to capture the image or 'ESC' to exit.")
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Error: Failed to capture the frame.")
            break

        # Display the camera feed
        cv2.imshow("Camera", frame)

        # Wait for key press
        key = cv2.waitKey(1) & 0xFF

        if key == 27:  # ESC key to exit
            print("Exiting...")
            break
        elif key == 32:  # Space key to capture
            image_path = "captured_image.jpg"
            cv2.imwrite(image_path, frame)
            print(f"Image captured and saved to {image_path}")
            break

    camera.release()
    cv2.destroyAllWindows()

    # Compress the captured image
    compress_img(image_path, new_size_ratio=0.8, quality=85, to_jpg=True)
