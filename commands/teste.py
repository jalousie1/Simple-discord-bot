import discord
from discord.ext import commands
from discord import Asset, slash_command, option

class teste(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:

        self.bot = bot

    @slash_command(name = 'baa', guild_only = True, description = 'Aaaaaaab')
    @option(name = 'member', description = 'Mencione um membro')

    async def aaa(self, Interaction: discord.Interaction, member: discord.Member = None):
        
        if member == None: member = Interaction.user

        await Interaction.response.send_message(f'Olá {member.mention}!')



def setup(bot: commands.Bot):
    bot.add_cog(teste(bot))