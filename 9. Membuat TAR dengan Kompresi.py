import tarfile

with tarfile.open('compressed_archive.tar.gz', 'w:gz') as tar:  # Kompresi gzip
    tar.add('file1.txt')
print("File TAR terkompresi telah dibuat.")
# Fungsi: Menggunakan kompresi untuk menghasilkan file TAR.
# Kondisi: Ketika Anda ingin mengurangi ukuran file dengan kompresi.
