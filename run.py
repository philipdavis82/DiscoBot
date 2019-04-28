import discord
from discord.ext import commands
import tools
from tree import Tree


with open('TOKEN.txt') as file:
        TOKEN = file.read()

bot = commands.Bot(command_prefix='!')
roller = tools.dice_commander()


@bot.command()
async def test(ctx):
    arth,_ = str(ctx.author).split('#')
    if arth == "DumDum":
        await ctx.send("AHHHHHHHHHHHHHHHHHH")
    else:
        author = str(ctx.author)
        author,_ = author.split('#')
        await ctx.send('Hello {0}!'.format(author))

@bot.command()
async def roll(ctx,args='1d1',cmd='all'):
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
async def edit(ctx,tolerance = '30',step = '0.5',link='nan'):
    await ctx.send("I'll get on it")
    import video
    if True:
        try:
            video_path = video.download(link)
            tolerance = int(tolerance)
            step = float(step)
        except:
            await ctx.send("Oh God")
        else:
            ve = video.VideoEditer(tolerance=tolerance)
            ve.extract_audio()
            null_video = ve.run()
            try:
                ds_video = discord.File(null_video)
            except:
                await ctx.send(null_video)
            else:
                await ctx.send("Here it is",file=ds_video)

    if False:
        video_path = video.download(link)
        ve = video.VideoEditer()
        ve.extract_audio()
        null_video = ve.run()
        ds_video = discord.File(null_video)
        await ctx.send("Here it is",file=ds_video)

    
@bot.command()
async def tree(ctx,atts=None):
    await ctx.send("Oh Boy, A Tree!!")
    try:
        atts = atts.split(",")
        kwargs = {}
        for att in atts:
            att = att.split("=")
            try:
                att[1] = int(att[1])
            except:
                try:
                    att[1] = float(att[1])
                except:
                    att[1] = att[1]
            kwargs[att[0]] = att[1]
        tre=Tree(**kwargs)
    except:
        print("Exception")
        tre = Tree()

    tre.makeBranches([tre.start],*tre.start_args)
    ds_tree = discord.File("E:/Trees/tree.png")
    await ctx.send("Here it is",file=ds_tree)
    

        
    

@bot.command()
async def h(ctx,cmd='nan'):
    with open('help.txt') as file:
        help_text = file.read()
    arth,_ = str(ctx.author).split('#')
    if arth == "Seadia":
        await ctx.send("AHHHHHHHHHHHHHHHHHH")
        await ctx.send(help_text)
    else:
        try:
            await ctx.send(help_text)
        except:
            await ctx.send("??????????")

'''@bot.command(pass_context=True)
async def clear(ctx,number='1'):
    #channel = discord.TextChannel()
    channel = ctx.channel
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for messege in channel.history(limit = number):
        mgs.append(messege)
        await messege.delete()'''


bot.run(TOKEN)

#"C:\ProgramData\Anaconda3\envs\default\envs\python36"