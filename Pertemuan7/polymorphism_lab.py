class Hewan:
    def bersuara(self):
        print("Hewan mengeluarkan suara")


class Kucing(Hewan):
    def bersuara(self):
        print("Meong...")


class Anjing(Hewan):
    def bersuara(self):
        print("Guk guk...")


class Burung(Hewan):
    def bersuara(self):
        print("Cuit cuit...")


def dengarkan_suara(objek):
    objek.bersuara()


dengarkan_suara(Kucing())
dengarkan_suara(Anjing())
dengarkan_suara(Burung())