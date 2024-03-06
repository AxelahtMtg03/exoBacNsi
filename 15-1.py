def mini(releve:list,date:list)->tuple:
    minireleve=releve[0]
    minidate=date[0]
    for i in range(len(releve)):
        if releve[i]<minireleve:
            minireleve=releve[i]
            minidate=date[i]
    return(minireleve,minidate)

t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

print(mini(t_moy, annees))