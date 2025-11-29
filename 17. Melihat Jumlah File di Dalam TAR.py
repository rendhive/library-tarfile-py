import tarfile

with tarfile.open('archive.tar', 'r') as tar:
    file_count = len(tar.getmembers())
print("Jumlah file dalam TAR:", file_count)
# Fungsi: Menghitung jumlah file yang ada di dalam arsip TAR.
# Kondisi: Ketika Anda ingin mendapatkan ringkasan isi arsip tanpa perlu melihat detailnya.
