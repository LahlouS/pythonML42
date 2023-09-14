import pandas as pd

class FileLoader:
    def __init__(self):
        pass

    def load(self, path):
        try:
            df = pd.read_csv(path)
            print(f'loading dataset of size {df.shape}')
            return df
        except Exception as err:
            print("Error occurred:", err)
            if hasattr(err, 'filename'):
                print("Filename:", err.filename)
    
    def display(self, df, n):
        if isinstance(df, pd.DataFrame):
            start = 0 if n > 0 else n
            stop = n if n > 0 else df.shape[0]
            print(df[start:stop])
            print(f'\n[{abs(n)} rows x {df.shape[1]} columns]')
            return True
        else:
            print('ERRRO: arg must be of type nd.array')
            return False
