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
        
    @commands.command()
    async def aboutme(self,ctx):
        embed=discord.Embed(title="關於 啵啵貓機器人", url="https://github.com/TeemoCaption/DiscordBot_01.git", description="歡迎邀請此機器人至你的伺服器，如果需要修改什麼功能請私訊我Discord", color=0xffa200)
        embed.set_author(name="Discord：MIKU#6148", url="https://discord.com/channels/MIKU#6148", icon_url="https://upload.wikimedia.org/wikipedia/zh/7/7f/Hatsune_Miku_NT.jpg")
        embed.set_thumbnail(url="https://image-resizer.cwg.tw/resize/uri/https%3A%2F%2Fstorage.googleapis.com%2Fwww-cw-com-tw%2Farticle%2F201810%2Farticle-5bd182cf13ebb.jpg/?w=1600&format=webp")
        embed.add_field(name="貓咪小舖（GTA5輔助販售）", value="https://discord.gg/HzrSyghBDu", inline=False)
        embed.set_footer(text="喵~")
        await ctx.send(embed=embed)
        
        
def setup(bot):
    bot.add_cog(Main(bot))    #Main類別裡面