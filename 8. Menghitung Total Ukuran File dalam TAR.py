import tarfile

with tarfile.open('archive.tar', 'r') as tar:
    total_size = sum(member.size for member in tar.getmembers())
print("Total ukuran file dalam TAR:", total_size, "bytes")
# Fungsi: Menghitung total ukuran semua file dalam arsip TAR.
# Kondisi: Ketika Anda perlu mengetahui seberapa besar arsip TAR.
