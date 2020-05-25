#I use the dictionary for teams and their ELO vaues.
thisdict =	{
#Premier League
  'liverpool': 2043,
  'mancity': 2037,
  'tottenham': 1891,
  'arsenal': 1866,
  'chelsea': 1863,
  'manunited': 1838,
  'everton': 1769,
  'crystalpalace': 1742,
  'leicester': 1783,
  'westham': 1729,
  'wolves': 1719,
  'newcastle': 1715,
  'bournemouth': 1690,
  'watford': 1685,
  'burnley': 1681,
  'southampton': 1673,
  'brighton': 1616,
  'astonvilla': 1612,
  'sheffunited': 1619,
  'norwich': 1631,
#Championship
  'westbrom': 1607,
  'derby': 1567,
  'leeds': 1545,
  'swansea': 1543,
  'middlesbrough': 1543,
  'brentford': 1540,
  'bristolcity': 1530,
  'sheffwed': 1524,
  'stoke': 1521,
  'preston': 1514,
  'hull': 1504,
  'forest': 1501,
  'birmingham': 1496,
  'blackburn': 1466,
  'wigan': 1450,
  'millwall': 1450,
  'reading': 1449,
  'qpr': 1439,
  'rotherham': 1385,
  'ipswich': 1383,
  'bolton': 1318,
  'cardiff': 1607,
  'fulham': 1585,
  'huddersfield': 1522,
#Scottish Premiership
  'celtic': 1570,
  'rangers': 1514,
  'aberdeen': 1403,
  'kilmarnock': 1392,
  'hibernian': 1358,
  'hearts': 1283,
  'motherwell': 1274,
  'stjohnstone': 1236,
  'livingston': 1232,
  'stmirren': 1200,
  'hamilton': 1166,
  'dundee': 1128,
#Bundesliga
  'bayern': 1994,
  'dortmund': 1823,
  'leipzig': 1781,
  'levurkusen': 1761,
  'frankfurt': 1745,
  'hoffenheim': 1727,
  'werder': 1717,
  'wolfsburg': 1704,
  'gladbach': 1693,
  'mainz': 1650,
  'schalke': 1646,
  'hertha': 1637,
  'dusseldorf': 1604,
  'freiburg': 1596,
  'ausburg': 1591,
  'stuttgart': 1578,
#Serie A
  'juventus': 1867,
  'napoli': 1803,
  'roma': 1747,
  'atlanta': 1746,
  'inter': 1730,
  'milan': 1710,
  'torino': 1692,
  'lazio': 1658,
  'sampdoria': 1608,
  'fiorentina': 1591,
  'balogna': 1572,
  'sassuolo': 1565,
  'udinese': 1561,
  'spal': 1550,
  'empoli': 1547,
  'genoa': 1536,
#Campionato Sammarinese di Calcio
  'trefiori': 710,
  'trepenne': 680,
  'lafiorita': 664,
#La Liga
  'barcelona': 1985,
  'atletico': 1876,
  'real': 1839,
  'valencia': 1800,
  'getafe': 1755,
  'sevilla': 1760,
  'espanyol': 1727,
  'villareal': 1725,
  'bilbao': 1732,
  'realsociedad': 1721,
  'eibar': 1700,
  'betis': 1672,
  'levante': 1677,
  'alaves': 1687,
  'celta': 1670,
  'levante': 1657,
#Ligue Un
  'psg': 1822,
  'lyon': 1727,
  'losc': 1664,
  'saint-et': 1637,
  'marseille': 1637,
  'rennes': 1636,
  'nice': 1611,
  'montpellier': 1610,
  'reims': 1569,
  'nantes': 1581,
  'bordeaux': 1561,  
  'monaco': 1541,  
  'strasboug': 1539,  
  'metz': 1522,
  'angers': 1574,  
  'nimes': 1569,  
  'brest': 1509,  
  'toulouse': 1507,  
  'amiens': 1491,  
  'dijon': 1466,
#Other
  'ajax': 1833,
  'porto': 1813,
  'benfica': 1795,
  'salzburg': 1763,
  'partizan': 1571,
  'crvenazvezda': 1545,
  'shaktar': 1761,
  'dinamokyiv': 1763,
  'zenit': 1676,
  'krasnador': 1660,
  'cska': 1650,
}
#I use a differnent dictonary so the program so that you can't enter a team value for competion input and vise versa.
thatdict =	{
#Competions
  'ucl': 83.1,
  'uel': 80.2,
  'england': 61.6,
  'france': 53.1,
  'germany': 55.2,
  'italy': 66.6,
  'spain': 76.5,
  'scotland': 44.7,
  'none': 0,
}
#introduction
def introduction():#This is a function
    print('Welcome to Football Match Predictor Game')
introduction()
#Home Team
home_team = (input('pick home team'))#user input for who home team is
if (home_team) in thisdict:
    home_team_old_value = thisdict[home_team]
else:
    while True:
        try:
            home_team =(input("team not recognised, please type recognised team"))
            if (home_team) in thisdict:
                home_team_old_value = thisdict[home_team]
                break
            else:
                print("please input a positive integer")
        except:
            print("Please input a positive integer")

#Home Field Advantage
competition = (input('enter competion'))
if (competition) in thatdict: #If entered competition is in the list
    home_field_advantage = thatdict[competition]
    home_team_new_value = home_team_old_value + home_field_advantage
else:
    while True:
        try:
            home_field_advantage = int(input("competion not recognised, please type competion"))
            if (home_field_advantage) in thatdict:
                home_field_advantage = thatdict[competition]
                break
            else:
                print("please input a positive integer")
        except:
            print("please input a positive integer")
print (home_team_new_value)

#Away Team
away_team = (input("pick away team"))#user input for who away team is
if (away_team) in thisdict:
    away_team_value = thisdict[away_team]
else:
    while True:
        try:
            away_team = (input("team not recognised, please type recognised team"))
            if (away_team) in thisdict:
                away_team_value = thisdict[away_team]
                break
            else:
                print("please input a positive integer")
        except:
            print("please input a positive integer")
print (away_team_value)

#equations
Qa = 10**(home_team_new_value/400)
Qb = 10**(away_team_value/400)
home_team_percentage = (Qa/(Qa+Qb))*100
away_team_percentage = (Qb/(Qa+Qb))*100

#This prints out the results of the equations
if (home_team) in thisdict:
    print (home_team,'has a',home_team_percentage,'% chance of winning')
else:
    print ('Home team has a',home_team_percentage,'% chance of winning')

if (away_team) in thisdict:
    print (away_team,'has a',away_team_percentage,'% chance of winning')
else:
    print ('Away team has a',away_team_percentage,'% chance of winning')
