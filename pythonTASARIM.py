
ders_adi = "Python"
hoca_adi = "Dr. Öğretim Üyesi Erhan Cebeci"
ders_adi = "veri tabanı"
hoca_adi = "Ahmet doğukan Sarıyalçınkaya"
ders_adi = "İngilizce"
hoca_adi = "Dr. Öğretim Üyesi Gonca Tarı"


vize_notu = float(input(f"{ders_adi} dersi için vize notunu girin: "))
final_notu = float(input(f"{ders_adi} dersi için final notunu girin: "))

ortalama = (vize_notu * 0.4) + (final_notu * 0.6)

# Sonucu gösterme
print(f"\n{ders_adi} dersi ({hoca_adi}) için not ortalamanız: {ortalama:.2f}")

if ortalama >= 60:
    print(f"{ders_adi} dersini geçtiniz!")
else:
    print(f"{ders_adi} dersini geçemediniz.")
