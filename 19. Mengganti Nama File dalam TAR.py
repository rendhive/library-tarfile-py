import tarfile

with tarfile.open('archive.tar', 'r') as tar:
    member = tar.getmember('file1.txt')
    member.name = 'new_file_name.txt'  # Mengganti nama filenya

    with tarfile.open('updated_archive.tar', 'w') as new_tar:
        new_tar.addfile(member, tar.extractfile('file1.txt'))
print("File dalam TAR telah diubah namanya.")
# Fungsi: Mengganti nama file dalam arsip TAR dengan membuat arsip baru.
# Kondisi: Ketika Anda ingin membuat arsip baru dengan file yang sudah dinamai ulang.
