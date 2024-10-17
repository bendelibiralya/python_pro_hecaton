import discord
from discord.ext import commands
from dtoken import token 

#yetkiler
intents = discord.Intents.default()
intents.message_content = True
#normalde yazının başında yazan $
bot = commands.Bot(command_prefix= '!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f"""Welcome to the discord channel of our Climatechangeisreal website! I am {bot.user}, and I am ready to help you! You can say '!helppls' to learn more about our website or you can say '!more' to learn about my commands and what you can do here.""")

@bot.command()
async def helppls(ctx):
    await ctx.send("Our website is created to help you make your poster and raise awareness on our World's biggest problem climate change! It is pretty easy to make your poster. You just have to open the website, press 'start your poster' button, choose the image you would like to use and the text you wanna add, decide on your texts color and the frame color of your image (if you want one), choose the position of your text and press 'crete poster'. Ta-da! You poster is ready! If you want help with the positions of your texts just write '!whatposition' and I will help you!")

@bot.command()
async def whatposition(ctx):
    await ctx.send(""""I will tell you the best positions for each image:
                   photo number: upper text position - lower text position
                   1: 140 - 140
                   2: 285 - 285
                   3: 295 - 295
                   4: 170 - 170
                   5: 130 - 130
                   6: 225 - 225
                   7: 125 - 125
                   8: 140 - 125 (I don't reccomend using white for the lower text here)
                   9: 125 - 125
                   10: 125 - 125
                   11: 130 - 130
                   12: 140 - 140
                   13: 180 - 180 (I don't reccomend using white for both texts here)
                   14: 150 - 150 (I don't reccomend using white for both texts here)
                   15: 135 - 135
                   16: 150 - 150 (I don't reccomend using white for both texts here)
                   17: 190 - 190
                   18: 130 - 130
                   19: 180 - 180 (I don't reccomend using white for both texts here)
                   20: 130 - 130
                   21: 220 - 220
                   22: 155 - 155 (I don't reccomend using black for both texts here)""")

@bot.command()
async def more(ctx):
    await ctx.send("""I have some commands to help you with your posters such as 
    - '!sloganidea' to give you ideas for your slogan
- '!photo' to tell you how to save your posters
- '!whatposition' to help you choose the best position for your text in each image on our website

Instead of these, you can have fun here in our discord server. We have a chitchat voice area, posters area, games area and a lot more to come!""")

@bot.command()
async def sloganidea(ctx):
    await ctx.send("")

@bot.command()
async def photo(ctx):
    await ctx.send("")

@bot.command()
async def feedback(ctx):
    await ctx.send("Hello and welcome to the feedback channel! Feel free to tell us about your opinions and suggestions here. We assure you that we will attach importance to them!")

@bot.command()
async def myposter(ctx):
    await ctx.send("Hello and welcome! This are is made for you to share your posters and comment on each others posters. Don’t forget to send your posters screenshot here!")

bot.run(token)