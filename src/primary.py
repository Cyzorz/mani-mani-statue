import discord
from database import DB
from discord.ext import commands
from asset import Asset
import qrcodegen as qr
import config

class Bot(discord.Client):
    database = DB()

client = commands.Bot(command_prefix=config.COMMAND_PREFIX)
client.remove_command('help')

@client.event
async def on_ready():
    print("Mani-Mani Statue has been deployed!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"QR codes!"))

@client.command(description = "Generates a QR Code for the user to use to claim a free token")
async def qrcode(message):
    qr.qrGen.create()
    embed= discord.Embed(title="QR Code", description = "Scan this to get a free token!", color = 0xffffff)
    embed.set_image(url = "attachment://qrcode_test.png")
    i = Bot.database.find_points(message.author.id)
    if i == False:
        i = 0
    await message.channel.send(file=Asset.getFile('qrcode_test.png'), embed=embed)
    Bot.database.update_points(int(message.author.id), int(i) + 1)

@client.command(description = "Pong!")
async def ping(message):
    await message.channel.send("Pong!")

@client.command(description = "Returns a list of available commands for the user to use")
async def help(message):
    command_list = ""
    for command in client.commands:
        command_list += f"`{config.COMMAND_PREFIX}{command}` **-** {command.description}\n\n"
    embed = discord.Embed(title = "Mani-Mani Statue Help", description = f"Please use `{config.COMMAND_PREFIX}` before every command!\nList of available commands:\n\n" + command_list)
    embed.set_thumbnail(url = client.user.avatar_url)
    await message.channel.send(embed=embed)

client.run(config.TOKEN)

