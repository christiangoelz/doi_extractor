# DOI Extractor

A tiny Python program to extract DOIs from BibTeX or RIS files.

## Installation

Clone this repository:
```bash
git clone ...
```
Install:
```bash
cd  doi_extractor
pip install -e .
```
 
## Usage 

Using python: 
```Python
from doi_extractor import DOIExtractor

# Define input and output fle
input_file = 'path/to/my_bibtex.bib'
input_file = 'path/to/output.txt'

# Run extraction
extractor = DOIExtractor(input_file)
extractor.extract()
extractor.save(output_file)

```

Using command line: 
```bash
extract_doi 'path/to/my_bibtex.bib' 'path/to/output.txt'
```
