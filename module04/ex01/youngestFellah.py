import pandas as pd
from fileLoader import FileLoader

def youngestFellah(df, year):
    if isinstance(df, pd.DataFrame) and isinstance(year, int):

        m_filtered_df = df[(df['Sex'] == 'M') & (df['Year'] == year)]
        f_filtered_df = df[(df['Sex'] == 'F') & (df['Year'] == year)]
        print(f_filtered_df.head())
        try:
            sorted_df = {
                        "m": m_filtered_df.sort_values(by='Age')["Age"].iloc[0],
                        "f": f_filtered_df.sort_values(by='Age')["Age"].iloc[0]
                        }
        except Exception as err:
            print(f'ERRROR: {err} (which basically means that the year you are looking for does not exist)')
            sorted_df = None
        return sorted_df


if __name__ == "__main__":
    fl = FileLoader()
    olymp_df = fl.load('athlete_events.csv')
    print(youngestFellah(olymp_df, 1992))
