import discord
from discord.ext import commands
from discord import Asset, slash_command, option

class foto(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:

        self.bot = bot

    @slash_command(name="foto", guild_only = True, description="Mostra a foto do usuário")
    @option(name="member", description="Precisa escolher alguem")

    async def foto(self, Interaction: discord.Interaction, member: discord.Member = None):
        if member == None:
            await Interaction.response.send_message(content = 'Precisa escolher alguem', ephemeral = True)
        else:
            embed = discord.Embed(title="", description=f'{member.mention} ', color = discord.Color.from_rgb(214, 140, 237))
            embed.set_author(name=f"{member.name}'s Avatar", icon_url=member.display_avatar)
            embed.set_image(url=member.display_avatar)

            await Interaction.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(foto(bot))