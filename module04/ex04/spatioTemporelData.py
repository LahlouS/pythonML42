import pandas as pd

class SpatioTemporelData:

    def __init__(self, df):
        if isinstance(df, pd.DataFrame) and "City" in df.columns and "Year" in df.columns:
            self.df = df
    
    def where(self, year):
        return [df[(df["Year"] == year)]["City"].iloc[0]]


    def when(self, location):
        years = df[(df["City"] == location)].groupby(["Year"]).size().reset_index(name='Count')
        return [year for year in years["Year"]] 

if __name__ == "__main__":
    from fileLoader import FileLoader
    df = FileLoader().load('./athlete_events.csv')
    sptmp = SpatioTemporelData(df)
    print(sptmp.where(1896))
    # Output
    # [’Athina’]
    print(sptmp.where(2016))
    # Output
    # [’Rio de Janeiro’]
    print(sptmp.when('Athina'))
    # Output
    # [2004, 1906, 1896]
    print(sptmp.when('Paris'))
    # Output
    # [1900, 1924]
