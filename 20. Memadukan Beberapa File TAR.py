import tarfile

file_tars = ['archive1.tar', 'archive2.tar']
with tarfile.open('combined_archive.tar', 'w') as new_tar:
    for file_tar in file_tars:
        with tarfile.open(file_tar, 'r') as tar:
            for member in tar.getmembers():
                new_tar.addfile(member, tar.extractfile(member.name))
print("Beberapa arsip tar berhasil digabungkan ke dalam 'combined_archive.tar'.")
# Fungsi: Menggabungkan beberapa file TAR ke dalam satu arsip TAR.
# Kondisi: Ketika Anda ingin mengombinasikan beberapa arsip untuk pengarsipan yang lebih rapi.
