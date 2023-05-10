import discord
from discord.ext import commands

class events(commands.Cog):

    def __init__(self, bot: discord.Bot):

        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        
        print(f'Estou conectado como {self.bot.user.name}')
        print(self.bot.user.id)

        await self.bot.change_presence(status = discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name='Oiieee'))

def setup(bot: commands.Bot):
    bot.add_cog(events(bot))