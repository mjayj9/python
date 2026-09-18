import csv
data = [
    ["이름", "나이", "점수"],
    ["김철수", 15, 90],
    ["이영희", 14, 85],
    ["박민수", 15, 95]
]
with open("이름3.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

with open("점수3.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)


with open("이름3.csv", "w+", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
    writer = csv.writer(f)
    writer.writerows(data)