import tarfile

with tarfile.open('archive.tar', 'r') as tar:
    tar.extract('file1.txt', 'extracted_files')  # Mengekstrak hanya file1.txt
print("file1.txt berhasil diekstrak.")
# Fungsi: Mengekstrak file tertentu dari arsip TAR.
# Kondisi: Ketika Anda hanya ingin mendapatkan file tertentu dari TAR.
