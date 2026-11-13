
from decimal import Decimal, InvalidOperation

def process_file(filename):
    total = Decimal("0.00")
    report = []
    rejected = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                try:
                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        raise ValueError("Invalid number of fields")

                    reg_no, name, amount = parts
                    amount = Decimal(amount)

                    total += amount
                    report.append(f"{name} {amount}")

                except (ValueError, InvalidOperation):
                    rejected.append((line_no, line.strip()))

        print("Mess Bill Report")
        for item in report:
            print(item)

        print("Total:", total)
        print("Rejected Lines:", rejected)

    except FileNotFoundError:
        print("File not found")

process_file("mess_oct.txt")
