import tarfile

with tarfile.open('archive.tar', 'r') as tar:
    print("File dalam TAR:", tar.getnames())
# Fungsi: Membaca nama-nama file dalam arsip TAR.
# Kondisi: Ketika Anda ingin mengetahui isi file TAR tanpa mengekstraknya.
