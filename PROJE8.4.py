class Membership:
    members = []  # Tüm üyeler burada saklanır

    def __init__(self, member_id, name, points=0):
        self.__member_id = member_id  # Üye ID'si
        self.__name = name  # Üyenin adı
        self.__points = points  # Başlangıç puanı
        Membership.members.append(self)  # Yeni üyeyi listeye ekle

    def earn_points(self, points):
        if points > 0:
            self.__points += points  # Puan ekle
            Club.log_event(f"{self.__name} {points} puan kazandı.")
            print(f"{points} puan eklendi. Yeni toplam puan: {self.__points}")
        else:
            print("Kazançlı puan sıfırdan büyük olmalıdır.")

    def redeem_points(self, points):
        if points > 0:
            if points <= self.__points:
                self.__points -= points  # Puan kullan
                Club.log_event(f"{self.__name} {points} puan harcadı.")
                print(f"{points} puan harcandı. Kalan puan: {self.__points}")
            else:
                print("Yetersiz puan.")
        else:
            print("Harcanan puan sıfırdan büyük olmalıdır.")

    def show_points(self):
        print(f"Üye Adı: {self.__name}, Üye ID: {self.__member_id}, Toplam Puan: {self.__points}")


class Gym(Club):  # Kulüp sınıfını daha özgün hale getirmek için isminde değişiklik yaptım
    event_log = []  # Etkinlik geçmişi

    @staticmethod
    def display_club_info():
        print("Kulüp Bilgileri:")
        print("Kulüp Adı: FitGym")
        print("Sağlık ve fitness hedeflerinizde size yardımcı olmak için buradayız.")

    @staticmethod
    def log_event(description):
        Gym.event_log.append(description)  # Olayı kaydet

    @staticmethod
    def show_event_log():
        print("Etkinlik Geçmişi:")
        for event in Gym.event_log:
            print(event)


def main():
    while True:
        print("\n--- Üyelik Puan Yönetim Sistemi ---")
        print("1. Üye Kaydet")
        print("2. Puan Kazan")
        print("3. Puan Harca")
        print("4. Puanları Görüntüle")
        print("5. Kulüp Bilgilerini Göster")
        print("6. Etkinlik Geçmişini Göster")
        print("0. Çıkış")
        choice = input("Seçiminizi yapın: ")

        if choice == '0':
            break
        elif choice == '1':
            member_id = input("Üye ID'sini girin: ")
            name = input("Üye adını girin: ")
            new_member = Membership(member_id, name)
            print(f"{name} için üyelik oluşturuldu.")
        elif choice == '2':
            member_id = input("Puan kazanacak üye ID'sini girin: ")
            points = int(input("Kazanılacak puanı girin: "))
            for member in Membership.members:
                if member._Membership__member_id == member_id:
                    member.earn_points(points)
                    break
            else:
                print("Üye bulunamadı.")
        elif choice == '3':
            member_id = input("Puan harcayacak üye ID'sini girin: ")
            points = int(input("Harcanacak puanı girin: "))
            for member in Membership.members:
                if member._Membership__member_id == member_id:
                    member.redeem_points(points)
                    break
            else:
                print("Üye bulunamadı.")
        elif choice == '4':
            member_id = input("Puanları görüntülenecek üye ID'sini girin: ")
            for member in Membership.members:
                if member._Membership__member_id == member_id:
                    member.show_points()
                    break
            else:
                print("Üye bulunamadı.")
        elif choice == '5':
            Gym.display_club_info()  # Kulüp ismini değiştirdim
        elif choice == '6':
            Gym.show_event_log()  # Kulüp ismini değiştirdim
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
