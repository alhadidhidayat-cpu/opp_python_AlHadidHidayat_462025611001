class Karyawan:
    def __init__(self, nama, jabatan, gaji_pokok):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji_pokok = gaji_pokok
        self.bonus = 0


    def tampilkan_profil(self):
        """Menampilkan informasi detail karyawan."""
        print(f"Nama     : {self.nama}")
        print(f"Jabatan  : {self.jabatan}")
        print(f"Total Gaji: Rp{self.gaji_pokok + self.bonus:,}")
        print("-" * 30)

    def tambah_bonus(self, persentase):
        """Menghitung dan menambahkan bonus berdasarkan persentase dari gaji pokok."""
        self.bonus = self.gaji_pokok * (persentase / 100)
        print(f"Berhasil menambahkan bonus {persentase}% untuk {self.nama}.")

    @staticmethod
    def sapaan_perusahaan():
        """Fungsi umum yang tidak bergantung pada data objek individu."""
        return "Selamat datang di PT. Maju Jaya! Integritas dan Inovasi adalah prioritas kami."



karyawan1 = Karyawan("Andi", "Software Engineer", 8000000)
karyawan2 = Karyawan("Budi", "Project Manager", 12000000)

print("=== PROGRAM MANAJEMEN KARYAWAN ===\n")

print(Karyawan.sapaan_perusahaan())
print("\n")

karyawan1.tambah_bonus(10)
karyawan1.tampilkan_profil()

karyawan2.tambah_bonus(15)
karyawan2.tampilkan_profil()

print("Pesan Penutup:")
print(karyawan1.sapaan_perusahaan())