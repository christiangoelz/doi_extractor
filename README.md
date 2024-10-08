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

# Run extraction
extractor = DOIExtractor(input_file)

# 1. extract dois
extractor.extract()

# 2. generate lens search string
extractor.to_lens_string()

# Save
extractor.save_dois()
extractor.save_lens_string()
```

Using command line: 
```bash
doi_extractor 'path/to/my_bibtex.bib'
```
