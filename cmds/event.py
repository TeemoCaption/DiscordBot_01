from msilib.schema import Class
from quopri import encodestring
from xml.sax.handler import feature_external_ges
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
        await channel.send(f"{member} \n跳進來了")      #發送訊息

    @commands.Cog.listener()     
    async def on_member_remove(self,member):     #成員離開
        channel=self.bot.get_channel(int(jdata['leave_channel']))       #get_channel("頻道id")=>取得頻道
        await channel.send(f"{member} \n離開了")
    
    @commands.Cog.listener()     
    async def on_message(self,msg):   
        keyword=["嗨","哈囉","你好","有人嗎"]
        keyword2=["輔助推薦"]
        keyword3=["全能型"]
        keyword4=["最強科技"]
        keyword5=["崩潰防護型"]
        keyword6=["中等型"]
        keyword7=["模組型"]
        keyword8=["任務型"]
        keyword9=["刷錢型"]
        keyword10=["2TAKE腳本","2take腳本"]
        keyword11=["營業時間"]
        
        if  msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send("哈囉!需要什麼幫助?常見提問有:\n輔助推薦\n營業時間\n\n")
        elif  msg.content in keyword2 and msg.author != self.bot.user: 
            await msg.channel.send("目前可分為幾種輔助：\n全能型\n最強科技\n崩潰防護型\n中等型\n模組型\n任務型\n刷錢型\n2TAKE腳本\n\n")
        
        elif msg.content in keyword3 and msg.author != self.bot.user:
            await msg.channel.send(jdata["command"]["con"])
                    
        elif msg.content in keyword4 and msg.author != self.bot.user:
            await msg.channel.send(jdata["command"]["con2"])
                
        elif msg.content in keyword5 and msg.author != self.bot.user:
            await msg.channel.send(jdata["command"]["con3"])
                
        elif msg.content in keyword6 and msg.author != self.bot.user:
            await msg.channel.send(jdata["command"]["con4"])
                
        elif msg.content in keyword7 and msg.author != self.bot.user:
            await msg.channel.send(jdata["command"]["con5"])
                
        elif msg.content in keyword8 and msg.author != self.bot.user:
            await msg.channel.send(jdata["command"]["con6"])
                
        elif msg.content in keyword9 and msg.author != self.bot.user:
            await msg.channel.send(jdata["command"]["con7"])
                
        elif msg.content in keyword10 and msg.author != self.bot.user:
            await msg.channel.send(jdata["command"]["con8"])
        elif  msg.content in keyword11 and msg.author != self.bot.user:
            await msg.channel.send("由於開學關係(本人大學生)，回覆時間通常在下午5、6點那邊(禮拜三例外)有需要什麼請私訊群主或打在交流區那邊，有時候在忙可能會慢回請見諒")
            
                
            
        
            
        if msg.content=="2T" or msg.content=="2t" or msg.content=="2TAKE" or msg.content=="2take":
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
        elif msg.content=="JF" or msg.content=="jf":
            pic=discord.File(jdata['photo']['JF'])
            await msg.channel.send(file=pic)
        elif msg.content=="OX" or msg.content=="ox":
            pic=discord.File(jdata['photo']['OX'])
            await msg.channel.send(file=pic)
        elif msg.content=="Stand" or msg.content=="stand":
            pic=discord.File(jdata['photo']['Stand'])
            await msg.channel.send(file=pic)
        elif msg.content=="VVS":
            pic=discord.File(jdata['photo']['VVS'])
            await msg.channel.send(file=pic)
        elif msg.content=="XF" or msg.content=="xf":
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