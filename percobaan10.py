import cv2
img = cv2.imread('tts1.png', cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(img, 100, 200)
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
result = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.drawContours(result, contours, -1, (0, 255, 0), 2)
cv2.imwrite('contours.jpg', result)

# import cv2

# # Baca gambar dalam skala abu-abu
# img = cv2.imread('tts1.png', cv2.IMREAD_GRAYSCALE)

# # Deteksi tepi menggunakan Canny
# edges = cv2.Canny(img, 100, 200)

# # Temukan kontur
# contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# # Konversi gambar ke format BGR untuk menggambar kontur berwarna
# result = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# # Ambang area minimum untuk menyaring kontur kecil
# min_area = 100

# # Iterasi melalui kontur dan gambar hanya kontur besar
# font = cv2.FONT_HERSHEY_SIMPLEX
# for i, contour in enumerate(contours):
#     area = cv2.contourArea(contour)
#     if area > min_area:
#         # Gambar kontur
#         cv2.drawContours(result, [contour], -1, (0, 255, 0), 2)

#         # Hitung perimeter
#         perimeter = cv2.arcLength(contour, True)

#         # Temukan pusat massa (centroid)
#         M = cv2.moments(contour)
#         if M['m00'] != 0:
#             cx = int(M['m10'] / M['m00'])
#             cy = int(M['m01'] / M['m00'])
#         else:
#             cx, cy = 0, 0

#         # Tambahkan label dengan area dan perimeter
#         label = f"#{i} A:{int(area)} P:{int(perimeter)}"
#         cv2.putText(result, label, (cx - 50, cy - 10), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)

# # Simpan gambar hasil
# cv2.imwrite('contours_annotated.jpg', result)
