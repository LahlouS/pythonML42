import pandas as pd


def proportionBySport(df, year, sport, sex):
    if not (isinstance(year, int) and isinstance(sport, str) and isinstance(sex, str) and isinstance(df, pd.DataFrame)):
        return None
    filtered_df = df[(df["Year"] == year) & (df["Sex"] == sex)].drop_duplicates(subset=["ID", "Sport"])
    result_df = filtered_df.groupby(["Sport"]).size().reset_index(name='Count')
    return result_df[(result_df["Sport"] == sport)]["Count"].sum() / result_df["Count"].sum()

if __name__ == '__main__':
    from fileLoader import FileLoader
    
    fl = FileLoader()
    df = fl.load('./athlete_events.csv')
    print(proportionBySport(df, 2004, 'Tennis', 'F'))