import pandas as pd

class CsvReader:
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        # try:
        if header:
            self.file_as_pd_data_frame = pd.read_csv(filename, sep=sep, header=0)
        else:
            self.file_as_pd_data_frame = pd.read_csv(filename, sep=sep, header=None)
        self.targeted_rows = self.file_as_pd_data_frame.iloc[skip_top: self.file_as_pd_data_frame.shape[0] - skip_bottom ]
        self.request_as_list_of_list = self.targeted_rows.values.tolist()

        self.header_list = self.file_as_pd_data_frame.columns.tolist()
        self.initSuccess = True
        # except:
            # self.initSuccess = False


    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        if type == None:
            return True
        else:
            print('JE SUIS PASSE PAR LA')
            return False


    def getdata(self):
        if self.initSuccess:
            return self.request_as_list_of_list
        raise Exception("Invalid data format. Expected a list.")

    def getheader(self):
        if self.initSuccess:
            return self.header_list
        raise Exception("Invalid data format. Expected a list.")

filename = 'bad.csv'
if __name__ == "__main__":
    with CsvReader(filename) as file:
        data = file.getdata()
        header = file.getheader()
    print(data)