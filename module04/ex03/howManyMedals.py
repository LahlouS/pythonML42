import pandas as pd
from fileLoader import FileLoader


def howManyMedals(df, name):
    name_filtered_df = df[(df["Name"] == name)]
    test = name_filtered_df.copy()
    test["Medal"].fillna('chouBlanc', inplace=True)
    group_by_year_and_medal = test.groupby(["Year", "Medal"]).size().reset_index(name='Count')

    ret_dict = {}
    for idx, rows in group_by_year_and_medal.iterrows():
        if str(rows["Year"]) not in ret_dict:
            ret_dict[str(rows["Year"])] = {"Gold": 0, "Silver": 0, "Bronze": 0}
        if rows["Medal"] != "chouBlanc":
            ret_dict[str(rows["Year"])][rows["Medal"]] = rows["Count"]
    return ret_dict
if __name__ == "__main__":
    df = FileLoader().load('./athlete_events.csv')
    for key, val in howManyMedals(df, "Karl Jan Aas").items():
        print(key, val)