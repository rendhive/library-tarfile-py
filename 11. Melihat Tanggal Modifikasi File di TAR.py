import tarfile

with tarfile.open('archive.tar', 'r') as tar:
    for member in tar.getmembers():
        print(f"File: {member.name}, Diperbarui pada: {member.mtime}")
# Fungsi: Mencetak tanggal modifikasi untuk semua file dalam file TAR.
# Kondisi: Ketika Anda perlu mengetahui kapan file diarsipkan.
