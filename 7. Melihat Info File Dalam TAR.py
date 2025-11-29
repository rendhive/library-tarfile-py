import tarfile

with tarfile.open('archive.tar', 'r') as tar:
    file_info = tar.getinfo('file1.txt')
    print("Informasi file:", file_info)
# Fungsi: Mendapatkan informasi seperti ukuran file, tanggal, dll.
# Kondisi: Ketika Anda ingin mendapatkan detail spesifik tentang file dalam TAR.
