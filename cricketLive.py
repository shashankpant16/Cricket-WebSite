#!/usr/bin/env python
# coding: utf-8

# # CRICKET PYTHON
# ### This program will fetch all live and recently finished cricket matches and will display the scorecard with scoreboard .
# ### Here i have used cricbuzz api, which is easy way to pull out the scores of live matches.
# ### If you want to do the same thing with web scrapping see my "Getting-live-cricket-score-using-python" repository.

# In[1]:


#Importing the necessary libraries.
# !pip install pycricbuzz
from pycricbuzz import Cricbuzz
import pandas as pd

#creating object of Cricbuzz
cb = Cricbuzz()


# In[2]:


#This method will print the basic match information.

def matchInfo(match):
    print(match['srs'],"\n"+match['team1']['name'],' vs ',match['team2']['name'])
    print("**************************************************************")
    print(match['mnum'],"\tToss-> ",match['toss'])
    print("Status: ",match['status'],"\n")
    #print(match['team1']['name']," -> ",match['team1']['squad'])
    #print(match['team2']['name']," -> ",match['team2']['squad'])
    #print("\n\n")


# In[3]:


#This method will display the scorecards of both the teams.

def scorecard(ref):
    for i in ref.values():
        team1_bat = []
        team2_bowl = []
        print(i[0]['batteam'],":",i[0]['runs']," for ",i[0]['wickets'])
        print("Overs : ",i[0]['overs'])
        print("\n\n")
        for j in i[0]['batcard']:
            team1_bat.append(j)
        for k in i[0]['bowlcard']:
            team2_bowl.append(k)
        df_bat = pd.DataFrame(team1_bat,index=range(len(team1_bat)))
        df_bowl = pd.DataFrame(team2_bowl,index=range(len(team2_bowl)))
        df_bat = df_bat[['name','runs','balls','fours','six','dismissal']]
        df_bowl = df_bowl[["name","overs","wickets","runs","maidens","wides","nballs"]]
        print("BATTING\n")
        print(df_bat)
        print("\n\nBOWLING\n")
        print(df_bowl)
        


# In[4]:


#Here is the main calling of the program and both the functions are called in appropriate order

k=1
for i in cb.matches():
    print("\n\n")
    print("############################################## MATCH ",k," ###################################################")
    print("\n\n")
    matchInfo(i)
    try:
        scorecard(cb.scorecard(i['id']))
    #cb.livescore(i['id'])
    except:
        pass
    k+=1
    


# In[ ]:




