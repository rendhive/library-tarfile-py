import tarfile

with tarfile.open('compressed_archive.tar.gz', 'r:gz') as tar:
    tar.extractall('extracted_compressed')
print("Semua file dari TAR terkompresi diekstrak ke 'extracted_compressed'.")
# Fungsi: Mengekstrak semua file dari file TAR yang terkompresi.
# Kondisi: Ketika Anda ingin mengambil isi dari file TAR terkompresi.
