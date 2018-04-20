
import sys
import re

refe_pat = re.compile(r'"references": \[.*?\]')
lang_pat = re.compile(r'"lang": ".*?"')
year_pat = re.compile(r'"year": [0-9]*')
titl_pat = re.compile(r'"title": ".*?"')
doi_pat = re.compile(r'"doi": ".*?"')
id_pat = re.compile(r'"id": ".*?"')

with open(sys.argv[1]) as f:
    for line in f:
        line_entry = []

        lang = lang_pat.search(line)
        if not lang or '"en"' not in lang.group(0):
            continue

        year = year_pat.search(line)
        if not year:
            continue

        titl = titl_pat.search(line)
        if not titl:
            continue

        enid = id_pat.search(line)
        if not enid:
            continue

        line_entry.append(enid.group(0))
        line_entry.append(year.group(0))
        line_entry.append(titl.group(0))

        refe = refe_pat.search(line)
        if refe:
            line_entry.append(refe.group(0))
        else:
            line_entry.append('"references": []')

        doi = doi_pat.search(line)
        if doi:
            line_entry.append(doi.group(0))
        else:
            line_entry.append('"doi": ""')

        print("{" + ", ".join(line_entry) + "}")
        

