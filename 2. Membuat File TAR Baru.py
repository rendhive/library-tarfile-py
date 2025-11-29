import tarfile

with tarfile.open('archive.tar', 'w') as tar:
    tar.add('file1.txt')  # Menambahkan file ke dalam arsip TAR
print("File TAR 'archive.tar' berhasil dibuat.")
# Fungsi: Membuat arsip TAR baru dan menambahkan file ke dalamnya.
# Kondisi: Ketika Anda ingin mengarsipkan beberapa file ke dalam format TAR.
