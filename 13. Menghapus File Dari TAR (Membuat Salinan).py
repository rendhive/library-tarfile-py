import tarfile
import os

# Menghapus file perlu dilakukan dengan membuat arsip baru tanpa file tersebut
tar_path = 'archive.tar'
file_to_remove = 'file1.txt'
new_tar_path = 'new_archive.tar'

with tarfile.open(tar_path, 'r') as old_tar, \
     tarfile.open(new_tar_path, 'w') as new_tar:
    for member in old_tar.getmembers():
        if member.name != file_to_remove:
            new_tar.add(member, old_tar.extractfile(member.name))
print(f"File '{file_to_remove}' telah dihapus dari '{tar_path}'.")
# Fungsi: Menghapus file dari arsip TAR dengan membuat arsip baru yang tidak menyertakan file tersebut.
# Kondisi: Ketika Anda perlu memperbarui arsip dengan menghapus file tertentu.
