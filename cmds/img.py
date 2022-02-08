from quopri import encodestring
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json


with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class Img(Cog_Extension):
    @commands.command()
    async def photo(self,ctx):
        random_pic=random.choice(jdata["random_img"])
        pic=discord.File(random_pic)
        await ctx.send(file=pic)
        
def setup(bot):
    bot.add_cog(Img(bot))    #Img類別裡面