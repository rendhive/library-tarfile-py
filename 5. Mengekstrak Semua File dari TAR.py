import tarfile

with tarfile.open('archive.tar', 'r') as tar:
    tar.extractall('extracted_files')  # Mengekstrak semua ke direktori tertentu
print("Semua file berhasil diekstrak ke dalam folder 'extracted_files'.")
# Fungsi: Mengekstrak semua file dari arsip TAR ke direktori tertentu.
# Kondisi: Ketika Anda ingin mendekompresi semua isi dari TAR ke lokasi yang diinginkan.
