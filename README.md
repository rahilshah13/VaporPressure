Setup:
- `pip install camelot-py[cv]`
- `pip install PyPDF2`
- `mkdir outputs` at the top level of this repo

- On windows, you have to manually install ghostscript in order for camelot to work. You may also need to add ghostscript to your Path variable.

--
1. `parse_vp.py` 
2. `clean_output.py`
3. final artifacts: `complete_organic_table.csv` & `complete_inorganic_table.csv`

-- IFRA folder
- `ingredients.csv` is extracted from the IFRA gloassary
- `molecular_weights.csv` can be joined with `ingredients.csv` & vapor pressure data using CAS. 

- n.b. `ingredients.csv` uses lowercase `cas` while the other csvs use uppercase `CAS` (im too lazy to fix)