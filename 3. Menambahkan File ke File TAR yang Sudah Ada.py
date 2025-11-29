import tarfile

with tarfile.open('archive.tar', 'a') as tar:  # 'a' untuk append
    tar.add('file2.txt')  # Menambahkan file kedua
print("file2.txt berhasil ditambahkan ke 'archive.tar'.")
# Fungsi: Menambahkan file baru ke arsip TAR yang sudah ada.
# Kondisi: Ketika Anda perlu memperbarui arsip TAR dengan file tambahan.
