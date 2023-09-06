import pandas as pd
import sys

class CsvReader:
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        try:
            if isinstance(filename, str):
                self.filename = filename
            else:
                raise AttributeError('ERROR: \'filename\' must be a string')
            if isinstance(sep, str):
                self.sep = sep
            else:
                raise AttributeError('ERROR: \'sep\' must be a string')
            if isinstance(header, bool):
                self.header = header
            else:
                raise AttributeError('ERROR: \'header\' must be a bool')
            if isinstance(skip_top, int) and isinstance(skip_bottom, int):
                self.skip_bottom = skip_bottom
                self.skip_top = skip_top
            else:
                raise AttributeError('ERROR: \'skip_*\' must be an int')
            self.file_as_lst = []
        except AttributeError as a:
            print(a)
            sys.exit()

    def __enter__(self):
        self.file_handler = open(self.filename, 'r')
        size_check = 0
        parsed_file = self.file_handler.readlines()
        for idx, line in enumerate(parsed_file):
            attr_lst = [ word.strip() for word in line.split(self.sep) if len(word.strip()) != 0 ]
            if idx != 0 and len(attr_lst) != size_check:
                raise Exception(f'ERROR: \'{self.filename}\' is corrupted at line {idx + 1}')
                return None
            size_check = len(attr_lst)
            self.file_as_lst.append(attr_lst)
        return self



    def __exit__(self, type, value, traceback):
        if isinstance(type, OSError):
            print('could not open the file')
        else:
            self.file_handler.close()
    
    def getdata(self):
        size_idx = len(self.file_as_lst) - 1
        header_skip = 0 if not self.header else 1
        return self.file_as_lst[header_skip + self.skip_top: size_idx - self.skip_bottom ]

    def getheader(self):
        if self.header:
            return self.file_as_lst[0]
        return None




