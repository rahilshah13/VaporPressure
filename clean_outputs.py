import csv
import os

# removes the first two rows from every CSV, then combines them into a single output file.
def stitch_csv_files(input_files, output_file):
  header_row = ["N", "FORMULA", "NAME",	"CAS", "A", "B", "C",	"TMIN", "TMAX",	"code"]

  with open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header_row)

    for filename in input_files:
      with open(filename, 'r') as infile:
        reader = csv.reader(infile)
        # Skip the first two rows
        next(reader, None)
        next(reader, None)

        for row in reader:
          writer.writerow(row)
        

# Replace with your list of CSV file paths
cwd = os.getcwd()

organic_files = [cwd + "/outputs/organic_data-page-" + str(i) + "-table-1.csv" for i in range(1, 314)]
inorganic_files = [cwd + "/outputs/inorganic_data-page-" + str(i) + "-table-1.csv" for i in range(1, 8)]


stitch_csv_files(organic_files, "complete_organic_table.csv")
stitch_csv_files(inorganic_files, "complete_inorganic_table.csv")

print("fin.")