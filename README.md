# ArchivesSpace Beyond the Basics Skillshare: Data Auditing for the ArchivesSpace PUI
  
### Requirements

- ArchivesSpace 2.x+
- MySQL client
- Python 3
  
  `pandas` module (included with [Anaconda](https://www.anaconda.com/download/))
- [OpenRefine](http://openrefine.org/download.html)
- [LibreOffice](https://www.libreoffice.org/download/download/), Excel

### Demo 1: Publication Status

`get_note_pub_status.sql`

`get_component_pub_status.sql`

`get_resource_pub_status.sql`

### Demo 2: Access Restrictions

`extract_restricts.py`

#### Troubleshooting

`find_diffs.py`

`find_dupes.py`

### Demo 3: Dates

[Timetwister](https://github.com/alexduryee/timetwister) + `subprocess` module
  Thanks to Alex Duryee!

`date_parse.py`

#### Regular expressions to find dates in strings:
  - `[^a-zA-z0-9]\d\d\d\d[^a-zA-Z0-9]`
    - Broadest, will return all 4 digit numbers directly in between any 2 non-letter, non-number characters. Will also return accession numbers which contain years
    
#### Reg Ex Resources:
[Reg Ex Checker](https://regex101.com/)

### Demo 4: Labels

`extract_text.py`

`pandas-toolbox.py`

### Demo 5: URLs

### Demo 6: Containers

### Demo 7: Extents

-GROUP BY, COUNT

### Demo 8: Citations

### Lessons Learned

- Prioritize tasks by potential impact on users, data security
- Clean-up is an iterative process
- Use SQL to retrieve data
- Use Python to manipulate, analyze, and update data
  - Output as input
