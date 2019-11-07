import requests
import discord
from discord.ext import commands

def get_verse():
    return requests.get("http://www.ourmanna.com/verses/api/get?format=text&order=random").text.replace("God", "Alan")

bot = commands.Bot(command_prefix = "+")

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="type +alan"))

@bot.command(name="alan", help = "response with a verse from the bible")
async def send_verse(ctx):
        response = get_verse()
        await ctx.send(response)
bot.run("NjQxOTE5NDI1MzMwNjc1NzEz.XcPYWw.oYogV-zu0X2qQ68UZWV3ls9Q2Vw")
