from discord.ext.commands import Bot
import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
     print('Logged in as')
     print(client.user.name)
     print(client.user.id)
     print('I am Ready')



@client.event
async def on_member_remove(member):
        print("Recognised that a member called " + member.name + " left.")
        embed=discord.Embed(title="Good-Bye! , " + member.name, color=discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name="💥THE BEST💥", icon_url="https://cdn.discordapp.com/attachments/651838504220885010/658640882937102347/JPEG_20191002_104501.jpg")
        embed.set_thumbnail(url= member.avatar_url)  
        embed.add_field(name="I hope you enjoyed ",value="**With us.**", inline=False)
        embed.set_footer(text="Made with ♥ by ⎝⧹𝗗𝗿. BOSS™╱⎠#0928", icon_url="https://cdn.discordapp.com/attachments/651838504220885010/658640882496569355/images_1.jpeg")
        await client.send_message(client.get_channel("657140154774978581"), embed=embed)
        print("Sent message to good-bye channel")

@client.event
async def on_member_join(member):
        print("Recognised that a member called " + member.name + " joined")
        embed=discord.Embed(title="Welcome to The best, " + member.name, description="Thanks for join server", color=0xFF3366)
        embed.set_author(name="💥 THE BEST 💥", icon_url="https://cdn.discordapp.com/attachments/651838504220885010/658640882937102347/JPEG_20191002_104501.jpg")
        embed.set_thumbnail(url= member.avatar_url)
        embed.add_field(name="This is the best Discord Server for Trivia Games!", value="Enjoy the **THE_BEST**", inline=False)
        embed.set_footer(text="Made with ♥ by ⎝⧹𝗗𝗿. BOSS™╱⎠#0928", icon_url="https://cdn.discordapp.com/attachments/651838504220885010/658640882496569355/images_1.jpeg")
        await client.send_message(member, embed=embed)
        await client.send_message(client.get_channel("657140098877358080"), embed=embed)
        print("Sent message to " + member.mention)

@client.command(pass_context=True)
async def crates(ctx):
    embed = discord.Embed(color=(random.randint(0, 0xffffff)))
    embed.add_field(name="Crates Avaliable", value="King Crate \n Savage Crate \n Med Crate")
    embed.add_field(name="How to get them", value="**Type ?crate for a random crate out of those 3**")
    await client.say(embed=embed)
	

     


client.run("NjQ0MjM0OTM4NDM4MTIzNTQx.XgG92w.jG_VsZE8dTHofj30uK7WxdT8SAI")



