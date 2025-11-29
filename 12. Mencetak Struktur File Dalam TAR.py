import tarfile

with tarfile.open('archive.tar', 'r') as tar:
    print("Struktur file dalam TAR:")
    tar.printdir()
# Fungsi: Mencetak daftar file dan direktori dalam arsip TAR.
# Kondisi: Ketika Anda ingin melihat struktur lengkap dari file TAR secara langsung.
