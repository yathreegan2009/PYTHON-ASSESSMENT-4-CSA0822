
from pathlib import Path

def process_attendance(folder):
    attendance = {}
    errors = []

    files = Path(folder).glob("*.txt")

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                try:
                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        raise ValueError("Invalid record")

                    reg, date, status = parts

                    if status not in ("P", "A"):
                        raise ValueError("Invalid status")

                    if reg not in attendance:
                        attendance[reg] = [0, 0]

                    if status == "P":
                        attendance[reg][0] += 1
                    else:
                        attendance[reg][1] += 1

                except ValueError as e:
                    errors.append(
                        (file.name, line_no, str(e))
                    )

    with open("attendance_report.txt", "w") as f:
        for reg, counts in attendance.items():
            present, absent = counts
            total = present + absent
            percentage = present / total * 100

            f.write(f"{reg}: {percentage:.2f}%\n")

            if percentage < 75:
                print(reg, "Below 75%")

    with open("error_log.txt", "w") as f:
        for error in errors:
            f.write(str(error) + "\n")

process_attendance("attendance")
