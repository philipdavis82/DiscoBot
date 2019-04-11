import discord
from discord.ext import commands
import tools


TOKEN = 'NTY1NjY5MzQyNTk1OTA3NjE1.XK53EA.4RJyFJGeUPxMmyH0jwheiV0UfpU'

bot = commands.Bot(command_prefix='!')
roller = tools.dice_commander()
with open('help.txt') as file:
    help_text = file.read()

@bot.command()
async def test(ctx):
    await ctx.send('Fuck You! {0}'.format(ctx.author))

@bot.command()
async def roll(ctx,args,cmd='all'):
    #await ctx.send(cmd)
    try:
        amount,die = args.split('d')
        amount = int(amount)
        die = int(die)
    except:
        await ctx.send('Try Agian, I believe in you!')
    else:
        try:
            await ctx.send(roller.commands[cmd](dice = die,amount = amount))
        except:
            await ctx.send("Dice Commander Failed")

@bot.command()
async def last(ctx,cmd='nan'):
    try:
        await ctx.send(roller.commands['last']())
    except:
        await ctx.send("Dice Commander Failed")

@bot.command()
async def cmds(ctx,cmd='nan'):
    if ctx == "Seadia":
        await ctx.send("AHHHHHHHHHHHHHHHHHH")
    else:
        try:
            await ctx.send(help_text)
        except:
            await ctx.send("??????????")




bot.run(TOKEN)

#"C:\ProgramData\Anaconda3\envs\default\envs\python36"