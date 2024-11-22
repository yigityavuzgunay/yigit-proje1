import random
from abc import ABC, abstractmethod

# Soyut Sınıflar
class Katilimci(ABC):
    def __init__(self, isim):
        self.isim = isim
        self.puan = 0

    @abstractmethod
    def hamle_yap(self):
        pass

class BilgisayarKatilimci(ABC):
    def __init__(self):
        pass

# Somut Sınıflar
class InsanKatilimci(Katilimci):
    def hamle_yap(self):
        hamle = input("Ay, Gök, veya Deniz seçin: ").lower()
        while hamle not in ['ay', 'gök', 'deniz']:
            hamle = input("Geçersiz seçim! Ay, Gök, veya Deniz seçin: ").lower()
        return hamle

class RastgeleBilgisayarKatilimci(BilgisayarKatilimci):
    def hamle_yap(self):
        return random.choice(['ay', 'gök', 'deniz'])

# Yarışma Mantığı
class Yarisma:
    def __init__(self):
        self.insan_katilimci = None
        self.bilgisayar_katilimci = RastgeleBilgisayarKatilimci()
        self.gecmis = []

    def kazanan_belirle(self, insan_hamle, bilgisayar_hamle):
        if insan_hamle == bilgisayar_hamle:
            return None  # Beraberlik
        elif (insan_hamle == 'ay' and bilgisayar_hamle == 'deniz') or \
             (insan_hamle == 'gök' and bilgisayar_hamle == 'ay') or \
             (insan_hamle == 'deniz' and bilgisayar_hamle == 'gök'):
            return self.insan_katilimci
        else:
            return self.bilgisayar_katilimci

    def oynat(self):
        insan_isim = input("Katilimcinin adını girin: ")
        self.insan_katilimci = InsanKatilimci(insan_isim)

        while True:
            insan_hamle = self.insan_katilimci.hamle_yap()
            bilgisayar_hamle = self.bilgisayar_katilimci.hamle_yap()

            print(f"{self.insan_katilimci.isim} seçimi: {insan_hamle}")
            print(f"Bilgisayar seçimi: {bilgisayar_hamle}")

            kazanan = self.kazanan_belirle(insan_hamle, bilgisayar_hamle)

            if kazanan is None:
                print("Sonuç: Beraberlik!")
            elif kazanan == self.insan_katilimci:
                print(f"Sonuç: {self.insan_katilimci.isim} kazandı!")
                self.insan_katilimci.puan += 1
            else:
                print("Sonuç: Bilgisayar kazandı!")
                self.bilgisayar_katilimci.puan += 1

            self.gecmis.append((self.insan_katilimci.isim, insan_hamle, "Bilgisayar", bilgisayar_hamle))

            print(f"{self.insan_katilimci.isim} Puanı: {self.insan_katilimci.puan}, Bilgisayar Puanı: {self.bilgisayar_katilimci.puan}")

            devam = input("Devam etmek istiyor musunuz? (E/H): ").lower()
            if devam != 'e':
                break

        print("\nYarışma Geçmişi:")
        for kayit in self.gecmis:
            print(f"{kayit[0]}: {kayit[1]} - {kayit[2]}: {kayit[3]}")

# Yarışma başlatma
if __name__ == "__main__":
    yarisma = Yarisma()
    yarisma.oynat()
