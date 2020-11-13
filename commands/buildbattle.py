import discord
from discord.ext import commands
from aiohttp import ClientSession
from mojang import MojangAPI
from configparser import ConfigParser
from utils.utils import utils
import random

parser = ConfigParser()
parser.read('botconfig.ini')
API_KEY = parser.get('CONFIG', 'api_key')

class BuildBattleCMD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.session = ClientSession()

    @commands.command(aliases=['bb'])
    async def buildbattle(self, ctx, username:str=None):
        try:
            #verify if player exists
            if username==None:
                embed = discord.Embed(title="Error", description="""Please provide a username.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
            uuid = MojangAPI.get_uuid(str(username))
            if uuid == '5d1f7b0fdceb472d9769b4e37f65db9f':
                embed = discord.Embed(title="Error", description="""That user does not exist.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
            elif not uuid:
                embed = discord.Embed(title="Error", description="""That user does not exist.""", color=0xff0000)
                await ctx.send(embed=embed)
                return
            #send request
            async with self.session.get('https://api.hypixel.net/player?key=' + API_KEY + '&uuid=' + uuid) as response:
                data = await response.json()
            #errors
            if data['success'] == False:
                if data['cause'] == 'Malformed UUID':
                    embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                    await ctx.send(embed=embed)
                    return
                else:
                    embed = discord.Embed(title="Error", description="""Something went wrong.""", color=0xff0000)
                    await ctx.send(embed=embed)
                    return
            #it worked!
            elif data['success'] == True:
                if data['player'] == None:
                    embed = discord.Embed(title="Error", description="""That user has never joined the Hypixel Network.""", color=0xff0000)
                    await ctx.send(embed=embed)
                    return
            try:
                wins = data['player']['stats']['BuildBattle']['wins']
            except:
                wins = 'N/A'
            try:
                played = data['player']['stats']['BuildBattle']['games_played']
            except:
                played = 'N/A'
            try:
                coins = data['player']['stats']['BuildBattle']['coins']
            except:
                coins = 'N/A'
            async with self.session.get("https://sessionserver.mojang.com/session/minecraft/profile/" + uuid) as response:
                data = await response.json()
            color=random.randint(1, 16777215)
            embed = discord.Embed(title=data['name'] + "'s Build battle Stats", color=color)
            embed.set_thumbnail(url='https://crafatar.com/avatars/' + uuid)
            embed.add_field(name='Games Played', value=str(utils.comma(played)))
            embed.add_field(name='Wins', value=str(utils.comma(wins)))
            embed.add_field(name='Coins', value=str(utils.comma(coins)))
            await ctx.send(embed=embed)
        except discord.Forbidden:
            try:
                await ctx.send("Error: Cannot send embeds in this channel. Please contact a server administrator to fix this issue.")
                return
            except discord.Forbidden:
                try:
                    await ctx.author.send("Error: Cannot send messages in that channel. Please contact a server administrator to fix this issue.")
                except discord.Forbidden:
                    return
        
        

def setup(bot):
    bot.add_cog(BuildBattleCMD(bot))