import pandas as pd

class CsvReader:
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        try:
            self.file_as_pd_data_frame = pd.read_csv(filename, sep=sep, header=None)
            if header:
                self.targeted_rows = self.file_as_pd_data_frame.iloc[skip_top + 1: self.file_as_pd_data_frame.shape[0] - skip_bottom ]
            else:
                self.targeted_rows = self.file_as_pd_data_frame.iloc[skip_top: self.file_as_pd_data_frame.shape[0] - skip_bottom ]
            self.request_as_list_of_list = self.targeted_rows.values.tolist()
            self.header_list = self.file_as_pd_data_frame.iloc[0].tolist()
            # if header:
                # self.header_list = self.file_as_pd_data_frame.iloc[0].tolist()
            # else:
                # self.header_list = None
            self.initSuccess = True
            self.corrupted = self.targeted_rows.isna().any().any()
        except Exception as e:
            print(e)
            self.initSuccess = False


    def __enter__(self):
        if not self.corrupted:
            return self
        return None
    
    def __exit__(self, type, value, traceback):
        if type == None:
            return True
        else:
            return False


    def getdata(self):
        if self.initSuccess and not self.corrupted:
            return self.request_as_list_of_list
        if self.corrupted:
            raise Exception("file is corrupted")
        raise Exception("Invalid data format. Expected a list.")

    def getheader(self):
        if self.initSuccess and not self.corrupted and self.header_list:
            return self.header_list
        raise Exception("Invalid data format. Expected a list.")

filename = 'good.csv'
if __name__ == "__main__":
    with CsvReader(filename) as file:
        data = file.getdata()
        # header = file.getheader()
    print(data)


# if __name__ == "__main__":
    # with CsvReader('bad.csv') as file:
        # if file == None:
            # print("File is corrupted")