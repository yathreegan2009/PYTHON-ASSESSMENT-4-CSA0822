
def save_returns(books):
    with open("returns.log", "a", encoding="utf-8") as log:
        for book in books:
            log.write(book + "\n")

def process(day_file):
    try:
        with open(day_file, "r", encoding="utf-8") as f:
            books = f.readlines()

        save_returns(books)

    except FileNotFoundError as e:
        with open("error.log", "a", encoding="utf-8") as log:
            log.write(str(e) + "\n")

    except PermissionError as e:
        with open("error.log", "a", encoding="utf-8") as log:
            log.write(str(e) + "\n")

# Processing three days
process("day1.txt")
process("day2.txt")
process("day3.txt")

# Display the log
try:
    with open("returns.log", "r", encoding="utf-8") as f:
        print("Returned Books:")
        print(f.read())

except FileNotFoundError:
    print("Log file not found")
