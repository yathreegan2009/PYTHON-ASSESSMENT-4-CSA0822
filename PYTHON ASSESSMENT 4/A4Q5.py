
def read_data():
    return [80, 90, 70, 60]

def percentage(marks):
    return sum(marks) / len(marks)

def write_report(result):
    with open("report.txt", "w") as f:
        f.write(f"Attendance: {result}%")

if __name__ == "__main__":
    data = read_data()
    result = percentage(data)
    write_report(result)
    print(result)
