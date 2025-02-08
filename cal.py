import json
from datetime import datetime

def log_operation(operation, num1, num2, result):
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "operation": operation,
        "num1": num1,
        "num2": num2,
        "result": result
    }

    with open("calculator_log.json", "a") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")

# Fungsi kalkulator
def calculator():
    print("Selamat datang di Kalkulator Sederhana!")
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    choice = input("Masukkan pilihan (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))

        if choice == '1':
            result = num1 + num2
            operation = "Penjumlahan"
            print(f"Hasil: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            operation = "Pengurangan"
            print(f"Hasil: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            operation = "Perkalian"
            print(f"Hasil: {num1} * {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("Error: Pembagian dengan nol tidak diperbolehkan!")
                return
            result = num1 / num2
            operation = "Pembagian"
            print(f"Hasil: {num1} / {num2} = {result}")

        log_operation(operation, num1, num2, result)
    else:
        print("Pilihan tidak valid!")

# Jalankan kalkulator
if __name__ == "__main__":
    calculator()
