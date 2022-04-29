from ctypes import Union
from msilib import sequence
from typing import Optional, Sequence
import lightbulb
import hikari
import datetime
import os
from dotenv import load_dotenv
import requests 

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

#bad bad bad enifficent code
#I GIVE UP IF IT WORKS IT WORKS

def verse_funct_text(r):
    
    #getting the text of the verse
    finaltxt = str(r.text)
    finaltxt = finaltxt.split("bilingual-left", 1)
    finaltxt = finaltxt[1]
    finaltxt = finaltxt.split("div", 1)
    finaltxt = finaltxt[0]
    finaltxt = finaltxt.replace(">", "") 
    finaltxt = finaltxt.replace("<", "") 
    final_verse_text = finaltxt + '"'
    
    #getting the verse number(id? idk) of the verse
    finaltxt = str(r.text)
    finaltxt = finaltxt.split("Verse of the Day:", 1)
    finaltxt = finaltxt[1]
    finaltxt = finaltxt.split('"/>', 1)
    finaltxt = finaltxt[0]
    final_verse_text =  final_verse_text +" -" + finaltxt

    print(final_verse_text)
    return(final_verse_text)


def verse_funct_image(r):

    #getting the image of the verse
    finaltxt = str(r.text)
    finaltxt = finaltxt.split("fb-comments", 1)
    finaltxt = finaltxt[1]
    finaltxt = finaltxt.split("data-num-posts=", 1)
    finaltxt = finaltxt[0]
    finaltxt = finaltxt.replace('" data-href="', "") 
    final_verse_image = finaltxt.replace('"', "") 

    print(final_verse_image)
    return(final_verse_image)


#calculating days until next camp
today = datetime.date.today()
future = datetime.date(2022,7,17)
diff = future - today
days_until = str(diff.days)


#authing discord bot
bot = lightbulb.BotApp(
    token=TOKEN,
    default_enabled_guilds=(733440457618620417)
)

#check for the discord bot starting
@bot.listen(hikari.StartedEvent)
async def on_start(event):
    print("dish bot Esh workin")



#sayying the ammount of days when called
@bot.command
@lightbulb.command("time-until-camp", "tells you the ammount of days until the next camp")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("It is {} days until camp!" .format(days_until))

@bot.command
@lightbulb.command("website", "the bot github website!")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("https://github.com/Ethaisa123/Willow-discord-bot")


#BOT COMMAND FOR VERSE
@bot.command()
@lightbulb.option("verse", "type of verse shown", choices=["verse-text", "verse-image"], required=True)
@lightbulb.command("verse-of-the-day", "a random verse every day")
@lightbulb.implements(lightbulb.SlashCommand)
async def echo(ctx):
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get('https://www.verseoftheday.com/', params=payload)
    
    if ctx.options.verse == "verse-text":
        await ctx.respond(verse_funct_text(r))
    elif ctx.options.verse == "verse-image":
        await ctx.respond(verse_funct_image(r))
    



#BOT COMMAND FOR PLAYLIST
@bot.command()
@lightbulb.option("camps", "the song playlists from different camps", choices=["futuristic-camp", "retro-camp", "general-playlist"], required=True)
@lightbulb.command("camp-playlists", "the song playlists from different camps")
@lightbulb.implements(lightbulb.SlashCommand)
async def echo(ctx):
    if ctx.options.camps == "futuristic-camp":
        await ctx.respond("futuristic-link")
    elif ctx.options.camps == "retro-camp":
        await ctx.respond(ctx.options.camps + ": https://open.spotify.com/playlist/2fhDqL3iwb2ar85FlxXE8p")
    elif ctx.options.camps == "general-playlist":
        await ctx.respond(ctx.options.camps + ": https://open.spotify.com/playlist/1bOpQMbSqb1lWmAsqyGcQX")

"""


@bot.command
@lightbulb.option("category", "rule category", choices=["Main", "Minecraft", "Minecraft Shops"],  required=True)
@lightbulb.option("number", "number for the rule", required=True)
@lightbulb.command("rule", "Trigger a rule message", )
@lightbulb.implements(lightbulb.SlashCommand)
async def rule(ctx: lightbulb.Context) -> None:
    if ctx.options.category == "Main":
        await RuleTrig(ctx=ctx, category="main", number=int(ctx.options.number))
    elif ctx.options.category == "Minecraft":
        await RuleTrig(ctx=ctx, category="mcrules", number=int(ctx.options.number))
    elif ctx.options.category == "Minecraft Shops":
        await RuleTrig(ctx=ctx, category="mcshoprules", number=int(ctx.options.number))


@bot.command
@lightbulb.lightbulb.decorators.option("camp-playlist", "the song playlists from different camps",  Optional[Sequence[Union["", "", "", ""]]])
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    pass



@bot.command
@lightbulb.command("group", "testing groups")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass

@my_group.child
@lightbulb.command("subcommand", "subcommand this is")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond("subcommand")

@bot.command
@lightbulb.option("num1", "first number", type=int)
@lightbulb.option("num2", "secound number", type=int)
@lightbulb.command("add", "adds numbers")
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)
"""

bot.run()
