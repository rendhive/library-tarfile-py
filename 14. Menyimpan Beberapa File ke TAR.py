import tarfile

file_names = ['file1.txt', 'file2.txt']

with tarfile.open('multi_file_archive.tar', 'w') as tar:
    for file in file_names:
        tar.add(file)
print("File-file berhasil disimpan dalam 'multi_file_archive.tar'.")
# Fungsi: Menyimpan beberapa file ke dalam satu arsip TAR.
# Kondisi: Ketika Anda perlu mengarsipkan lebih dari satu file sekaligus.
