from pandas import *
from ggplot import *

import pandas

def lineplot(filename): #one line graph with titles
    h = pandas.read_csv(filename)
    gg = ggplot(h, aes('yearID', 'HR')) + geom_point(color ='red') + geom_line(color='red')
    + ggtitle('Total HRs by Year') + xlab('Year') + ylab('HR)
    return gg

####################

def lineplot_compare(hr_by_team_year_sf_la_csv):

    # This csv file has three columns: yearID, HR, and teamID. The data in the
    # file gives the total number of home runs hit each year by the SF Giants 
    # (teamID == 'SFN') and the LA Dodgers (teamID == "LAN"). Produce a 
    # visualization comparing the total home runs by year of the two teams. 

    h = pandas.read_csv(hr_by_team_year_sf_la_csv)
    gg = ggplot(h, aes('yearID', 'HR', color='teamID')) + geom_point() + geom_line()
    return gg
