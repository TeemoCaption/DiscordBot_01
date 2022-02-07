from msilib.schema import Class
from quopri import encodestring
import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension    #從core資料夾內的classes.py檔案中引用Cog_Extension


class Main(Cog_Extension):
    
    @commands.command()
    async def ping(self,ctx):     #打指令    ctx全名叫context
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')
        
def setup(bot):
    bot.add_cog(Main(bot))    #Main類別裡面