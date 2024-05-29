- have to manually install ghostscript, potentially [add to path], then restart vscode
- you may have to make an "outputs" folder at the top level of this directory if it doesn't auto create

1. `parse_vp.py` 
2. `clean_output.py`
3. final artifacts: `complete_organic_table.csv` & `complete_inorganic_table.csv`

-- IFRA folder
- `ingredients.csv` is extracted from the IFRA gloassary
- `molecular_weights.csv` can be joined with `ingredients.csv` & vapor pressure data by using CAS