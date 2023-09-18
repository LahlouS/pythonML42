team_sports = [
            'Basketball', 
            'Football',
            'Tug-Of-War',
            'Badminton',
            'Handball',
            'Water Polo',
            'Hockey',
            'Rowing',
            'Volleyball',
            'Synchronized Swimming',
            'Baseball',
            'Rugby',
            'Lacrosse',
            'Polo'
            ]

def howManyMedalsByCountry(df, team):
    team_filtered_df = df[(df["Team"] == team) & (df["Sport"].isin(team_sports))]
    test = team_filtered_df.copy()

    test["Medal"].fillna('chouBlanc', inplace=True)
    group_by_year_and_medal = test.groupby(["Year", "Medal"]).size().reset_index(name='Count')

    ret_dict = {}
    for idx, rows in group_by_year_and_medal.iterrows():
        if str(rows["Year"]) not in ret_dict:
            ret_dict[str(rows["Year"])] = {"Gold": 0, "Silver": 0, "Bronze": 0}
        if rows["Medal"] != "chouBlanc":
            ret_dict[str(rows["Year"])][rows["Medal"]] = rows["Count"]
    return ret_dict


if __name__ == '__main__':
    from fileLoader import FileLoader

    df = FileLoader().load('./athlete_events.csv')

    for year, medals in howManyMedalsByCountry(df, 'France').items():
        print(year, medals)
