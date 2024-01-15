# CSV files are a common format for working with structured data in Python. Here's what you need to know:
#   - CSV stands for comma-separated values.
#   - CSV files are plain text files that contain tabular data.
#   - CSV files typically use a comma , as a delimiter to separate values.
#   - CSV files typically have a .csv file extension.
#   - CSV files can be opened using the open() function.

# Example: Open a CSV file and print its contents.
with open("data/users.csv", "r") as file:
    content = file.read()
    print(content)

# Example: Open a CSV file and print its contents line-by-line.
with open("data/users.csv", "r") as file:
    content = file.readlines()
    print(content)

# Example: Open a CSV file and print its contents using the csv module.
import csv

with open("data/users.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
