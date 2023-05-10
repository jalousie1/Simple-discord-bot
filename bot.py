import discord, os
from discord.ext import commands
from key import token

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)
TOKEN = token.get('TOKEN')

for filename in os.listdir('./commands'):
    
    if filename.endswith('.py') and not filename.startswith('__'):
            
            client.load_extension('commands.{0}'.format(filename[:-3]))

for filename in os.listdir('./plugins'):
    
    if filename.endswith('.py') and not filename.startswith('__'):
            
            client.load_extension('plugins.{0}'.format(filename[:-3]))

#@client.event - Não usei pq ja estou usando na pasta events
#async def on_ready():
    #print(f'Bot conectado como:')
    #print(client.user.name)
    #print(client.user.id)

    #await client.change_presence(status = discord.Status.streaming, activity=discord.Activity(type=discord.ActivityType.watching, name='Oiieee'))

client.run(TOKEN)