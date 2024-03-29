import discord
from discord.ext import commands
from discord import app_commands
import os
from db_connect import connection
            
c = connection.cursor()
GUILD = os.getenv('GUILD_ID')
#function that allows user to assign leagues to names of their choice
class Assign(commands.Cog):

    def __init___(self,bot:commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name='assign')
    @app_commands.checks.has_role('Admin')#Ensuring the approiate role is met, will be diffeerent for each server... must ensure user has the role to be able to use the below function
    async def assign_league(self, interaction: discord.Interaction,league: str, number:str) -> None:

        """Assign league name to league ID"""
        self.league_number = number
        self.league_name = league
        
        try:
            c.execute("SELECT * FROM league WHERE league_name = %s;",(self.league_name,))
            rows = c.fetchall()

            if len(rows) == 0:
                c.execute("INSERT INTO league (league_name,league_number) VALUES(%s,%s)",(self.league_name,self.league_number,))
                connection.commit()
                return await interaction.response.send_message('League successfully assigned.')

            else:
                return await interaction.response.send_message('League name or number already exists, please try again with a different combination.')

        except Exception:
                connection.rollback()
                return await interaction.response.send_message('Whoops, something went wrong')

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Assign(bot), guilds=[discord.Object(id=GUILD)])

