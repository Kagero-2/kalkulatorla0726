#please add your calculator function here
# Kelompok 10
# ============================
# Rizky Pangestu - 2802394582
# Jason Raphael Soedirgo - 2802394531
# Muhammad Wildan Izzaturrahman - 2802497845
# Joy Tan - 2802412370
# Yohannes Jovan Aristo - 2802420624

# Kalkulator Sederhana
def tambah(a, b):
	return a + b

def kurang(a, b):
	return a - b

def kali(a, b):
	return a * b

def bagi(a, b):
	if b == 0:
		return "Error: Pembagian dengan nol!"
	return a / b

def main():
	print("=== Kalkulator Sederhana Kel 10 ===")
	print("Operasi yang tersedia:")
	print("1. Penjumlahan (+)")
	print("2. Pengurangan (-)")
	print("3. Perkalian (*)")
	print("4. Pembagian (/)\n")

	while True:
		try:
			a = float(input("Masukkan angka pertama: "))
			b = float(input("Masukkan angka kedua: "))
			operasi = input("Pilih operasi (+, -, *, /): ")

			if operasi == '+':
				hasil = tambah(a, b)
			elif operasi == '-':
				hasil = kurang(a, b)
			elif operasi == '*':
				hasil = kali(a, b)
			elif operasi == '/':
				hasil = bagi(a, b)
			else:
				print("Operasi tidak valid. Silakan coba lagi.\n")
				continue

			print(f"Hasil: {hasil}\n")
		except ValueError:
			print("Input tidak valid. Masukkan angka yang benar.\n")
			continue

		lanjut = input("Hitung lagi? (y/n): ").lower()
		if lanjut != 'y':
			print("Terima kasih telah menggunakan kalkulator.")
			break

if __name__ == "__main__":
	main()
