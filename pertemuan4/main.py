class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def __str__(self):
        return f"Produk: {self.nama} | Harga: Rp{self.harga:,}"

    def __eq__(self, other):
        if isinstance(other, Produk):
            return self.harga == other.harga
        return False

    def __lt__(self, other):
        if isinstance(other, Produk):
            return self.harga < other.harga
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Produk):
            return self.harga > other.harga
        return NotImplemented


produk1 = Produk("Kaos Oversize", 150000)
produk2 = Produk("Celana Cargo", 250000)
produk3 = Produk("Hoodie Gorpcore", 250000)

print("=== Daftar Produk ===")
print(produk1)
print(produk2)
print(produk3)
print("-" * 30)

print("=== Hasil Perbandingan Harga ===")

print(f"Apakah {produk1.nama} < {produk2.nama}? {produk1 < produk2}")

print(f"Apakah {produk2.nama} > {produk1.nama}? {produk2 > produk1}")

print(f"Apakah harga {produk2.nama} sama dengan {produk3.nama}? {produk2 == produk3}")