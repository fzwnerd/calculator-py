import json
import os

# Fungsi untuk menyimpan log ke file JSON
def save_log(operation, num1, num2, result):
    log_entry = {
        "operation": operation,
        "num1": num1,
        "num2": num2,
        "result": result
    }

    # Cek apakah file log sudah ada
    if os.path.exists("calculator_log.json"):
        with open("calculator_log.json", "r") as file:
            logs = json.load(file)
    else:
        logs = []

    # Tambahkan log baru
    logs.append(log_entry)

    # Simpan log ke file
    with open("calculator_log.json", "w") as file:
        json.dump(logs, file, indent=4)

# Fungsi untuk menghapus log
def clear_log():
    if os.path.exists("calculator_log.json"):
        os.remove("calculator_log.json")
        print("Log file has been deleted.")
    else:
        print("No log file found.")

# Fungsi-fungsi Aritmatika
def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

# Fungsi kalkulator
def calculator():
    print("\nSimple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        # Input Pengguna
        pilihan = input("Choose an operation (1/2/3/4): ")
        angka1 = float(input("Enter the first number: "))
        angka2 = float(input("Enter the second number: "))

        # Kondisi dan Pemanggilan Fungsi
        if pilihan == "1":
            result = tambah(angka1, angka2)  # Panggil fungsi tambah
            operation = "+"
        elif pilihan == "2":
            result = kurang(angka1, angka2)  # Panggil fungsi kurang
            operation = "-"
        elif pilihan == "3":
            result = kali(angka1, angka2)  # Panggil fungsi kali
            operation = "*"
        elif pilihan == "4":
            result = bagi(angka1, angka2)  # Panggil fungsi bagi
            operation = "/"
        else:
            print("Invalid operation choice.")
            return

        # Output
        print(f"Result: {result}")

        # Simpan log operasi (kecuali jika terjadi error pembagian oleh nol)
        if result != "Error: Division by zero is not allowed.":
            save_log(operation, angka1, angka2, result)

    except ValueError:
        print("Invalid input. Please enter numbers only.")

# Menu utama
def main():
    # Pesan Selamat Datang
    print("Welcome to Python Calculator Beta Test!")

    while True:
        print("\nMenu:")
        print("1. Use Calculator")
        print("2. Clear Log")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            clear_log()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Jalankan program
if __name__ == "__main__":
    main()
