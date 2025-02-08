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

# Fungsi pengurangan
def kurang(x, y):
    return x - y

# Fungsi perkalian
def kali(x, y):
    return x * y

# Fungsi pembagian
def bagi(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

# Fungsi kalkulator
def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    try:
        num1 = float(input("Enter the first number: "))
        operation = input("Enter the operation: ")
        num2 = float(input("Enter the second number: "))

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = kurang(num1, num2)  # Menggunakan fungsi kurang(x, y)
        elif operation == "*":
            result = kali(num1, num2)  # Menggunakan fungsi kali(x, y)
        elif operation == "/":
            result = bagi(num1, num2)  # Menggunakan fungsi bagi(x, y)
        else:
            print("Invalid operation.")
            return

        print(f"Result: {result}")

        # Simpan log operasi (kecuali jika terjadi error pembagian oleh nol)
        if result != "Error: Division by zero is not allowed.":
            save_log(operation, num1, num2, result)

    except ValueError:
        print("Invalid input. Please enter numbers only.")

# Menu utama
def main():
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
