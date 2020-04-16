from pybaseball import standings

bar_outline_colors = ['rgb(245, 140, 144)','rgb(71, 146, 173)','rgb(30, 122, 60)','rgb(227, 6, 107)','rgb(110, 207, 9)',
              'rgb(193, 194, 221)','rgb(3, 107, 161)','rgb(125, 165, 217)','rgb(107, 112, 135)','rgb(231, 68, 237)',
              'rgb(46, 38, 232)','rgb(118, 15, 185)','rgb(77, 169, 185)','rgb(144, 200, 133)','rgb(73, 196, 227)',
              'rgb(149, 155, 89)','rgb(42, 49, 10)','rgb(107, 72, 87)','rgb(104, 13, 228)','rgb(5, 246, 62)']
bar_colors = ['rgb(245, 140, 144, .7)','rgb(71, 146, 173, .7)','rgb(30, 122, 60, .7)','rgb(227, 6, 107, .7)','rgb(110, 207, 9, .7)',
              'rgb(193, 194, 221, .7)','rgb(3, 107, 161, .7)','rgb(125, 165, 217, .7)','rgb(107, 112, 135, .7)','rgb(231, 68, 237, .7)',
              'rgb(46, 38, 232, .7)','rgb(118, 15, 185, .7)','rgb(77, 169, 185, .7)','rgb(144, 200, 133, .7)','rgb(73, 196, 227, .7)',
              'rgb(149, 155, 89, .7)','rgb(42, 49, 10, .7)','rgb(107, 72, 87, .7)','rgb(104, 13, 228, .7)','rgb(5, 246, 62, .7)']

# 1994 start of 5 teams per division
# data = standings(1960)

def get_data(year, div_id=0):
    league_data = standings(year)[div_id].values
    return league_data

def get_size(year):
    val = standings(year)
    size = val[0].get('Name')
    return size.size


