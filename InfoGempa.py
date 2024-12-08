import sys
from Gempa import *


gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("Palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("Jayapura", 3.3)
gempa5 = Gempa("Garut", 4.0)


print(Gempa.judul)
print(Gempa.deskripsi)
print("\033[92mInfo Dampak Gempa :\033[0m\n")

 
gempa1.dampak()
gempa2.dampak()
gempa3.dampak()
gempa4.dampak()
gempa5.dampak()

print("\n\033[92mTugas 12 Selesai\033[0m\n")
input("Tekan Enter untuk keluar.")
sys.exit(0)