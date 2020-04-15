from pybaseball import standings

# 1994 start of 5 teams per division

# data = standings(2019)

def get_data(year, div_id):
    league_data = standings(year)[div_id].values
    return league_data




