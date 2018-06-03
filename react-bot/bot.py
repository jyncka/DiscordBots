import discord
import json
from discord.ext import commands

bot = commands.Bot(command_prefix='$', description='A bot that embeds reactions for you.')
bot.remove_command('help')

@bot.event
async def on_ready():
	print("Logged in as")
	print(bot.user.name)
	print(bot.user.id)
	print('----')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="react bot", description="A bot that embeds reaction gifs and images for you.", color=0xeee657)
    
    # give info about you here
    embed.add_field(name="Author", value="jyncka")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](https://discordapp.com/api/oauth2/authorize?client_id=452581331046498324&permissions=18432&scope=bot)")

    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="react bot", description="A bot that embeds reaction gifs and images for you. List of commands are:", color=0xeee657)
    embed.add_field(name="$react", value="Type `$react [reaction]` to have React Bot embed an image link.")
    embed.add_field(name="$list", value="Lists available reactions - make sure you type them as they appear here.")
    
    await ctx.send(embed=embed)

@bot.command()
async def list(ctx):
	embed = discord.Embed(title="reaction list", description="Here are the available reactions for this server:", color=0xeee657)
	embed.add_field(name="lizard-king", value="$react lizard-king")
	embed.add_field(name="i-know", value="$react i-know")
	embed.add_field(name="lewd", value="$react lewd")
	embed.add_field(name="pigeon", value="$react pigeon")
	embed.add_field(name="ping", value="$react ping")
	embed.add_field(name="shout", value="$react shout")
	embed.add_field(name="stray", value="$react stray")
	embed.add_field(name="tell-me", value="$react tell-me")

	await ctx.send(embed=embed)

@bot.command()
async def react(ctx, reaction):
	with open('reactions.json', 'r') as f:
		data = json.load(f)

	if reaction in data['reactions']:
		await ctx.send(data['reactions'][reaction])
	else:
		await ctx.send("Looks like I don't have that, maybe you should suggest it?")

@react.error
async def react_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		print("no reaction")
		await ctx.send("Uh oh! You didn't give me a reaction!")

bot.run('NDUyNTgxMzMxMDQ2NDk4MzI0.DfTXpQ.FqIzJzRx5I4dqcoMIggVQog-NEk')
