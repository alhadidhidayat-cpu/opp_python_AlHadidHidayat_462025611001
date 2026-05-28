class Kendaraan:
    def __init__(self):
        print("Kendaraan dibuat")

    def info(self):
        print("Ini adalah kendaraan")


class Mobil(Kendaraan):
    def __init__(self):
        super().__init__()
        print("Mobil dibuat")

    def info(self):
        super().info()
        print("Mobil memiliki 4 roda")


class Listrik(Kendaraan):
    def __init__(self):
        super().__init__()
        print("Kendaraan listrik dibuat")

    def info(self):
        super().info()
        print("Menggunakan tenaga listrik")


class MobilListrik(Mobil, Listrik):
    def __init__(self):
        super().__init__()
        print("Mobil listrik dibuat")

    def info(self):
        super().info()
        print("Mobil listrik ramah lingkungan")


print("=== Membuat Objek MobilListrik ===")
objek = MobilListrik()

print("\n=== Menampilkan Info ===")
objek.info()

print("\n=== Method Resolution Order (MRO) ===")
print(MobilListrik.__mro__)