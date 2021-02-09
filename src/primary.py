import discord
from database import DB
from discord.ext import commands
import qrcodegen as qr
import config

class Bot(discord.Client):
    database = DB()

client = commands.Bot(command_prefix="m!")

async def on_ready(self):
    print(self.user.name + "has been deployed!")
    await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"QR codes!"))

@client.command()
async def qrcode(message):
    qr.qrGen.create()
    file = discord.File("assets/qrcode_test.png", filename="qrcode_test.png")
    embed= discord.Embed(title="QR Code", description = "Scan this to get a free token!", color = 0xffffff)
    embed.set_image(url = "attachment://qrcode_test.png")
    i = Bot.database.find_points(message.author.id)
    if i == False:
        i = 0
    await message.channel.send(file=file, embed=embed)
    Bot.database.update_points(int(message.author.id), int(i) + 1)

client.run(config.TOKEN)

