from PyPDF2 import PdfReader
import csv
import requests
from bs4 import BeautifulSoup as BS

reader = PdfReader("glossary.pdf")
pages = reader.pages[12:]

primary_descriptors = set([
  "Aromatic", "Earthy", "Woody", "Citrus", "Floral", "Minty", "Sulfurous", "Musk like", "Green", \
  "Herbal", "Fruity", "Marine", "Food like", "Aldehydic", "Animal like", "Powdery", "Balsamic", "Amber", \
  "Gourmand", "Acidic", "Ozonic", "Smoky", "Spicy", "Tobacco like", "Anisic", "Camphoraceous", "Honey"
])

CAS = {}

# parse into a format that can be easily stored as csv
def parse_ingredients_pdf():
  ingredients = []

  i = 0
  for i, p in enumerate(pages):
    text = p.extract_text().split("\n")
    line_n = 13

    while True: # break at end of page
      ingredient, field_n = dict(), 0

      while True:
        if field_n == 0:
          ingredient["cas"] = text[line_n + field_n]
          CAS.add(ingredient["cas"])
          field_n += 1
        
        elif text[line_n + field_n].strip() in primary_descriptors:
          ingredient["desc-1"] = text[line_n + field_n]
          ingredient["desc-2"] = text[line_n + field_n + 1]
          ingredient["desc-3"] = text[line_n + field_n + 2]
          field_n += 4
          ingredients.append(ingredient)
          break

        else:
          if field_n == 1: ingredient["name"] = text[line_n + field_n]
          else: ingredient["name"] += text[line_n + field_n]
          field_n += 1

      line_n += field_n
      if text[line_n].find('©') != -1:
        break
      
    print("PAGE", i, "COMPLETE")
  return ingredients

def write_to_csv(ingredients, file_name):
  with open(file_name, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=ingredients[0].keys())
    w.writeheader()
    w.writerows(ingredients)

def csv_to_cas_dict(file_name):
  ingredients = dict()
  with open(file_name, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
      ingredients[row["cas"]] = {"name": row["name"].strip(), "desc-1": row["desc-1"].strip(), "desc-2": row["desc-2"].strip(), "desc-3": row["desc-3"].strip()}
  return ingredients


def fetch_physical_properties(cas, writer):
  URL = "https://webbook.nist.gov/cgi/cbook.cgi?ID={cas}&Units=SI&cTP=on"
  page = requests.get(URL.format(cas=cas))
  soup = BS(page.content, "html.parser")

  try:
    MW = soup.find("a", title="IUPAC definition of relative molecular mass (molecular weight)").parent.parent.text
    writer.writerow([cas, MW.split(":")[1].strip()])
    print("{0}\n{1}".format(cas, MW))
    
  except:
    print("MW not found.")

def main():
  ALL_INGREDIENTS = csv_to_cas_dict("ingredients.csv")

  with open("molecular_weights.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["CAS", "MolecularWeight"])

    for i in ALL_INGREDIENTS:
      fetch_physical_properties(i, writer)
      print("---")

if __name__ == "__main__":
  main()