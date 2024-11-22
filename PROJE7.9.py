from abc import ABC, abstractmethod

class KontrolEdilebilir(ABC):
    
    def ac(self):
        pass

    
    def kapat(self):
        pass

    
    def durum_bilgisi(self):
        pass

class Cihaz(KontrolEdilebilir):
    def __init__(self, isim):
        self.isim = isim
        self.acik = False

    def ac(self):
        self.acik = True
        print(f"{self.isim} açıldı.")

    def kapat(self):
        self.acik = False
        print(f"{self.isim} kapatıldı.")

    def durum_bilgisi(self):
        durum = "açık" if self.acik else "kapalı"
        print(f"{self.isim} durumu: {durum}")


class Klima(Cihaz):
    def __init__(self, isim):
        super().__init__(isim)

class ElektrikFırını(Cihaz):
    def __init__(self, isim):
        super().__init__(isim)
        self.sicaklik = 180  

    def sicaklik_ayarla(self, yeni_sicaklik):
        self.sicaklik = yeni_sicaklik
        print(f"{self.isim} sıcaklığı {self.sicaklik}°C olarak ayarlandı.")

class AlarmSistemi(Cihaz):
    def __init__(self, isim):
        super().__init__(isim)
        self.alarm_aktif = False

    def alarm_tetikle(self):
        self.alarm_aktif = True
        print(f"{self.isim} alarmı tetiklendi!")

    def alarm_sifirla(self):
        self.alarm_aktif = False
        print(f"{self.isim} alarmı sıfırlandı.")


class AkıllıEv:
    def __init__(self):
        self.cihazlar = []

    def cihaz_ekle(self, cihaz):
        self.cihazlar.append(cihaz)

    def cihazlari_kontrol_et(self):
        while True:
            print("\nCihazlar:")
            for i, cihaz in enumerate(self.cihazlar):
                print(f"{i + 1}. {cihaz.isim}")

            secim = input("Bir cihazı kontrol etmek için numarasını seçin (çıkmak için 'q'): ")
            if secim == 'q':
                break

            try:
                cihaz = self.cihazlar[int(secim) - 1]
            except (IndexError, ValueError):
                print("Geçersiz seçim. Lütfen tekrar deneyin.")
                continue

            islem = input("Yapmak istediğiniz işlemi seçin (aç/kapat/durum/sıcaklık/alarm): ").lower()
            if islem == "aç":
                cihaz.ac()
            elif islem == "kapat":
                cihaz.kapat()
            elif islem == "durum":
                cihaz.durum_bilgisi()
            elif isinstance(cihaz, ElektrikFırını) and islem == "sıcaklık":
                yeni_sicaklik = int(input("Yeni sıcaklığı girin: "))
                cihaz.sicaklik_ayarla(yeni_sicaklik)
            elif isinstance(cihaz, AlarmSistemi) and islem == "alarm":
                alarm_islem = input("Alarmı tetiklemek için 'tetik', sıfırlamak için 'sıfırla' yazın: ").lower()
                if alarm_islem == "tetik":
                    cihaz.alarm_tetikle()
                elif alarm_islem == "sıfırla":
                    cihaz.alarm_sifirla()
            else:
                print("Bu işlem bu cihaz için geçerli değil.")


if __name__ == "__main__":
    akilli_ev = AkıllıEv()

    # Yeni cihazlar
    akilli_ev.cihaz_ekle(Klima("Yatak Odası Klima"))
    akilli_ev.cihaz_ekle(ElektrikFırını("Mutfak Fırını"))
    akilli_ev.cihaz_ekle(AlarmSistemi("Ev Alarm Sistemi"))

    # Cihazları kontrol et
    akilli_ev.cihazlari_kontrol_et()
