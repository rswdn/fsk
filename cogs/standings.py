import discord 
from discord.ext import commands
from sleeper_wrapper import League
import pandas as pd
from tabulate import tabulate
from db_connect import connection
import re

c = connection.cursor()

#bot command to get the standings for the requested league, will work for any sleeper league as logn as you have the league ID.

class Standings(commands.Cog):

    def __init__(self,client):
        self.client = client


    @commands.command(name='standings', help='Get standings for the requested league')
    async def get_standings(self,ctx,arg):
        try:
            c.execute("SELECT league_number FROM league WHERE league_name = %s;",(arg,))
            rows = c.fetchall()
            if len(rows) == 0: #if none found, return error
                await ctx.send('No league found.')
            else:
                self.results = str(re.sub(r"[]),[('']", '', str(rows))) #stripping results of query so it can be passed to the table
                self.league = League(self.results)
                self.league_name = self.league.get_league()
                self.rosters = self.league.get_rosters()
                self.users = self.league.get_users()
                self.standings = self.league.get_standings(self.rosters,self.users)
                self.df = pd.DataFrame.from_dict(self.standings) #returning the standings as a dataframe
                self.results = (self.df[self.df.columns[[0,1,2]]])#closing which columns to return
                self.results['W/L']=self.results[1] + '-'+ self.results[2]#adding the 'W/L' ratio
                self.table_data = self.results.drop([1,2], axis=1) #dropping the 2 W/L columns as they are no longer needed
                self.table = "```" + tabulate(self.table_data, headers=['Name','W/L'], showindex=False, tablefmt='plain') + "```" #formatting the table   
                self.embed = discord.Embed(title=self.league_name['name'] + ' ' + 'Standings', description=self.table, colour=15844367) #setting up the table to be embeded
                await ctx.send(embed=self.embed)

        except Exception:
            connection.rollback()
            await ctx.send('Whoops, something went wrong')


def setup(client):#setting up the disocrd client, must have this for COGS to work!
    client.add_cog(Standings(client))


