import csv

with open("D:\\Shiash Internship\\CodingPractices\\data.csv", "w") as f:
    writter = csv.writer(f)
    writter.writerow(["name", "id", "class"])
    writter.writerow(["sankar", "1", "null"])

