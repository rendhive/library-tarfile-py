import tarfile

filename = 'archive.tar'

# Memeriksa apakah file adalah tarfile
is_tar = tarfile.is_tarfile(filename)
print(f"Apakah '{filename}' adalah file TAR?:", is_tar)
# Fungsi: Memeriksa apakah file tertentu adalah file TAR.
# Kondisi: Ketika Anda perlu memvalidasi format sebelum melakukan operasi lebih lanjut.
