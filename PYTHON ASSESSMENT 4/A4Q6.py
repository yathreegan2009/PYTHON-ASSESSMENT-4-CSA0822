
import os
import re

students = {}
seen = set()
events = {}
errors = []

def validate_email(email):
    return bool(re.match(
        r"^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$",
        email
    ))

def process_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:

            for line_no, line in enumerate(f, 1):
                try:
                    parts = line.strip().split(",")

                    if len(parts) != 5:
                        raise ValueError("Damaged record")

                    reg, name, dept, email, choices = parts

                    if not validate_email(email):
                        raise ValueError("Invalid email")

                    if reg in seen:
                        raise ValueError("Duplicate registration")

                    seen.add(reg)

                    students[reg] = [name, dept, email]

                    for event in choices.split(";"):
                        event = event.strip()

                        if event:
                            events.setdefault(event, []).append(
                                f"{reg},{name},{dept}"
                            )

                except ValueError as e:
                    errors.append(
                        f"{filename}, Line {line_no}: {e}"
                    )

    except FileNotFoundError:
        errors.append(f"{filename}: File not found")

    except PermissionError:
        errors.append(f"{filename}: Permission denied")

def generate_reports():

    os.makedirs("output", exist_ok=True)

    # Master list
    with open("output/master_list.txt", "w") as f:
        for reg, details in students.items():
            f.write(f"{reg},{details}\n")

    # Event-wise participant lists
    for event, participants in events.items():
        filename = "output/" + event + ".txt"

        with open(filename, "w") as f:
            for student in participants:
                f.write(student + "\n")

    # Summary report
    with open("output/summary.txt", "w") as f:
        f.write("Total Registrations: " + str(len(students)))
        f.write("\nTotal Events: " + str(len(events)))

        for event, participants in events.items():
            f.write(
                f"\n{event}: {len(participants)} participants"
            )

    # Error log
    with open("output/error_log.txt", "w") as f:
        for error in errors:
            f.write(error + "\n")

# Process department files
files = [
    "department1.txt",
    "department2.txt",
    "department3.txt",
    "department4.txt",
    "department5.txt"
]

for filename in files:
    process_file(filename)

generate_reports()

print("Registration Processing Completed")
print("Total Students:", len(students))
print("Total Events:", len(events))
print("Errors:", len(errors))
