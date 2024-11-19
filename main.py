from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
import json

teams = ['ATL', 'BOS', 'CHO', "CHI", "CLE", "DAL", "DEN", "DET", "GSW", "HOU", "IND", "OKC", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", "BKN", "ORL", "PHI", "PHO", "POR", "SAC", "TOR", "UTA", "WAS", "SAS"]
stats = {}

m = get_team_misc("ATL", 2024)
e = (m['eFG%'].values[0]-m['eFG%'].values[1])*100
t = (m['TOV%'].values[0]-m['TOV%'].values[1])
r = ((m['ORB%']+m['DRB%']))-1
ft = (m['FT/FGA'].values[0]-m['FT/FGA'].values[1])*100
s = 0.4*e+0.25*t+0.2*r+0.15*ft



stats['ATL'] = [e, t, r, ft, s]


m = get_team_misc("BOS", 2024)
e = (m['eFG%'].values[0]-m['eFG%'].values[1])*100
t = (m['TOV%'].values[0]-m['TOV%'].values[1])
r = ((m['ORB%']+m['DRB%']))-1
ft = (m['FT/FGA'].values[0]-m['FT/FGA'].values[1])*100
s = 0.4*e+0.25*t+0.2*r+0.15*ft

stats['BOS'] = [e, t, r, ft, s]
    

m = get_team_misc("DET", 2024)
e = (m['eFG%'].values[0]-m['eFG%'].values[1])*100
t = (m['TOV%'].values[0]-m['TOV%'].values[1])
r = ((m['ORB%']+m['DRB%']))-1
ft = (m['FT/FGA'].values[0]-m['FT/FGA'].values[1])*100
s = 0.4*e+0.25*t+0.2*r+0.15*ft

stats['DET'] = [e, t, r, ft, s]




sorted_by_value = sorted(stats.items(), key=lambda item: item[4])
with open("misc.json", 'w') as file:
    json.dump(stats, file)

#with open('users.json') as file:
#    users = json.load(file)



    
'''for count in teams:
    m = get_team_misc(count, 2024)
    e = m['eFG%'].values[0]-m['eFG%'].values[1]
    t = m['TOV%'].values[0]-m['TOV%'].values[1]
    r = ((m['ORB%']+m['DRB%'])/100)-1
    ft = m['FT/FGA'].values[0]-m['FT/FGA'].values[1]

    s = 0.4*e+0.25*t+0.2*r+0.15*ft
    f.write(count + ": " + str(s) + "\n")
    
    
f.close()'''