import json
import os

# Fungsi untuk menyimpan log ke file JSON
def save_log(operation, numbers, result):
    log_entry = {
        "operation": operation,
        "numbers": numbers,
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

# Fungsi kalkulator dengan hitungan ganda
def calculator():
    print("\nSimple Calculator with Multiple Operations")
    print("Operations: +, -, *, /")

    try:
        # Input angka dan operasi
        expression = input("Enter your expression (e.g., 5 + 3 - 2): ")
        parts = expression.split()

        # Validasi input
        if len(parts) < 3 or len(parts) % 2 == 0:
            print("Invalid expression. Please use the format: x + y - z")
            return

        # Inisialisasi hasil dengan angka pertama
        result = float(parts[0])
        operation_history = [result]  # Untuk menyimpan riwayat operasi

        # Proses hitungan ganda
        for i in range(1, len(parts), 2):
            operator = parts[i]
            next_number = float(parts[i + 1])

            if operator == "+":
                result = tambah(result, next_number)
            elif operator == "-":
                result = kurang(result, next_number)
            elif operator == "*":
                result = kali(result, next_number)
            elif operator == "/":
                result = bagi(result, next_number)
            else:
                print(f"Invalid operator: {operator}")
                return

            operation_history.extend([operator, next_number])  # Tambahkan ke riwayat

        # Output
        print(f"Result: {result}")

        # Simpan log operasi (kecuali jika terjadi error pembagian oleh nol)
        if result != "Error: Division by zero is not allowed.":
            save_log(" ".join(map(str, operation_history)), operation_history, result)

    except ValueError:
        print("Invalid input. Please enter numbers and valid operators.")

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
