class Gempa:
    skala = ""
    lokasi = ""
    judul = "\n\033[1mAplikasi Pendeteksi Gempa, Berdasarkan Skala Gempa Sederhana - Pembuat Eko Muchamad Haryono\033[0m\n"
    deskripsi = "\033[93mData Lokasi Gempa Dan Skala Gempa Sudah Di Tentukan Dari Dosen\n\033[0m"


    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala


    def dampak(self):
        if self.skala < 2:
            print(f"Gempa Pertama di {self.lokasi} || Ket. Dampak Gempa : \033[91m Dampak gempa, tidak berasa.\033[0m || Dengan Skala {self.skala}")
        elif 2 <= self.skala <= 4:
            print(f"Gempa Kedua di {self.lokasi} || Ket. Dampak Gempa : \033[91m Dampak gempa, bangunan retak-retak.\033[0m || Dengan Skala {self.skala}")
        elif 4 <= self.skala <= 6:
            print(f"Gempa Ketiga di {self.lokasi} || Ket. Dampak Gempa : \033[91m Dampak gempa, bangunan roboh.\033[0m || Dengan Skala {self.skala}")
        elif self.skala >= 6:
            print(f"Gempa Keempat di {self.lokasi} || Ket. Dampak Gempa : \033[91m Dampak gempa, bangunan roboh dan berpotensi tsunami.\033[0m* || Dengan Skala {self.skala}")