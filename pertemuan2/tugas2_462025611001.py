class Kamera:
    def __init__(self, merk, model, resolusi):
        self.merk = merk
        self.model = model
        self.resolusi = resolusi
        self.is_on = False 

    def tekan_tombol_power(self):
        self.is_on = not self.is_on
        status = "Menyala" if self.is_on else "Mati"
        print(f"Kamera {self.merk} {self.model} sekarang {status}.")

    def ambil_gambar(self):
        if self.is_on:
            print(f"Cekrek! Mengambil gambar dengan resolusi {self.resolusi}MP.")
        else:
            print("Gagal! Nyalakan kamera terlebih dahulu.")


kamera_pro = Kamera("Sony", "A7IV", 33)

kamera_vlog = Kamera("DJI", "Osmo Pocket 3", 12)

print(f"--- Menggunakan {kamera_pro.merk} ---")
kamera_pro.tekan_tombol_power()
kamera_pro.ambil_gambar()

print(f"\n--- Menggunakan {kamera_vlog.merk} ---")
kamera_vlog.tekan_tombol_power()
kamera_vlog.ambil_gambar()