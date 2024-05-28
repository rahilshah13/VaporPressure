import PyPDF2
import camelot
import os

def extract_pages(input_fn, start_page, end_page, output_fn):
  pdf_reader = PyPDF2.PdfReader(open(input_fn, 'rb'))  # Open in binary mode
  pdf_writer = PyPDF2.PdfWriter()

  for page_num in range(start_page - 1, end_page):  # Adjust for 0-based indexing
    page = pdf_reader.pages[page_num]
    pdf_writer.add_page(page)

  with open(output_fn, 'wb') as output_file:  # Open in binary write mode
    pdf_writer.write(output_file)

  print(f"{end_page - start_page + 1} pages extracted from '{input_fn}' and saved to '{output_fn}'.")


def extract_table_data(pdf_file):
  pages = read_pdf(pdf_file, multiple_tables=True)
  table_data = []

  for page in pages:
    for table in page:
      print(table)
      table_data.append(table)

  return table_data


################################################
################################################
 
def main():
  cwd = os.getcwd()
  pages = [(8, 320, 'organic_table_pages.pdf'), (322, 328, 'inorganic_table_pages.pdf')]

  for (start, end, output_fn) in pages:
    extract_pages(cwd+"/inputs/book.pdf", start, end, cwd + "/inputs/"+output_fn)

  organic_data = camelot.read_pdf(cwd + '/inputs/organic_table_pages.pdf', pages='all')
  inorganic_data = camelot.read_pdf(cwd + '/inputs/inorganic_table_pages.pdf', pages='all')

  organic_data.export(cwd + "/outputs/organic_data.csv", f="csv", compress=False)
  inorganic_data.export(cwd + "/outputs/inorganic_data.csv", f="csv", compress=False)



if __name__=="__main__": 
  main()