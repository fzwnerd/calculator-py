# Calculator-Py

A simple yet powerful command-line calculator built with Python. This calculator supports basic arithmetic operations (addition, subtraction, multiplication, and division) and can handle multiple operations in a single expression (e.g., `5 + 3 - 2`). It also logs all calculations to a JSON file for future reference.

## Features

- **Basic Arithmetic Operations**: Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- **Multiple Operations**: Allows chaining multiple operations in a single expression (e.g., `5.5 + 3.2 - 2.1`).
- **Decimal Support**: Handles decimal numbers seamlessly.
- **Error Handling**: Detects invalid inputs and division by zero errors.
- **Logging**: Saves all calculations to a `calculator_log.json` file for easy tracking.
- **Interactive Menu**: Provides a user-friendly menu for using the calculator, clearing logs, and exiting the program.

## Getting Started

### Prerequisites

- Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/fzwnerd/calculator-py.git
   ```

2. Navigate to the project directory:
   ```bash
   cd calculator-py
   ```

3. Run the calculator:
   ```bash
   python calculator_with_decimals.py
   ```

### Usage

1. **Start the Calculator**:
   Run the script, and you will see the following menu:
   ```
   Welcome to Python Calculator Beta Test!

   Menu:
   1. Use Calculator
   2. Clear Log
   3. Exit
   Choose an option:
   ```

2. **Use the Calculator**:
   - Choose option `1` to use the calculator.
   - Enter your expression (e.g., `5.5 + 3.2 - 2.1`).
   - The result will be displayed, and the calculation will be logged in `calculator_log.json`.

3. **Clear Logs**:
   - Choose option `2` to clear the calculation logs.

4. **Exit the Program**:
   - Choose option `3` to exit the program.

### Example

#### Input:
```
Choose an option: 1
Enter your expression (e.g., 5.5 + 3.2 - 2.1): 5.5 + 3.2 - 2.1
```

#### Output:
```
Result: 6.6
```

#### Log File (`calculator_log.json`):
```json
[
    {
        "operation": "5.5 + 3.2 - 2.1",
        "numbers": [5.5, "+", 3.2, "-", 2.1],
        "result": 6.6
    }
]
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request and describe your changes.
