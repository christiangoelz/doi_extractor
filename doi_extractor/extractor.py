import bibtexparser
import re
from pathlib import Path
import sys

class DOIExtractor:
    def __init__(self, file):
        self.dois = []
        self.no_dois = []

        # Check inputs
        valid_files = ['bib', 'ris']
        file = Path(file)

        if file.is_file():
            self.file = file
            self.ending = file.suffix[1:]

            if self.ending not in valid_files:
                options = 'Allowed filetypes are '
                options += 'and '.join([f'.{v}' for v in valid_files[:-1]])
                print(f'Filetype not supported. {options}')
                sys.exit(1)
        else:
            print('Please provide a .bib or .ris file')
            sys.exit(1)

    def extract(self):
        if self.ending == 'bib':
            self.__extract_dois_from_bibtex()
        elif self.ending == 'ris':
            self.__extract_dois_from_ris()
        else:
            print(f'Unsupported file type: {self.ending}')
            sys.exit(1)

        if len(self.no_dois) > 0:
            print(f'No dois found for {self.no_dois}')
        return self

    def save(self, out_file):
        with open(out_file, 'w') as file:
            file.write(', '.join(self.dois))

    ###### Core extractor functions ######
    def __extract_dois_from_bibtex(self):
        bib_database = bibtexparser.parse_file(self.file)
        
        for entry in bib_database.entries:
            if 'doi' in entry:
                doi = self.__clean_doi(entry['doi'])
                self.dois.append(doi)
            elif 'DOI' in entry:
                doi = self.__clean_doi(entry['DOI'])
                self.dois.append(doi)
            else:
                self.no_dois.append(entry['title'])


    def __extract_dois_from_ris(self):
        with open(self.file, 'r') as risfile:
            lines = risfile.readlines()

        doi_found = False
        current_article = None

        for line in lines:
            if line.startswith('TI  - '):
                if not doi_found:
                    current_article = line[6:].strip()
                doi_found = False
            if line.startswith('DO  - '):
                self.dois.append(line[6:].strip())
                doi_found = True

        if current_article and not doi_found:
            self.no_dois.append(current_article)
            
    def __clean_doi(self, doi):

        if doi[:3] == 'doi':
            doi = doi.split('doi:')[-1]
        elif doi[:4] == 'http':
            doi = doi.split('https://doi.org/') [-1]

        return doi
    
def main():
    if len(sys.argv) != 3:
        print('Usage: python extractor.py <input_file> <output_file>')
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    extractor = DOIExtractor(input_file)
    extractor.extract()
    extractor.save(output_file)


if __name__ == '__main__':
    main()