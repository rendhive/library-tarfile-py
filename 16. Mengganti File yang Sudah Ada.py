import tarfile

with tarfile.open('replacement_archive.tar', 'w') as tar:
    tar.add('replacement_file.txt')  # File baru untuk mengganti yang lama
print("File berhasil ditambahkan, menggantikan yang lama.")
# Fungsi: Mengganti file yang sudah ada dengan menambahkan file baru.
# Kondisi: Ketika Anda ingin memperbarui konten tanpa perlu membuat arsip baru sepenuhnya.
