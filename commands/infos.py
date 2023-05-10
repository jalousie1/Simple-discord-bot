import discord
from discord.ext import commands
from discord import slash_command, option

class infos(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:

        self.bot = bot 

    @slash_command(name="infos", guild_only = True, description="Informações da conta")
    @option(name="user", description="Precisa escolher alguem") 

    async def infos(self, Interaction: discord.Interaction, member: discord.Member = None):
        if member == None:
            await Interaction.response.send_message(content = 'Precisa escolher alguem', ephemeral = True)
        else:
            embed = discord.Embed(title="", description=f'', color = discord.Color.from_rgb(214, 140, 237))
            embed.set_thumbnail(url = member.display_avatar)
            embed.add_field(name=":moyai: Nome", value=member.name, inline=True)
            embed.add_field(name="ID", value=member.id, inline=True)
            embed.add_field(name="Status", value=member.status, inline=True)
            embed.add_field(name="Nickname", value=member.nick, inline=True)
            embed.add_field(name="Conta criada em", value=member.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"), inline=True)
            embed.add_field(name="Entrou no servidor em", value=member.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"), inline=True)

            await Interaction.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(infos(bot))