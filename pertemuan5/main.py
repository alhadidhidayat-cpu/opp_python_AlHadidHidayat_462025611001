class AbsensiDigital:
    def __init__(self, nama, id_pengguna, pin):
        self.__nama = nama
        self.__id_pengguna = id_pengguna
        self.__pin = pin
        self.__log_kehadiran = [] 

    def get_nama(self):
        return self.__nama

    def get_id(self):
        return self.__id_pengguna

    def catat_kehadiran(self, pin_input, jam_masuk):
        print(f"\n[Sistem] Mencoba mencatat kehadiran untuk: {self.__nama}")
    
        if pin_input == self.__pin:
            self.__log_kehadiran.append(jam_masuk)
            print("Verifikasi Berhasil: Kehadiran telah dicatat.")
        else:
            print("Verifikasi Gagal: PIN salah. Akses ditolak!")

    def lihat_riwayat(self, pin_input):
        if pin_input == self.__pin:
            return f"Riwayat Absensi {self.__nama}: {self.__log_kehadiran}"
        else:
            return "Akses Dilarang: PIN salah untuk melihat riwayat."


karyawan1 = AbsensiDigital("Aris Setiawan", "EMP-001", "1234")


print(f"Nama Karyawan: {karyawan1.get_nama()}")
print(f"ID Karyawan  : {karyawan1.get_id()}")

karyawan1.catat_kehadiran("9999", "08:00 WIB")

karyawan1.catat_kehadiran("1234", "07:55 WIB")

print("-" * 30)
print(karyawan1.lihat_riwayat("1234"))