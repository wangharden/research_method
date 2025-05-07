import csv

def csv_to_bibtex(csv_file, bibtex_file):
    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        with open(bibtex_file, 'w', encoding='utf-8') as bibfile:
            for row in reader:
                bib_entry = f"@article{{{row['title'].replace(' ', '_')},\n"
                bib_entry += f"  title = {{{row['title']}}},\n"
                bib_entry += f"  author = {{{row['author']}}},\n"
                bib_entry += f"  year = {{{row['year']}}},\n"
                bib_entry += f"  abstract = {{{row['abstract']}}},\n"
                bib_entry += f"  doi = {{{row['doi']}}},\n"
                bib_entry += f"  keywords = {{{row['keywords']}}},\n"
                bib_entry += f"  category = {{{row['category']}}},\n"
                if 'Venue' in row:
                    bib_entry += f"  venue = {{{row['Venue']}}},\n"
                if 'Short Notes' in row:
                    bib_entry += f"  note = {{{row['Short Notes']}}},\n"
                bib_entry += "}\n\n"
                bibfile.write(bib_entry)

csv_to_bibtex('2.csv', 'bib/references.bib')