import csv

student_info = [["Rabindra", 30], ["Hari", 25]]  # this is a list
header_name = ["Name", " Age"]
with open("output.csv", "w", newline="") as file_obj:
    csv_writer = csv.writer(file_obj)
    csv_writer.writerow(header_name)  #  for header a single row
    csv_writer.writerows(student_info)  # for multiple data
