from pybaseball import standings

data = standings(2019)

def getTeamData(info, index):
    arr = []
    for x in data[index].get(info):
        arr.append(x)
    return arr

# MLB Team Stats for American League East
def alea_stats():
    team = getTeamData('Tm', 0)
    wins = getTeamData('W', 0)
    loses = getTeamData('L', 0)
    win_lose = getTeamData('W-L%', 0)
    gb = getTeamData('GB', 0)
    alea_data = [team, wins, loses, win_lose, gb]
    return alea_data

# MLB Team Stats for American League Central
def alct_stats():
    team = getTeamData('Tm', 1)
    wins = getTeamData('W', 1)
    loses = getTeamData('L', 1)
    win_lose = getTeamData('W-L%', 1)
    gb = getTeamData('GB', 1)
    alct_data = [team, wins, loses, win_lose, gb]
    return alct_data

# MLB Team Stats for American League West
def alwt_stats():
    team = getTeamData('Tm', 2)
    wins = getTeamData('W', 2)
    loses = getTeamData('L', 2)
    win_lose = getTeamData('W-L%', 2)
    gb = getTeamData('GB', 2)
    alwt_data = [team, wins, loses, win_lose, gb]
    return alwt_data

# MLB Team Stats for National League East
def nlea_stats():
    team = getTeamData('Tm', 3)
    wins = getTeamData('W', 3)
    loses = getTeamData('L', 3)
    win_lose = getTeamData('W-L%', 3)
    gb = getTeamData('GB', 3)
    nlea_data = [team, wins, loses, win_lose, gb]
    return nlea_data

# MLB Team Stats for National League Central
def nlct_stats():
    team = getTeamData('Tm', 4)
    wins = getTeamData('W', 4)
    loses = getTeamData('L', 4)
    win_lose = getTeamData('W-L%', 4)
    gb = getTeamData('GB', 4)
    nlct_data = [team, wins, loses, win_lose, gb]
    return nlct_data

# MLB Team Stats for National League West
def nlwt_stats():
    team = getTeamData('Tm', 5)
    wins = getTeamData('W', 5)
    loses = getTeamData('L', 5)
    win_lose = getTeamData('W-L%', 5)
    gb = getTeamData('GB', 5)
    nlwt_data = [team, wins, loses, win_lose, gb]
    return nlwt_data

alea_data = alea_stats()
alct_data = alct_stats()
alwt_data = alwt_stats()
nlea_data = nlea_stats()
nlct_data = nlct_stats()
nlwt_data = nlwt_stats()

