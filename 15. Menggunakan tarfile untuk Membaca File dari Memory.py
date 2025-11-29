import tarfile
from io import BytesIO

# Membuat arsip tar di memory
tar_buffer = BytesIO()
with tarfile.open(fileobj=tar_buffer, mode='w') as tar:
    tar.writestr('in_memory_file.txt', 'Konten yang ada di memori.')

# Membaca kembali data dari buffer
tar_buffer.seek(0)  # Reset ke awal buffer
with tarfile.open(fileobj=tar_buffer, mode='r') as tar:
    content = tar.extractfile('in_memory_file.txt').read()
    print("Konten dari file:", content.decode())
# Fungsi: Membuat dan membaca file TAR langsung dari memory tanpa menyimpannya ke disk.
# Kondisi: Ketika Anda ingin bekerja dengan file TAR dalam aplikasi yang tidak membutuhkan penyimpanan fisik.
