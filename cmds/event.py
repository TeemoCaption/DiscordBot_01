from msilib.schema import Class
from quopri import encodestring
import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension    #從core資料夾內的classes.py檔案中引用Cog_Extension



with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)


class Event(Cog_Extension):
    
    @commands.Cog.listener()   #監聽觸發性事件  
    async def on_member_join(self,member):     #成員加入
        channel=self.bot.get_channel(int(jdata['welcome_channel']))       #get_channel("頻道id")=>取得頻道
        await channel.send(f"{member} 跳進來了")      #發送訊息

    @commands.Cog.listener()     
    async def on_member_remove(self,member):     #成員離開
        channel=self.bot.get_channel(int(jdata['leave_channel']))       #get_channel("頻道id")=>取得頻道
        await channel.send(f"{member} 離開了")
    
    @commands.Cog.listener()     
    async def on_message(self,msg):   
        if msg.content=="嗨" and msg.author != self.bot.user:
            await msg.channel.send("哈囉! "+msg.author)
            
        if msg.content=="2T" or msg.content=="2t":
            pic=discord.File(jdata['photo']['2T'])
            await msg.channel.send(file=pic)
        elif msg.content=="21Lua":
            pic=discord.File(jdata['photo']['21lua'])
            await msg.channel.send(file=pic)
        elif msg.content=="午夜":
            pic=discord.File(jdata['photo']['午夜'])
            await msg.channel.send(file=pic) 
        elif msg.content=="FK":
            pic=discord.File(jdata['photo']['FK'])
            await msg.channel.send(file=pic)  
        elif msg.content=="幻影":
            pic=discord.File(jdata['photo']['幻影'])
            await msg.channel.send(file=pic)   
        elif msg.content=="表演者":
            pic=discord.File(jdata['photo']['表演者'])
            await msg.channel.send(file=pic)   
        elif msg.content=="威脅":
            pic=discord.File(jdata['photo']['威脅'])
            await msg.channel.send(file=pic) 
        elif msg.content=="毒液":
            pic=discord.File(jdata['photo']['毒液'])
            await msg.channel.send(file=pic)
        elif msg.content=="軌道":
            pic=discord.File(jdata['photo']['軌道'])
            await msg.channel.send(file=pic)  
        elif msg.content=="氩氣":
            pic=discord.File(jdata['photo']['氩氣'])
            await msg.channel.send(file=pic)  
        elif msg.content=="氪金":
            pic=discord.File(jdata['photo']['氪金'])
            await msg.channel.send(file=pic)  
        elif msg.content=="殘月":
            pic=discord.File(jdata['photo']['殘月'])
            await msg.channel.send(file=pic) 
        elif msg.content=="菲拉":
            pic01=discord.File(jdata['photo']['菲拉01'])
            await msg.channel.send(file=pic01)
            pic01=discord.File(jdata['photo']['菲拉02'])
            await msg.channel.send(file=pic02)
        elif msg.content=="開拓者":
            pic=discord.File(jdata['photo']['開拓者'])
            await msg.channel.send(file=pic)
        elif msg.content=="黃昏":
            pic=discord.File(jdata['photo']['黃昏'])
            await msg.channel.send(file=pic)
        elif msg.content=="新星":
            pic=discord.File(jdata['photo']['新星'])
            await msg.channel.send(file=pic)
        elif msg.content=="暗星":
            pic=discord.File(jdata['photo']['暗星'])
            await msg.channel.send(file=pic)
        elif msg.content=="碎片":
            pic=discord.File(jdata['photo']['碎片'])
            await msg.channel.send(file=pic)
        elif msg.content=="電路":
            pic=discord.File(jdata['photo']['電路'])
            await msg.channel.send(file=pic)
        elif msg.content=="搗亂":
            pic=discord.File(jdata['photo']['搗亂'])
            await msg.channel.send(file=pic)
        elif msg.content=="騎士" or msg.content=="KM":
            pic=discord.File(jdata['photo']['騎士'])
            await msg.channel.send(file=pic)
        elif msg.content=="櫻桃":
            pic=discord.File(jdata['photo']['櫻桃'])
            await msg.channel.send(file=pic)
        elif msg.content=="JF":
            pic=discord.File(jdata['photo']['JF'])
            await msg.channel.send(file=pic)
        elif msg.content=="OX":
            pic=discord.File(jdata['photo']['OX'])
            await msg.channel.send(file=pic)
        elif msg.content=="Stand" or msg.content=="stand":
            pic=discord.File(jdata['photo']['Stand'])
            await msg.channel.send(file=pic)
        elif msg.content=="VVS":
            pic=discord.File(jdata['photo']['VVS'])
            await msg.channel.send(file=pic)
        elif msg.content=="XF":
            pic=discord.File(jdata['photo']['XF'])
            await msg.channel.send(file=pic)
        elif msg.content=="Zero菜單" or msg.content=="zero菜單":
            pic=discord.File(jdata['photo']['Zero菜單'])
            await msg.channel.send(file=pic)
        elif msg.content=="zero lua":
            pic=discord.File(jdata['photo']['zero lua'])
            await msg.channel.send(file=pic)
        elif msg.content=="SF lua":
            pic=discord.File(jdata['photo']['SFlua'])
            await msg.channel.send(file=pic)
        
        
def setup(bot):
    bot.add_cog(Event(bot))    #Main類別裡面