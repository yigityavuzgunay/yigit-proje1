class Katilimci:
    def __init__(self, isim, yillar):
        self.isim = isim
        self.yillar = yillar

    def bilgileri_goster(self):
        return f"İsim: {self.isim}, Yıllar: {self.yillar}"

class Yarismaci(Katilimci):
    def __init__(self, isim, yillar, katilimci_numarasi):
        super().__init__(isim, yillar)
        self.katilimci_numarasi = katilimci_numarasi

    def bilgileri_goster(self):
        return f"{super().bilgileri_goster()}, Katılımcı Numarası: {self.katilimci_numarasi}"

class Hakem(Katilimci):
    def __init__(self, isim, yillar, uzmanlik_alani):
        super().__init__(isim, yillar)
        self.uzmanlik_alani = uzmanlik_alani

    def bilgileri_goster(self):
        return f"{super().bilgileri_goster()}, Uzmanlık Alanı: {self.uzmanlik_alani}"

# Örnek Kullanım
yarismaci = Yarismaci("Ahmet", 30, "Y98765")
hakem = Hakem("Zeynep", 45, "Performans Değerlendirme")

print(yarismaci.bilgileri_goster())
print(hakem.bilgileri_goster())
