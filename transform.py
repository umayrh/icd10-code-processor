import os
import csv
from xml.etree import ElementTree as ET


def transform_cm_diagnosis_codes_tabluar(source_file: str, dest_file: str):
    tree = ET.parse(source_file)
    root = tree.getroot()

    fieldnames = ['icd10_code_name', 'icd10_code_desc']
    os.makedirs(os.path.dirname(dest_file), exist_ok=True)

    with open(dest_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for child in root.findall('chapter'):
            for diag in child.iter('diag'):
                diag_name = diag.find('name').text
                diag_desc = diag.find('desc').text
                writer.writerow({'icd10_code_name': diag_name, 'icd10_code_desc': diag_desc})


if __name__ == "__main__":
    source_file = 'data/icd10cm_tabular_2023.xml'
    dest_file = './data/csv/icd10cm_tabular_2023.csv'
    transform_cm_diagnosis_codes_tabluar(source_file, dest_file)
